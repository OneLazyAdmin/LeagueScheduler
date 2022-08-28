# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Nami.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.gridLayout = QtWidgets.QGridLayout(self.Main)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chosen_league_title = QtWidgets.QLabel(self.Main)
        self.chosen_league_title.setObjectName("chosen_league_title")
        self.verticalLayout_2.addWidget(self.chosen_league_title)
        self.get_leagues = QtWidgets.QPushButton(self.Main)
        self.get_leagues.setObjectName("get_leagues")
        self.verticalLayout_2.addWidget(self.get_leagues)
        self.chosen_league_combo = QtWidgets.QComboBox(self.Main)
        self.chosen_league_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.chosen_league_combo.setObjectName("chosen_league_combo")
        self.verticalLayout_2.addWidget(self.chosen_league_combo)
        self.chosen_block_title = QtWidgets.QLabel(self.Main)
        self.chosen_block_title.setObjectName("chosen_block_title")
        self.verticalLayout_2.addWidget(self.chosen_block_title)
        self.chosen_block = QtWidgets.QComboBox(self.Main)
        self.chosen_block.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.chosen_block.setObjectName("chosen_block")
        self.verticalLayout_2.addWidget(self.chosen_block)
        self.get_schedule = QtWidgets.QPushButton(self.Main)
        self.get_schedule.setDefault(True)
        self.get_schedule.setObjectName("get_schedule")
        self.verticalLayout_2.addWidget(self.get_schedule)
        self.show_spoilers = QtWidgets.QPushButton(self.Main)
        self.show_spoilers.setObjectName("show_spoilers")
        self.verticalLayout_2.addWidget(self.show_spoilers)
        self.schedule_table = QtWidgets.QTableWidget(self.Main)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.schedule_table.setFont(font)
        self.schedule_table.setAutoFillBackground(False)
        self.schedule_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.schedule_table.setObjectName("schedule_table")
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 0, 0))
        self.schedule_table.setHorizontalHeaderItem(4, item)
        self.schedule_table.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.schedule_table)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Main, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Settings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.timezone_title = QtWidgets.QLabel(self.Settings)
        self.timezone_title.setObjectName("timezone_title")
        self.gridLayout_3.addWidget(self.timezone_title, 3, 0, 1, 1)
        self.timezone = QtWidgets.QComboBox(self.Settings)
        self.timezone.setObjectName("timezone")
        self.gridLayout_3.addWidget(self.timezone, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.Settings)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 1)
        self.picture_label = QtWidgets.QLabel(self.Settings)
        self.picture_label.setScaledContents(False)
        self.picture_label.setObjectName("picture_label")
        self.gridLayout_3.addWidget(self.picture_label, 0, 0, 1, 1)
        self.timezone_2 = QtWidgets.QComboBox(self.Settings)
        self.timezone_2.setObjectName("timezone_2")
        self.gridLayout_3.addWidget(self.timezone_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Settings)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.get_timeoffset_2 = QtWidgets.QPushButton(self.Settings)
        self.get_timeoffset_2.setObjectName("get_timeoffset_2")
        self.gridLayout_3.addWidget(self.get_timeoffset_2, 2, 1, 1, 1)
        self.get_timeoffset = QtWidgets.QPushButton(self.Settings)
        self.get_timeoffset.setObjectName("get_timeoffset")
        self.gridLayout_3.addWidget(self.get_timeoffset, 4, 1, 1, 1)
        self.tabWidget.addTab(self.Settings, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuLeague_Scheduler = QtWidgets.QMenu(self.menubar)
        self.menuLeague_Scheduler.setObjectName("menuLeague_Scheduler")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLeague_Scheduler.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chosen_league_title.setText(_translate("MainWindow", "League"))
        self.get_leagues.setText(_translate("MainWindow", "Get Leagues!"))
        self.chosen_block_title.setText(_translate("MainWindow", "Block"))
        self.get_schedule.setText(_translate("MainWindow", "Get Schedule!"))
        self.show_spoilers.setText(_translate("MainWindow", "Show Spoilers!"))
        item = self.schedule_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "StartDate"))
        item = self.schedule_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Starttime"))
        item = self.schedule_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Match"))
        item = self.schedule_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Winner"))
        item = self.schedule_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Picture"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), _translate("MainWindow", "Main"))
        self.timezone_title.setText(_translate("MainWindow", "Timezone"))
        self.picture_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Dateformat"))
        self.get_timeoffset_2.setText(_translate("MainWindow", "Select-Dateformat"))
        self.get_timeoffset.setText(_translate("MainWindow", "Get-Timeoffset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.menuLeague_Scheduler.setTitle(_translate("MainWindow", "League Scheduler"))
