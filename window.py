# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.balanceDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.balanceDisplay.setGeometry(QtCore.QRect(60, 20, 311, 61))
        self.balanceDisplay.setDigitCount(12)
        self.balanceDisplay.setProperty("value", 0.0)
        self.balanceDisplay.setObjectName("balanceDisplay")
        self.dollarLabel = QtWidgets.QLabel(self.centralwidget)
        self.dollarLabel.setGeometry(QtCore.QRect(10, 20, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dollarLabel.setFont(font)
        self.dollarLabel.setObjectName("dollarLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 991, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.expensesTab = QtWidgets.QWidget()
        self.expensesTab.setObjectName("expensesTab")
        self.expensesTable = QtWidgets.QTableWidget(self.expensesTab)
        self.expensesTable.setGeometry(QtCore.QRect(10, 10, 561, 621))
        self.expensesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.expensesTable.setDragEnabled(True)
        self.expensesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.expensesTable.setObjectName("expensesTable")
        self.expensesTable.setColumnCount(4)
        self.expensesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.expensesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.expensesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.expensesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.expensesTable.setHorizontalHeaderItem(3, item)
        self.expensesTable.verticalHeader().setVisible(False)
        self.editExpense = QtWidgets.QGroupBox(self.expensesTab)
        self.editExpense.setGeometry(QtCore.QRect(580, 270, 391, 411))
        self.editExpense.setObjectName("editExpense")
        self.transferLabel = QtWidgets.QLabel(self.editExpense)
        self.transferLabel.setGeometry(QtCore.QRect(10, 300, 61, 16))
        self.transferLabel.setObjectName("transferLabel")
        self.dateLabel = QtWidgets.QLabel(self.editExpense)
        self.dateLabel.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.editExpense)
        self.descriptionLabel.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.amountLabel = QtWidgets.QLabel(self.editExpense)
        self.amountLabel.setGeometry(QtCore.QRect(10, 340, 61, 16))
        self.amountLabel.setObjectName("amountLabel")
        self.expenseCalendar = QtWidgets.QCalendarWidget(self.editExpense)
        self.expenseCalendar.setGeometry(QtCore.QRect(50, 30, 321, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.expenseCalendar.setFont(font)
        self.expenseCalendar.setGridVisible(False)
        self.expenseCalendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.expenseCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.expenseCalendar.setObjectName("expenseCalendar")
        self.expenseAmountBox = QtWidgets.QDoubleSpinBox(self.editExpense)
        self.expenseAmountBox.setGeometry(QtCore.QRect(90, 340, 111, 22))
        self.expenseAmountBox.setMaximum(999999999.99)
        self.expenseAmountBox.setSingleStep(0.01)
        self.expenseAmountBox.setObjectName("expenseAmountBox")
        self.expenseDescriptionBox = QtWidgets.QLineEdit(self.editExpense)
        self.expenseDescriptionBox.setGeometry(QtCore.QRect(90, 260, 281, 20))
        self.expenseDescriptionBox.setObjectName("expenseDescriptionBox")
        self.expenseTransferBox = QtWidgets.QLineEdit(self.editExpense)
        self.expenseTransferBox.setGeometry(QtCore.QRect(90, 300, 281, 20))
        self.expenseTransferBox.setObjectName("expenseTransferBox")
        self.addExpense = QtWidgets.QPushButton(self.editExpense)
        self.addExpense.setGeometry(QtCore.QRect(10, 370, 181, 31))
        self.addExpense.setObjectName("addExpense")
        self.removeExpenses = QtWidgets.QPushButton(self.editExpense)
        self.removeExpenses.setGeometry(QtCore.QRect(200, 370, 181, 31))
        self.removeExpenses.setObjectName("removeExpenses")
        self.label_13 = QtWidgets.QLabel(self.editExpense)
        self.label_13.setGeometry(QtCore.QRect(70, 340, 16, 20))
        self.label_13.setObjectName("label_13")
        self.requiredPayments = QtWidgets.QGroupBox(self.expensesTab)
        self.requiredPayments.setGeometry(QtCore.QRect(580, 10, 391, 251))
        self.requiredPayments.setObjectName("requiredPayments")
        self.totalLabel = QtWidgets.QLabel(self.requiredPayments)
        self.totalLabel.setGeometry(QtCore.QRect(10, 220, 111, 16))
        self.totalLabel.setObjectName("totalLabel")
        self.totalBox = QtWidgets.QLineEdit(self.requiredPayments)
        self.totalBox.setEnabled(True)
        self.totalBox.setGeometry(QtCore.QRect(170, 220, 131, 20))
        self.totalBox.setReadOnly(True)
        self.totalBox.setObjectName("totalBox")
        self.stateSelect = QtWidgets.QComboBox(self.requiredPayments)
        self.stateSelect.setGeometry(QtCore.QRect(160, 30, 141, 22))
        self.stateSelect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stateSelect.setObjectName("stateSelect")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.stateSelect.addItem("")
        self.label_9 = QtWidgets.QLabel(self.requiredPayments)
        self.label_9.setGeometry(QtCore.QRect(150, 120, 16, 20))
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.requiredPayments)
        self.label_12.setGeometry(QtCore.QRect(150, 220, 16, 20))
        self.label_12.setObjectName("label_12")
        self.miscLabel = QtWidgets.QLabel(self.requiredPayments)
        self.miscLabel.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.miscLabel.setObjectName("miscLabel")
        self.label_8 = QtWidgets.QLabel(self.requiredPayments)
        self.label_8.setGeometry(QtCore.QRect(150, 90, 16, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.requiredPayments)
        self.label_7.setGeometry(QtCore.QRect(150, 60, 16, 20))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.requiredPayments)
        self.label_10.setGeometry(QtCore.QRect(150, 150, 16, 20))
        self.label_10.setObjectName("label_10")
        self.costOfLivingLabel = QtWidgets.QLabel(self.requiredPayments)
        self.costOfLivingLabel.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.costOfLivingLabel.setObjectName("costOfLivingLabel")
        self.groceriesBox = QtWidgets.QDoubleSpinBox(self.requiredPayments)
        self.groceriesBox.setGeometry(QtCore.QRect(170, 60, 131, 22))
        self.groceriesBox.setMaximum(999999999.99)
        self.groceriesBox.setSingleStep(0.01)
        self.groceriesBox.setObjectName("groceriesBox")
        self.utilitiesLabel = QtWidgets.QLabel(self.requiredPayments)
        self.utilitiesLabel.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.utilitiesLabel.setObjectName("utilitiesLabel")
        self.transportationBox = QtWidgets.QDoubleSpinBox(self.requiredPayments)
        self.transportationBox.setGeometry(QtCore.QRect(170, 150, 131, 22))
        self.transportationBox.setMaximum(999999999.99)
        self.transportationBox.setSingleStep(0.01)
        self.transportationBox.setObjectName("transportationBox")
        self.transportationLabel = QtWidgets.QLabel(self.requiredPayments)
        self.transportationLabel.setGeometry(QtCore.QRect(10, 150, 111, 16))
        self.transportationLabel.setObjectName("transportationLabel")
        self.housingBox = QtWidgets.QDoubleSpinBox(self.requiredPayments)
        self.housingBox.setGeometry(QtCore.QRect(170, 90, 131, 22))
        self.housingBox.setMaximum(999999999.99)
        self.housingBox.setSingleStep(0.01)
        self.housingBox.setObjectName("housingBox")
        self.miscBox = QtWidgets.QDoubleSpinBox(self.requiredPayments)
        self.miscBox.setGeometry(QtCore.QRect(170, 180, 131, 22))
        self.miscBox.setMaximum(999999999.99)
        self.miscBox.setSingleStep(0.01)
        self.miscBox.setObjectName("miscBox")
        self.housingLabel = QtWidgets.QLabel(self.requiredPayments)
        self.housingLabel.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.housingLabel.setObjectName("housingLabel")
        self.label_11 = QtWidgets.QLabel(self.requiredPayments)
        self.label_11.setGeometry(QtCore.QRect(150, 180, 16, 20))
        self.label_11.setObjectName("label_11")
        self.utilitiesBox = QtWidgets.QDoubleSpinBox(self.requiredPayments)
        self.utilitiesBox.setGeometry(QtCore.QRect(170, 120, 131, 22))
        self.utilitiesBox.setMaximum(999999999.99)
        self.utilitiesBox.setSingleStep(0.01)
        self.utilitiesBox.setObjectName("utilitiesBox")
        self.groceriesLabel = QtWidgets.QLabel(self.requiredPayments)
        self.groceriesLabel.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.groceriesLabel.setObjectName("groceriesLabel")
        self.label_14 = QtWidgets.QLabel(self.requiredPayments)
        self.label_14.setGeometry(QtCore.QRect(310, 60, 51, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.requiredPayments)
        self.label_15.setGeometry(QtCore.QRect(310, 90, 51, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.requiredPayments)
        self.label_16.setGeometry(QtCore.QRect(310, 120, 51, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.requiredPayments)
        self.label_17.setGeometry(QtCore.QRect(310, 150, 51, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.requiredPayments)
        self.label_18.setGeometry(QtCore.QRect(310, 180, 51, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.requiredPayments)
        self.label_19.setGeometry(QtCore.QRect(310, 220, 51, 20))
        self.label_19.setObjectName("label_19")
        self.grandTotalExpensesBox = QtWidgets.QLineEdit(self.expensesTab)
        self.grandTotalExpensesBox.setEnabled(True)
        self.grandTotalExpensesBox.setGeometry(QtCore.QRect(317, 652, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grandTotalExpensesBox.setFont(font)
        self.grandTotalExpensesBox.setReadOnly(True)
        self.grandTotalExpensesBox.setObjectName("grandTotalExpensesBox")
        self.grandTotalLabel = QtWidgets.QLabel(self.expensesTab)
        self.grandTotalLabel.setGeometry(QtCore.QRect(10, 650, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grandTotalLabel.setFont(font)
        self.grandTotalLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.grandTotalLabel.setObjectName("grandTotalLabel")
        self.editExpense.raise_()
        self.requiredPayments.raise_()
        self.expensesTable.raise_()
        self.grandTotalExpensesBox.raise_()
        self.grandTotalLabel.raise_()
        self.tabWidget.addTab(self.expensesTab, "")
        self.assetsTab = QtWidgets.QWidget()
        self.assetsTab.setObjectName("assetsTab")
        self.assetsTable = QtWidgets.QTableWidget(self.assetsTab)
        self.assetsTable.setGeometry(QtCore.QRect(10, 10, 561, 621))
        self.assetsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.assetsTable.setDragEnabled(True)
        self.assetsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.assetsTable.setObjectName("assetsTable")
        self.assetsTable.setColumnCount(3)
        self.assetsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.assetsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.assetsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.assetsTable.setHorizontalHeaderItem(2, item)
        self.assetsTable.verticalHeader().setVisible(False)
        self.grandTotalLabel_2 = QtWidgets.QLabel(self.assetsTab)
        self.grandTotalLabel_2.setGeometry(QtCore.QRect(10, 650, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grandTotalLabel_2.setFont(font)
        self.grandTotalLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.grandTotalLabel_2.setObjectName("grandTotalLabel_2")
        self.grandTotalAssetsBox = QtWidgets.QLineEdit(self.assetsTab)
        self.grandTotalAssetsBox.setEnabled(True)
        self.grandTotalAssetsBox.setGeometry(QtCore.QRect(317, 652, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grandTotalAssetsBox.setFont(font)
        self.grandTotalAssetsBox.setReadOnly(True)
        self.grandTotalAssetsBox.setObjectName("grandTotalAssetsBox")
        self.editExpense_2 = QtWidgets.QGroupBox(self.assetsTab)
        self.editExpense_2.setGeometry(QtCore.QRect(580, 10, 391, 361))
        self.editExpense_2.setObjectName("editExpense_2")
        self.dateLabel_2 = QtWidgets.QLabel(self.editExpense_2)
        self.dateLabel_2.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.dateLabel_2.setObjectName("dateLabel_2")
        self.descriptionLabel_2 = QtWidgets.QLabel(self.editExpense_2)
        self.descriptionLabel_2.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.descriptionLabel_2.setObjectName("descriptionLabel_2")
        self.valueLabel = QtWidgets.QLabel(self.editExpense_2)
        self.valueLabel.setGeometry(QtCore.QRect(10, 290, 61, 16))
        self.valueLabel.setObjectName("valueLabel")
        self.assetValueBox = QtWidgets.QDoubleSpinBox(self.editExpense_2)
        self.assetValueBox.setGeometry(QtCore.QRect(90, 290, 111, 22))
        self.assetValueBox.setMaximum(999999999.99)
        self.assetValueBox.setSingleStep(0.01)
        self.assetValueBox.setObjectName("assetValueBox")
        self.assetDescriptionBox = QtWidgets.QLineEdit(self.editExpense_2)
        self.assetDescriptionBox.setGeometry(QtCore.QRect(90, 260, 281, 20))
        self.assetDescriptionBox.setObjectName("assetDescriptionBox")
        self.addAsset = QtWidgets.QPushButton(self.editExpense_2)
        self.addAsset.setGeometry(QtCore.QRect(10, 320, 181, 31))
        self.addAsset.setObjectName("addAsset")
        self.removeAssets = QtWidgets.QPushButton(self.editExpense_2)
        self.removeAssets.setGeometry(QtCore.QRect(200, 320, 181, 31))
        self.removeAssets.setObjectName("removeAssets")
        self.label_20 = QtWidgets.QLabel(self.editExpense_2)
        self.label_20.setGeometry(QtCore.QRect(70, 290, 16, 20))
        self.label_20.setObjectName("label_20")
        self.assetCalendar = QtWidgets.QCalendarWidget(self.editExpense_2)
        self.assetCalendar.setGeometry(QtCore.QRect(50, 30, 321, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.assetCalendar.setFont(font)
        self.assetCalendar.setGridVisible(False)
        self.assetCalendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.assetCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.assetCalendar.setObjectName("assetCalendar")
        self.tabWidget.addTab(self.assetsTab, "")
        self.budgetTab = QtWidgets.QWidget()
        self.budgetTab.setObjectName("budgetTab")
        self.allotmentsTable = QtWidgets.QTableWidget(self.budgetTab)
        self.allotmentsTable.setGeometry(QtCore.QRect(10, 10, 561, 611))
        self.allotmentsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allotmentsTable.setDragEnabled(True)
        self.allotmentsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.allotmentsTable.setObjectName("allotmentsTable")
        self.allotmentsTable.setColumnCount(5)
        self.allotmentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.allotmentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.allotmentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.allotmentsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.allotmentsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.allotmentsTable.setHorizontalHeaderItem(4, item)
        self.allotmentsTable.verticalHeader().setVisible(False)
        self.editAllotment = QtWidgets.QGroupBox(self.budgetTab)
        self.editAllotment.setGeometry(QtCore.QRect(580, 10, 391, 211))
        self.editAllotment.setObjectName("editAllotment")
        self.priorityLabel = QtWidgets.QLabel(self.editAllotment)
        self.priorityLabel.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.priorityLabel.setObjectName("priorityLabel")
        self.categoryLabel = QtWidgets.QLabel(self.editAllotment)
        self.categoryLabel.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.categoryLabel.setObjectName("categoryLabel")
        self.allotmentAmountLabel = QtWidgets.QLabel(self.editAllotment)
        self.allotmentAmountLabel.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.allotmentAmountLabel.setObjectName("allotmentAmountLabel")
        self.allotmentAmountBox = QtWidgets.QDoubleSpinBox(self.editAllotment)
        self.allotmentAmountBox.setGeometry(QtCore.QRect(90, 130, 121, 22))
        self.allotmentAmountBox.setMaximum(999999999.99)
        self.allotmentAmountBox.setSingleStep(0.01)
        self.allotmentAmountBox.setObjectName("allotmentAmountBox")
        self.categoryBox = QtWidgets.QLineEdit(self.editAllotment)
        self.categoryBox.setGeometry(QtCore.QRect(90, 30, 231, 20))
        self.categoryBox.setObjectName("categoryBox")
        self.addAllotment = QtWidgets.QPushButton(self.editAllotment)
        self.addAllotment.setGeometry(QtCore.QRect(10, 170, 181, 31))
        self.addAllotment.setObjectName("addAllotment")
        self.removeAllotment = QtWidgets.QPushButton(self.editAllotment)
        self.removeAllotment.setGeometry(QtCore.QRect(200, 170, 181, 31))
        self.removeAllotment.setObjectName("removeAllotment")
        self.flatLabel = QtWidgets.QLabel(self.editAllotment)
        self.flatLabel.setGeometry(QtCore.QRect(70, 130, 16, 20))
        self.flatLabel.setObjectName("flatLabel")
        self.priorityBox = QtWidgets.QSpinBox(self.editAllotment)
        self.priorityBox.setGeometry(QtCore.QRect(90, 60, 121, 22))
        self.priorityBox.setMinimum(1)
        self.priorityBox.setMaximum(999)
        self.priorityBox.setObjectName("priorityBox")
        self.percentageLabel = QtWidgets.QLabel(self.editAllotment)
        self.percentageLabel.setEnabled(True)
        self.percentageLabel.setGeometry(QtCore.QRect(216, 130, 21, 20))
        self.percentageLabel.setObjectName("percentageLabel")
        self.flatOrPercentage = QtWidgets.QComboBox(self.editAllotment)
        self.flatOrPercentage.setGeometry(QtCore.QRect(90, 100, 121, 22))
        self.flatOrPercentage.setObjectName("flatOrPercentage")
        self.flatOrPercentage.addItem("")
        self.flatOrPercentage.addItem("")
        self.tabWidget.addTab(self.budgetTab, "")
        self.incomeBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.incomeBox.setGeometry(QtCore.QRect(580, 50, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.incomeBox.setFont(font)
        self.incomeBox.setMaximum(999999999.99)
        self.incomeBox.setSingleStep(0.01)
        self.incomeBox.setObjectName("incomeBox")
        self.dollarLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.dollarLabel_2.setGeometry(QtCore.QRect(530, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.dollarLabel_2.setFont(font)
        self.dollarLabel_2.setObjectName("dollarLabel_2")
        self.incomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.incomeLabel.setGeometry(QtCore.QRect(580, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.incomeLabel.setFont(font)
        self.incomeLabel.setObjectName("incomeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.actionSwitch_account = QtWidgets.QAction(MainWindow)
        self.actionSwitch_account.setObjectName("actionSwitch_account")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menubar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dollarLabel.setText(_translate("MainWindow", "$"))
        item = self.expensesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.expensesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.expensesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Transfer"))
        item = self.expensesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        self.editExpense.setTitle(_translate("MainWindow", "Add / Remove Expenses"))
        self.transferLabel.setText(_translate("MainWindow", "Transfer:"))
        self.dateLabel.setText(_translate("MainWindow", "Date:"))
        self.descriptionLabel.setText(_translate("MainWindow", "Description:"))
        self.amountLabel.setText(_translate("MainWindow", "Amount:"))
        self.expenseDescriptionBox.setPlaceholderText(_translate("MainWindow", "Description of payment"))
        self.expenseTransferBox.setPlaceholderText(_translate("MainWindow", "Party that is receiving the money"))
        self.addExpense.setText(_translate("MainWindow", "Add"))
        self.removeExpenses.setText(_translate("MainWindow", "Remove"))
        self.label_13.setText(_translate("MainWindow", "$"))
        self.requiredPayments.setTitle(_translate("MainWindow", "Required Monthly Payments"))
        self.totalLabel.setText(_translate("MainWindow", "Total:"))
        self.totalBox.setText(_translate("MainWindow", "0.00"))
        self.stateSelect.setItemText(0, _translate("MainWindow", "Select a state..."))
        self.stateSelect.setItemText(1, _translate("MainWindow", "Alabama"))
        self.stateSelect.setItemText(2, _translate("MainWindow", "Alaska"))
        self.stateSelect.setItemText(3, _translate("MainWindow", "Arizona"))
        self.stateSelect.setItemText(4, _translate("MainWindow", "Arkansas"))
        self.stateSelect.setItemText(5, _translate("MainWindow", "California"))
        self.stateSelect.setItemText(6, _translate("MainWindow", "Colorado"))
        self.stateSelect.setItemText(7, _translate("MainWindow", "Connecticut"))
        self.stateSelect.setItemText(8, _translate("MainWindow", "Delaware"))
        self.stateSelect.setItemText(9, _translate("MainWindow", "Florida"))
        self.stateSelect.setItemText(10, _translate("MainWindow", "Georgia"))
        self.stateSelect.setItemText(11, _translate("MainWindow", "Hawaii"))
        self.stateSelect.setItemText(12, _translate("MainWindow", "Idaho"))
        self.stateSelect.setItemText(13, _translate("MainWindow", "Illinois"))
        self.stateSelect.setItemText(14, _translate("MainWindow", "Indiana"))
        self.stateSelect.setItemText(15, _translate("MainWindow", "Iowa"))
        self.stateSelect.setItemText(16, _translate("MainWindow", "Kansas"))
        self.stateSelect.setItemText(17, _translate("MainWindow", "Kentucky"))
        self.stateSelect.setItemText(18, _translate("MainWindow", "Louisiana"))
        self.stateSelect.setItemText(19, _translate("MainWindow", "Maine"))
        self.stateSelect.setItemText(20, _translate("MainWindow", "Maryland"))
        self.stateSelect.setItemText(21, _translate("MainWindow", "Massachusetts"))
        self.stateSelect.setItemText(22, _translate("MainWindow", "Michigan"))
        self.stateSelect.setItemText(23, _translate("MainWindow", "Minnesota"))
        self.stateSelect.setItemText(24, _translate("MainWindow", "Mississippi"))
        self.stateSelect.setItemText(25, _translate("MainWindow", "Missouri"))
        self.stateSelect.setItemText(26, _translate("MainWindow", "Montana"))
        self.stateSelect.setItemText(27, _translate("MainWindow", "Nebraska"))
        self.stateSelect.setItemText(28, _translate("MainWindow", "Nevada"))
        self.stateSelect.setItemText(29, _translate("MainWindow", "New Hampshire"))
        self.stateSelect.setItemText(30, _translate("MainWindow", "New Jersey"))
        self.stateSelect.setItemText(31, _translate("MainWindow", "New Mexico"))
        self.stateSelect.setItemText(32, _translate("MainWindow", "New York"))
        self.stateSelect.setItemText(33, _translate("MainWindow", "North Carolina"))
        self.stateSelect.setItemText(34, _translate("MainWindow", "North Dakota"))
        self.stateSelect.setItemText(35, _translate("MainWindow", "Ohio"))
        self.stateSelect.setItemText(36, _translate("MainWindow", "Oklahoma"))
        self.stateSelect.setItemText(37, _translate("MainWindow", "Oregon"))
        self.stateSelect.setItemText(38, _translate("MainWindow", "Pennsylvania"))
        self.stateSelect.setItemText(39, _translate("MainWindow", "Rhode Island"))
        self.stateSelect.setItemText(40, _translate("MainWindow", "South Carolina"))
        self.stateSelect.setItemText(41, _translate("MainWindow", "South Dakota"))
        self.stateSelect.setItemText(42, _translate("MainWindow", "Tennessee"))
        self.stateSelect.setItemText(43, _translate("MainWindow", "Texas"))
        self.stateSelect.setItemText(44, _translate("MainWindow", "Utah"))
        self.stateSelect.setItemText(45, _translate("MainWindow", "Vermont"))
        self.stateSelect.setItemText(46, _translate("MainWindow", "Virginia"))
        self.stateSelect.setItemText(47, _translate("MainWindow", "Washington"))
        self.stateSelect.setItemText(48, _translate("MainWindow", "West Virginia"))
        self.stateSelect.setItemText(49, _translate("MainWindow", "Wisconsin"))
        self.stateSelect.setItemText(50, _translate("MainWindow", "Wyoming"))
        self.label_9.setText(_translate("MainWindow", "$"))
        self.label_12.setText(_translate("MainWindow", "$"))
        self.miscLabel.setText(_translate("MainWindow", "Misc:"))
        self.label_8.setText(_translate("MainWindow", "$"))
        self.label_7.setText(_translate("MainWindow", "$"))
        self.label_10.setText(_translate("MainWindow", "$"))
        self.costOfLivingLabel.setText(_translate("MainWindow", "Costs of living in state:"))
        self.utilitiesLabel.setText(_translate("MainWindow", "Utilities:"))
        self.transportationLabel.setText(_translate("MainWindow", "Transportation:"))
        self.housingLabel.setText(_translate("MainWindow", "Housing:"))
        self.label_11.setText(_translate("MainWindow", "$"))
        self.groceriesLabel.setText(_translate("MainWindow", "Groceries:"))
        self.label_14.setText(_translate("MainWindow", "/ month"))
        self.label_15.setText(_translate("MainWindow", "/ month"))
        self.label_16.setText(_translate("MainWindow", "/ month"))
        self.label_17.setText(_translate("MainWindow", "/ month"))
        self.label_18.setText(_translate("MainWindow", "/ month"))
        self.label_19.setText(_translate("MainWindow", "/ month"))
        self.grandTotalExpensesBox.setText(_translate("MainWindow", "0.00"))
        self.grandTotalLabel.setText(_translate("MainWindow", "Grand Total: $"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expensesTab), _translate("MainWindow", "Expenses"))
        item = self.assetsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.assetsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.assetsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.grandTotalLabel_2.setText(_translate("MainWindow", "Grand Total: $"))
        self.grandTotalAssetsBox.setText(_translate("MainWindow", "0.00"))
        self.editExpense_2.setTitle(_translate("MainWindow", "Add / Remove Assets"))
        self.dateLabel_2.setText(_translate("MainWindow", "Date:"))
        self.descriptionLabel_2.setText(_translate("MainWindow", "Description:"))
        self.valueLabel.setText(_translate("MainWindow", "Value"))
        self.assetDescriptionBox.setPlaceholderText(_translate("MainWindow", "Description of asset"))
        self.addAsset.setText(_translate("MainWindow", "Add"))
        self.removeAssets.setText(_translate("MainWindow", "Remove"))
        self.label_20.setText(_translate("MainWindow", "$"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assetsTab), _translate("MainWindow", "Assets"))
        item = self.allotmentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.allotmentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Priority"))
        item = self.allotmentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.allotmentsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Result"))
        item = self.allotmentsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Remainder"))
        self.editAllotment.setTitle(_translate("MainWindow", "Add / Remove Allotments"))
        self.priorityLabel.setText(_translate("MainWindow", "Priority:"))
        self.categoryLabel.setText(_translate("MainWindow", "Category:"))
        self.allotmentAmountLabel.setText(_translate("MainWindow", "Amount:"))
        self.categoryBox.setPlaceholderText(_translate("MainWindow", "Allocate money to..."))
        self.addAllotment.setText(_translate("MainWindow", "Add"))
        self.removeAllotment.setText(_translate("MainWindow", "Remove"))
        self.flatLabel.setText(_translate("MainWindow", "$"))
        self.percentageLabel.setText(_translate("MainWindow", "%"))
        self.flatOrPercentage.setItemText(0, _translate("MainWindow", "Flat"))
        self.flatOrPercentage.setItemText(1, _translate("MainWindow", "Percentage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.budgetTab), _translate("MainWindow", "Budget"))
        self.dollarLabel_2.setText(_translate("MainWindow", "$"))
        self.incomeLabel.setText(_translate("MainWindow", "Income:"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionSwitch_account.setText(_translate("MainWindow", "Switch account..."))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
