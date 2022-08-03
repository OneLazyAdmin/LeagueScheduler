import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_schedule.clicked.connect(self.onPushButtonClick)
        self.ui.tableWidget.cellChanged.connect(self.onCellChanged)

    def onPushButtonClick(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Budapest"))
        self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("9876"))
        print("Button wurde geklickt")

    def onCellChanged(self, row, col):
        print(row)
        print(col)

window = MainWindow()

#ui_window = Ui_MainWindow()
#ui_window.setupUi(window)
window.show()
sys.exit(app.exec_())
