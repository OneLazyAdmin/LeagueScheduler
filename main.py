import sys
import requests
import json
import datetime
import timedelta
import pytz
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow

# non-changing variable
apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
schedule = []
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

    def calculate_timezone(self):
        timezone_offset = datetime.datetime.now(pytz.timezone(self.ui.timezone.currentText())).utcoffset().total_seconds()/60/60
        print(timezone_offset)
        return timezone_offset
    def calculate_day_of_week(self,start_date):
        day_of_week = start_date.strftime("%A")
        return day_of_week

    def get_schedule(self):
        schedule.clear()
        self.ui.schedule_table.setRowCount(0)
        url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-GB&leagueId=98767991302996019"
        payload = {}
        headers = {'hl': 'en-US', 'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}
        chosen_league = self.ui.chosen_league.currentText()
        chosen_week = 'Week ' + str(self.ui.chosen_week.value())
        print(chosen_week)
        response = (requests.get(url, headers=headers, data=payload))
        data = response.json()
        schedule_pretty = json.dumps(data, indent=4)
        schedule_file = json.dumps(data)
        print(data)
        self.ui.timezone_title.pixmap()
        my_events = data["data"]["schedule"]["events"]
        for n_event in my_events:
            if n_event["blockName"] == chosen_week:
                print(n_event)
                #start_time = n_event["startTime"].split("T")[1].split("Z")[0]
                #print(start_time)
                start_timestamp = datetime.datetime.strptime((n_event["startTime"].replace("T", " ").split("Z")[0]), "%Y-%m-%d %H:%M:%S")
                timezone_offset = datetime.timedelta(hours=self.calculate_timezone())
                start_timestamp = start_timestamp + timezone_offset
                start_time = start_timestamp.time()
                print(start_time)
                start_date = datetime.datetime.strptime((n_event["startTime"].split("T")[0].replace("-", "/")),\
                                                        "%Y/%m/%d").strftime("%d.%m.%Y")
                day_of_week = self.calculate_day_of_week(start_timestamp)


                print(start_date)
                week = n_event["blockName"].split(" ")[1]
                print(week)
                # print(n_event["match"]["teams"])
                team1 = n_event["match"]["teams"][0]["name"]
                print(team1)
                team2 = n_event["match"]["teams"][1]["name"]
                print(team2)
                result = n_event["match"]["teams"][0]["result"]["outcome"]
                print(result)
                if result == "win":
                    winner = team1
                elif result == "loss":
                    winner = team2
                elif result is None:
                    winner = "TBD"
                print(winner)
                match = team1 + " vs. " + team2
                print(match)
                temp = {"startDate": day_of_week +", " + start_date, "startTime": str(start_time) + " (UTC + " + str(timezone_offset) + ")", "match": match,\
                        "winner": winner, "week": week}
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
            counter = counter + 1
        self.ui.schedule_table.resizeColumnToContents(2)


window = MainWindow()
window.show()
sys.exit(app.exec_())
