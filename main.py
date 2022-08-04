import sys
import requests
import json
import datetime
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
        my_events = data["data"]["schedule"]["events"]
        for n_event in my_events:
            if n_event["blockName"] == chosen_week:
                start_time = n_event["startTime"].split("T")[1].split("Z")[0]
                start_date = datetime.datetime.strptime((n_event["startTime"].split("T")[0].replace("-", "/")), "%Y/%m/%d").strftime("%d.%m.%Y")
                week = n_event["blockName"].split(" ")[1]
                # print(n_event["match"]["teams"])
                team1 = n_event["match"]["teams"][0]["name"]
                team2 = n_event["match"]["teams"][1]["name"]
                result = n_event["match"]["teams"][0]["result"]["outcome"]
                if result == "win":
                    winner = team1
                elif result == "loss":
                    winner = team2
                elif result is None:
                    winner = "TBD"
                match = team1 + " vs. " + team2
                # print(team1 + " vs. " + team2)
                temp = {"startDate": start_date, "startTime": start_time + " UTC", "match": match, "winner": winner, "week": week}
                #print(temp)
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
