from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from app_logic import AppManager

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1451, 834)
        MainWindow.setMinimumSize(QtCore.QSize(1448, 834))
        MainWindow.setMaximumSize(QtCore.QSize(1455, 837))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/blood-bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 80)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QTableWidget{border-radius: 20px;\n"
"}\n"
"#groupBox_2, #groupBox, #groupBox_3{\n"
"border-radius: 10px;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.Seconds_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.Seconds_LCD.setGeometry(QtCore.QRect(700, 10, 80, 30))
        self.Seconds_LCD.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Seconds_LCD.setFont(font)
        self.Seconds_LCD.setProperty("intValue", 53)
        self.Seconds_LCD.setObjectName("Seconds_LCD")
        self.Minutes_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.Minutes_LCD.setGeometry(QtCore.QRect(570, 10, 80, 31))
        self.Minutes_LCD.setMaximumSize(QtCore.QSize(80, 200))
        self.Minutes_LCD.setStyleSheet("")
        self.Minutes_LCD.setProperty("intValue", 20)
        self.Minutes_LCD.setObjectName("Minutes_LCD")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 10, 16, 31))
        self.label.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 50, 611, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color: white;")
        self.groupBox_4.setObjectName("groupBox_4")
        self.inventory_table = QtWidgets.QTableWidget(self.groupBox_4)
        self.inventory_table.setGeometry(QtCore.QRect(100, 20, 421, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_table.sizePolicy().hasHeightForWidth())
        self.inventory_table.setSizePolicy(sizePolicy)
        self.inventory_table.setMinimumSize(QtCore.QSize(200, 0))
        self.inventory_table.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color:rgb(0, 99, 73);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:transparent;\n"
"}\n"
"QTableWidget {\n"
"    background-color: transparent; /* Main background */\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgb(50, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.inventory_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.inventory_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inventory_table.setObjectName("inventory_table")
        self.inventory_table.setColumnCount(3)
        self.inventory_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.inventory_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.inventory_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.inventory_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventory_table.setItem(7, 2, item)
        self.inventory_table.horizontalHeader().setDefaultSectionSize(132)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(670, 50, 731, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("color: white;")
        self.groupBox_5.setObjectName("groupBox_5")
        self.hospitals_table = QtWidgets.QTableWidget(self.groupBox_5)
        self.hospitals_table.setGeometry(QtCore.QRect(110, 20, 521, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hospitals_table.sizePolicy().hasHeightForWidth())
        self.hospitals_table.setSizePolicy(sizePolicy)
        self.hospitals_table.setMinimumSize(QtCore.QSize(200, 0))
        self.hospitals_table.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color:rgb(0, 99, 73);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:transparent;\n"
"}\n"
"QTableWidget {\n"
"    background-color: transparent; /* Main background */\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgb(50, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.hospitals_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.hospitals_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.hospitals_table.setObjectName("hospitals_table")
        self.hospitals_table.setColumnCount(3)
        self.hospitals_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.hospitals_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.hospitals_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.hospitals_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospitals_table.setItem(7, 2, item)
        self.hospitals_table.horizontalHeader().setDefaultSectionSize(166)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 420, 1371, 391))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("color: white;")
        self.groupBox_6.setObjectName("groupBox_6")
        self.orders_table = QtWidgets.QTableWidget(self.groupBox_6)
        self.orders_table.setGeometry(QtCore.QRect(20, 30, 681, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orders_table.sizePolicy().hasHeightForWidth())
        self.orders_table.setSizePolicy(sizePolicy)
        self.orders_table.setMinimumSize(QtCore.QSize(0, 0))
        self.orders_table.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color:rgb(0, 99, 73);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:transparent;\n"
"}\n"
"QTableWidget {\n"
"    background-color: transparent; /* Main background */\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgb(50, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.orders_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.orders_table.setObjectName("orders_table")
        self.orders_table.setColumnCount(5)
        self.orders_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_table.horizontalHeader().setDefaultSectionSize(127)
        self.stop_button = QtWidgets.QPushButton(self.groupBox_6, clicked=lambda: app_manager.stop_simulation())
        self.stop_button.setGeometry(QtCore.QRect(210, 310, 171, 41))
        self.stop_button.setMinimumSize(QtCore.QSize(171, 0))
        self.stop_button.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("QPushButton {\n"
"    background-color: #E0115F; \n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #B00D4C;\n"
"    border: 1.2px inset gray;\n"
"}\n"
"")
        self.stop_button.setObjectName("stop_button")
        self.start_button = QtWidgets.QPushButton(self.groupBox_6, clicked=lambda: app_manager.start())
        self.start_button.setGeometry(QtCore.QRect(980, 320, 171, 41))
        self.start_button.setMinimumSize(QtCore.QSize(171, 0))
        self.start_button.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton {\n"
"    background-color: #00A86B; \n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #00804D;\n"
"    border: 1.2px inset gray;\n"
"}\n"
"")
        self.start_button.setObjectName("start_button")
        self.output_table = QtWidgets.QTableWidget(self.groupBox_6)
        self.output_table.setGeometry(QtCore.QRect(760, 30, 581, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_table.sizePolicy().hasHeightForWidth())
        self.output_table.setSizePolicy(sizePolicy)
        self.output_table.setMinimumSize(QtCore.QSize(0, 0))
        self.output_table.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color:rgb(0, 99, 73);\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:transparent;\n"
"}\n"
"QTableWidget {\n"
"    background-color: transparent; /* Main background */\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgb(50, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.output_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.output_table.setObjectName("output_table")
        self.output_table.setColumnCount(4)
        self.output_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.output_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.output_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.output_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.output_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output_table.setItem(7, 0, item)
        self.output_table.horizontalHeader().setDefaultSectionSize(134)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Blood Bank Dashboard"))
        self.label.setText(_translate("MainWindow", ":"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Inventory"))
        item = self.inventory_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.inventory_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.inventory_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.inventory_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.inventory_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.inventory_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.inventory_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.inventory_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.inventory_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Blood Type"))
        item = self.inventory_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Remaining Bags"))
        item = self.inventory_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Component"))
        __sortingEnabled = self.inventory_table.isSortingEnabled()
        self.inventory_table.setSortingEnabled(False)
        item = self.inventory_table.item(0, 0)
        item.setText(_translate("MainWindow", "A+"))
        item = self.inventory_table.item(0, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(0, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(1, 0)
        item.setText(_translate("MainWindow", "A-"))
        item = self.inventory_table.item(1, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(1, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(2, 0)
        item.setText(_translate("MainWindow", "B+"))
        item = self.inventory_table.item(2, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(2, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(3, 0)
        item.setText(_translate("MainWindow", "B-"))
        item = self.inventory_table.item(3, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(3, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(4, 0)
        item.setText(_translate("MainWindow", "AB+"))
        item = self.inventory_table.item(4, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(4, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(5, 0)
        item.setText(_translate("MainWindow", "AB-"))
        item = self.inventory_table.item(5, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(5, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(6, 0)
        item.setText(_translate("MainWindow", "O+"))
        item = self.inventory_table.item(6, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(6, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        item = self.inventory_table.item(7, 0)
        item.setText(_translate("MainWindow", "O-"))
        item = self.inventory_table.item(7, 1)
        item.setText(_translate("MainWindow", "1000"))
        item = self.inventory_table.item(7, 2)
        item.setText(_translate("MainWindow", "Whole blood"))
        self.inventory_table.setSortingEnabled(__sortingEnabled)
        self.groupBox_5.setTitle(_translate("MainWindow", "Hospitals"))
        item = self.hospitals_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.hospitals_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.hospitals_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.hospitals_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.hospitals_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.hospitals_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.hospitals_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.hospitals_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.hospitals_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hospital Name"))
        item = self.hospitals_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Beds"))
        item = self.hospitals_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class"))
        __sortingEnabled = self.hospitals_table.isSortingEnabled()
        self.hospitals_table.setSortingEnabled(False)
        item = self.hospitals_table.item(0, 0)
        item.setText(_translate("MainWindow", "Ain Shams"))
        item = self.hospitals_table.item(0, 1)
        item.setText(_translate("MainWindow", "200"))
        item = self.hospitals_table.item(0, 2)
        item.setText(_translate("MainWindow", "A"))
        item = self.hospitals_table.item(1, 0)
        item.setText(_translate("MainWindow", "Saudi German"))
        item = self.hospitals_table.item(1, 1)
        item.setText(_translate("MainWindow", "190"))
        item = self.hospitals_table.item(1, 2)
        item.setText(_translate("MainWindow", "A"))
        item = self.hospitals_table.item(2, 0)
        item.setText(_translate("MainWindow", "Cleopatra"))
        item = self.hospitals_table.item(2, 1)
        item.setText(_translate("MainWindow", "182"))
        item = self.hospitals_table.item(2, 2)
        item.setText(_translate("MainWindow", "A"))
        item = self.hospitals_table.item(3, 0)
        item.setText(_translate("MainWindow", "El Nozha"))
        item = self.hospitals_table.item(3, 1)
        item.setText(_translate("MainWindow", "120"))
        item = self.hospitals_table.item(3, 2)
        item.setText(_translate("MainWindow", "B"))
        item = self.hospitals_table.item(4, 0)
        item.setText(_translate("MainWindow", "El Safa"))
        item = self.hospitals_table.item(4, 1)
        item.setText(_translate("MainWindow", "100"))
        item = self.hospitals_table.item(4, 2)
        item.setText(_translate("MainWindow", "B"))
        item = self.hospitals_table.item(5, 0)
        item.setText(_translate("MainWindow", "Wadi El Neel"))
        item = self.hospitals_table.item(5, 1)
        item.setText(_translate("MainWindow", "90"))
        item = self.hospitals_table.item(5, 2)
        item.setText(_translate("MainWindow", "C"))
        item = self.hospitals_table.item(6, 0)
        item.setText(_translate("MainWindow", "Cardiac Center"))
        item = self.hospitals_table.item(6, 1)
        item.setText(_translate("MainWindow", "82"))
        item = self.hospitals_table.item(6, 2)
        item.setText(_translate("MainWindow", "C"))
        item = self.hospitals_table.item(7, 0)
        item.setText(_translate("MainWindow", "Ibn Sina"))
        item = self.hospitals_table.item(7, 1)
        item.setText(_translate("MainWindow", "75"))
        item = self.hospitals_table.item(7, 2)
        item.setText(_translate("MainWindow", "C"))
        self.hospitals_table.setSortingEnabled(__sortingEnabled)
        self.groupBox_6.setTitle(_translate("MainWindow", "Orders"))
        item = self.orders_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.orders_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hospital"))
        item = self.orders_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Needed Type"))
        item = self.orders_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Needed bags"))
        item = self.orders_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Remaining"))
        item = self.orders_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        __sortingEnabled = self.orders_table.isSortingEnabled()
        self.orders_table.setSortingEnabled(False)
        self.orders_table.setSortingEnabled(__sortingEnabled)
        self.stop_button.setText(_translate("MainWindow", "Stop Simulation"))
        self.start_button.setText(_translate("MainWindow", "Start Simulation"))
        item = self.output_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "6"))
        item = self.output_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.output_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "5"))
        item = self.output_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "8"))
        item = self.output_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "2"))
        item = self.output_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "7"))
        item = self.output_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "3"))
        item = self.output_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "4"))
        item = self.output_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Needed Type"))
        item = self.output_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nedded Bags"))
        item = self.output_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hospital"))
        item = self.output_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        __sortingEnabled = self.output_table.isSortingEnabled()
        self.output_table.setSortingEnabled(False)
        self.output_table.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app_manager = AppManager(ui)
    MainWindow.show()
    sys.exit(app.exec_())