import sys
import requests
import json
import datetime
import timedelta
import pytz
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap, QImage, QIcon

# non-changing variable
apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
schedule = []
leagues_list = []
leagues_list_only_names = []
block_names = set()
league_id = ""
app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Scheduler")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_schedule.clicked.connect(self.get_schedule)
        self.ui.timezone.addItems(pytz.all_timezones)
        self.ui.get_timeoffset.clicked.connect(self.calculate_timezone)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.show_spoilers.clicked.connect(self.show_spoilers)
        self.ui.get_leagues.clicked.connect(self.get_leagues)

    def get_leagues(self):
        url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-GB"
        payload = {}
        headers = {'hl': 'en-US', 'x-api-key': apikey}
        response = (requests.get(url, headers=headers, data=payload))


        print(response.content)
        data = response.json()
        print(data)
        my_leagues = data["data"]["leagues"]

        for league in my_leagues:
            print(league["id"])
            print(league["name"])
            print(league["image"])
            temp = {"id": league["id"], "name": league["name"], "image": league["image"]}
            leagues_list.append(temp)
            leagues_list_only_names.append(league["name"])
        leagues_list_only_names.sort()
        for league in leagues_list_only_names:
            self.ui.chosen_league_combo.addItem(league)

        self.ui.chosen_league_combo.currentTextChanged.connect(self.get_block)
        return leagues_list
    def get_block(self):
        block_names.clear()
        self.ui.chosen_block.clear()
        chosen_league = self.ui.chosen_league_combo.currentText()
        for d in leagues_list:
            if d['name'] == chosen_league:
                league_id = d['id']
        url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-GB&leagueId=" + league_id
        payload = {}
        headers = {'hl': 'en-US', 'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}
        response = (requests.get(url, headers=headers, data=payload))
        data = response.json()
        my_events = data["data"]["schedule"]["events"]
        for n_event in my_events:
            block_names.add(n_event["blockName"])
        self.ui.chosen_block.addItems(block_names)
        return data

    def calculate_timezone(self):
        timezone_offset = datetime.datetime.now(
            pytz.timezone(self.ui.timezone.currentText())).utcoffset().total_seconds() / 60 / 60
        print(timezone_offset)
        return timezone_offset

    def calculate_day_of_week(self, start_date):
        day_of_week = start_date.strftime("%A")
        return day_of_week
    def show_spoilers(self):
        self.ui.schedule_table.showColumn(3)
        self.ui.schedule_table.showColumn(4)
    def get_schedule(self):
        #pixmap = QPixmap("Nami.png")
        #print(pixmap)
        #self.ui.picture_label.setPixmap(pixmap)
        #self.ui.picture_label.show()
        schedule.clear()
        self.ui.schedule_table.setRowCount(0)
        chosen_league = self.ui.chosen_league_combo.currentText()
        for d in leagues_list:
            if d['name'] == chosen_league:
                league_id = d['id']
        url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-GB&leagueId=" + league_id
        payload = {}
        headers = {'hl': 'en-US', 'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}
        response = (requests.get(url, headers=headers, data=payload))
        data = response.json()
        my_events = data["data"]["schedule"]["events"]
        chosen_block = self.ui.chosen_block.currentText()
        print(chosen_block)
        schedule_pretty = json.dumps(data, indent=4)
        schedule_file = json.dumps(data)
        print(data)
        self.ui.timezone_title.pixmap()
        for n_event in my_events:
            if n_event["blockName"] == chosen_block:
                print(n_event)
                # start_time = n_event["startTime"].split("T")[1].split("Z")[0]
                # print(start_time)
                start_timestamp = datetime.datetime.strptime((n_event["startTime"].replace("T", " ").split("Z")[0]),
                                                             "%Y-%m-%d %H:%M:%S")
                timezone_offset = datetime.timedelta(hours=self.calculate_timezone())
                start_timestamp = start_timestamp + timezone_offset
                start_time = start_timestamp.time()
                print(start_time)
                start_date = datetime.datetime.strptime((n_event["startTime"].split("T")[0].replace("-", "/")),
                                                        "%Y/%m/%d").strftime("%d.%m.%Y")
                day_of_week = self.calculate_day_of_week(start_timestamp)

                print(start_date)
                week = n_event["blockName"]
                #print(week)
                # print(n_event["match"]["teams"])
                team1 = n_event["match"]["teams"][0]["name"]
                print(team1)
                team2 = n_event["match"]["teams"][1]["name"]
                print(team2)
                result = n_event["match"]["teams"][0]["result"]["outcome"]
                print(result)
                if result == "win":
                    winner = team1
                    f = open('image.png', 'wb')
                    url_logo = n_event["match"]["teams"][0]["image"]
                    f.write(requests.get(url_logo).content)
                    f.close()
                    pixmap = QPixmap("image.png")
                    icon = QIcon(pixmap)
                    icon_table = QtWidgets.QTableWidgetItem()
                    icon_table.setIcon(icon)
                elif result == "loss":
                    winner = team2
                    f = open('image.png', 'wb')
                    url_logo = n_event["match"]["teams"][1]["image"]
                    f.write(requests.get(url_logo).content)
                    f.close()
                    pixmap = QPixmap("image.png")
                    icon = QIcon(pixmap)
                    icon_table = QtWidgets.QTableWidgetItem()
                    icon_table.setIcon(icon)
                else:
                    winner = "TBD"
                    pixmap = QPixmap("Nami.png")
                    icon = QIcon(pixmap)
                    icon_table = QtWidgets.QTableWidgetItem()
                    icon_table.setIcon(icon)
                print(winner)
                match = team1 + " vs. " + team2
                print(match)
                temp = {"startDate": day_of_week + ", " + start_date,
                        "startTime": str(start_time) + " (UTC + " + str(timezone_offset) + ")", "match": match, \
                        "winner": winner, "week": week, "picture": icon_table}
                print(temp)
                schedule.append(temp)

        print(schedule)
        print(schedule[0])
        counter = 0
        for item in schedule:
            table_rows = self.ui.schedule_table.rowCount()
            print(table_rows)
            self.ui.schedule_table.insertRow(table_rows)
            self.ui.schedule_table.setItem(counter, 0, QtWidgets.QTableWidgetItem(item["startDate"]))
            self.ui.schedule_table.setItem(counter, 1, QtWidgets.QTableWidgetItem(item["startTime"]))
            self.ui.schedule_table.setItem(counter, 2, QtWidgets.QTableWidgetItem(item["match"]))
            self.ui.schedule_table.setItem(counter, 3, QtWidgets.QTableWidgetItem(item["winner"]))
            self.ui.schedule_table.setItem(counter, 4, QtWidgets.QTableWidgetItem(item["picture"]))
            self.ui.schedule_table.item(counter, 4).setBackground(QtGui.QColor(0,100,0))
            self.ui.schedule_table.hideColumn(3)
            self.ui.schedule_table.hideColumn(4)
            counter = counter + 1
        self.ui.schedule_table.resizeColumnsToContents()
        print(block_names)

window = MainWindow()
window.show()
sys.exit(app.exec_())
