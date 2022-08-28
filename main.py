import sys
import os
import requests
import datetime
import pytz
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
#from PyQt6 import QtGui, QtCore
#from PyQt6.QtGui import QPixmap, QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIcon

# These variables and need to be declared before the rest of the program starts
apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
schedule = []
leagues_list = []
leagues_list_only_names = []
block_names_set = set()
block_names_list = []
block_names_dictionary = {}
league_id = ""
app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LeagueScheduler")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_schedule.hide()
        self.ui.get_schedule.clicked.connect(self.get_schedule)
        self.ui.show_spoilers.hide()
        self.ui.show_spoilers.clicked.connect(self.show_spoilers)
        self.ui.timezone.addItems(pytz.all_timezones)
        self.ui.get_timeoffset.clicked.connect(self.calculate_timezone)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.get_leagues.clicked.connect(self.get_leagues)
        self.ui.chosen_block.hide()

    def get_leagues(self):
        url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-GB"
        payload = {}
        headers = {'hl': 'en-US', 'x-api-key': apikey}
        response = (requests.get(url, headers=headers, data=payload))

        data = response.json()
        my_leagues = data["data"]["leagues"]

        for league in my_leagues:
            temp = {"id": league["id"], "name": league["name"], "image": league["image"]}
            leagues_list.append(temp)
            leagues_list_only_names.append(league["name"])
        leagues_list_only_names.sort()
        for league in leagues_list_only_names:
            self.ui.chosen_league_combo.addItem(league)

        self.ui.chosen_league_combo.currentTextChanged.connect(self.get_block)
        self.ui.chosen_block.show()
        return leagues_list

    def get_block(self):
        block_names_set.clear()
        block_names_list.clear()
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
        upcoming_week_found = False

        for n_event in my_events:
            while not upcoming_week_found:
                if n_event["state"] == "unstarted":
                    upcoming_week = n_event["blockName"]
                    upcoming_week_date = datetime.datetime.strptime(
                        (n_event["startTime"].split("T")[0].replace("-", "/")), "%Y/%m/%d").strftime("%d.%m.%Y")
                    upcoming_week_string = upcoming_week + ", " + upcoming_week_date
                    upcoming_week_found = True
                # elif n_event["state"] == "inProgress":
                #    pass
                else:
                    break
            temp_date = datetime.datetime.strptime((n_event["startTime"].split("T")[0].replace("-", "/")),
                                                   "%Y/%m/%d").strftime("%d.%m.%Y")
            #if n_event["state"] == "inProgress":
            #    continue
            block_names_set.add((str(n_event["blockName"]) + ", " + str(temp_date)))
        self.ui.chosen_block.addItems(sorted(block_names_set, key=lambda x: datetime.datetime.strptime
        (x.split(", ")[1], "%d.%m.%Y").timetuple()))

        if upcoming_week_found:
            upcoming_week_index = self.ui.chosen_block.findText(upcoming_week_string, QtCore.Qt.MatchFlag.MatchContains)
            self.ui.chosen_block.setCurrentIndex(upcoming_week_index)
            self.ui.chosen_block.setItemText(upcoming_week_index,
                                             str(self.ui.chosen_block.currentText()) + " (upcoming block)")
        self.ui.get_schedule.show()

    def calculate_timezone(self):
        timezone_offset = datetime.datetime.now(
            pytz.timezone(self.ui.timezone.currentText())).utcoffset().total_seconds() / 60 / 60
        return timezone_offset

    def calculate_day_of_week(self, start_date):
        day_of_week = start_date.strftime("%A")
        return day_of_week

    def show_spoilers(self):
        self.ui.schedule_table.showColumn(3)
        self.ui.schedule_table.showColumn(4)

    def get_schedule(self):
        pixmap = QPixmap("Nami.png")
        self.ui.picture_label.setPixmap(pixmap)
        self.ui.picture_label.show()
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
        self.ui.timezone_title.pixmap()
        for n_event in my_events:
            key = "blockName"
            if n_event.get(key) is not None:
                if n_event["blockName"] in chosen_block:
                    start_timestamp = datetime.datetime.strptime((n_event["startTime"].replace("T", " ").split("Z")[0]),
                                                             "%Y-%m-%d %H:%M:%S")
                    timezone_offset = datetime.timedelta(hours=self.calculate_timezone())
                    start_timestamp = start_timestamp + timezone_offset
                    start_time = start_timestamp.time()
                    start_date = datetime.datetime.strptime((n_event["startTime"].split("T")[0].replace("-", "/")),
                                                        "%Y/%m/%d").strftime("%d.%m.%Y")
                    day_of_week = self.calculate_day_of_week(start_timestamp)
                    week = n_event["blockName"]
                    team1 = n_event["match"]["teams"][0]["name"]
                    team2 = n_event["match"]["teams"][1]["name"]
                    if n_event["state"] == "unstarted":
                        result = "TBD"
                    else:
                        result = n_event["match"]["teams"][0]["result"]["outcome"]
                    if result == "win":
                        winner = team1
                        f = open('image_name_super_unlikely.png', 'wb')
                        url_logo = n_event["match"]["teams"][0]["image"]
                        f.write(requests.get(url_logo).content)
                        f.close()
                        pixmap = QPixmap("image_name_super_unlikely.png")
                        icon = QIcon(pixmap)
                        icon_table = QtWidgets.QTableWidgetItem()
                        icon_table.setIcon(icon)
                    elif result == "loss":
                        winner = team2
                        f = open('image_name_super_unlikely.png', 'wb')
                        url_logo = n_event["match"]["teams"][1]["image"]
                        f.write(requests.get(url_logo).content)
                        f.close()
                        pixmap = QPixmap("image_name_super_unlikely.png")
                        icon = QIcon(pixmap)
                        icon_table = QtWidgets.QTableWidgetItem()
                        icon_table.setIcon(icon)
                    else:
                        winner = "TBD"
                        pixmap = QPixmap("Nami.png")
                        icon = QIcon(pixmap)
                        icon_table = QtWidgets.QTableWidgetItem()
                        icon_table.setIcon(icon)
                    match = team1 + " vs. " + team2
                    temp = {"startDate": day_of_week + ", " + start_date,
                            "startTime": str(start_time) + " (UTC + " + str(timezone_offset) + ")", "match": match,
                            "winner": winner, "week": week, "picture": icon_table}
                    if str(temp["startDate"]).split(", ")[1] in chosen_block:
                        schedule.append(temp)
                    else:
                        pass
        if os.path.exists("image_name_super_unlikely.png"):
            os.remove("image_name_super_unlikely.png")
        counter = 0
        for item in schedule:
            table_rows = self.ui.schedule_table.rowCount()
            self.ui.schedule_table.insertRow(table_rows)
            self.ui.schedule_table.setItem(counter, 0, QtWidgets.QTableWidgetItem(item["startDate"]))
            self.ui.schedule_table.setItem(counter, 1, QtWidgets.QTableWidgetItem(item["startTime"]))
            self.ui.schedule_table.setItem(counter, 2, QtWidgets.QTableWidgetItem(item["match"]))
            self.ui.schedule_table.setItem(counter, 3, QtWidgets.QTableWidgetItem(item["winner"]))
            self.ui.schedule_table.setItem(counter, 4, QtWidgets.QTableWidgetItem(item["picture"]))
            self.ui.schedule_table.item(counter, 4).setBackground(QtGui.QColor(0, 100, 0))
            self.ui.schedule_table.hideColumn(3)
            self.ui.schedule_table.hideColumn(4)
            counter = counter + 1
        self.ui.schedule_table.resizeColumnsToContents()
        self.ui.show_spoilers.show()


window = MainWindow()
window.show()
sys.exit(app.exec_())
