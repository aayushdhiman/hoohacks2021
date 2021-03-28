import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from window import Ui_MainWindow

import coli

import qdarkstyle


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Dropdowns, number / text inputs, and buttons
        self.stateSelect.currentTextChanged.connect(self.calculate_required_monthly_payments)

        self.groceriesBox.valueChanged.connect(self.update_total_payments_box)
        self.housingBox.valueChanged.connect(self.update_total_payments_box)
        self.utilitiesBox.valueChanged.connect(self.update_total_payments_box)
        self.transportationBox.valueChanged.connect(self.update_total_payments_box)
        self.miscBox.valueChanged.connect(self.update_total_payments_box)

        self.addExpense.clicked.connect(self.add_expense)
        self.removeExpenses.clicked.connect(self.remove_expenses)

        self.addAsset.clicked.connect(self.add_asset)
        self.removeAssets.clicked.connect(self.remove_assets)

        self.incomeBox.valueChanged.connect(self.update_balance)

        self.percentageLabel.setHidden(True)
        self.flatOrPercentage.currentTextChanged.connect(self.update_flat_percentage)

        self.addAllotment.clicked.connect(self.add_allotment)
        self.removeAllotment.clicked.connect(self.remove_allotments)

        # Variables
        self.expenses = []
        self.total_expenses = 0
        self.grand_total_expenses = 0

        self.assets = []
        self.grand_total_assets = 0

        self.allotments = []

        self.income = 0
        self.balance = 0

        # Themes
        self.light_theme = self.styleSheet()
        self.dark_theme = qdarkstyle.load_stylesheet()

        self.actionLight.triggered.connect(self.change_to_light_theme)
        self.actionDark.triggered.connect(self.change_to_dark_theme)

        self.change_to_light_theme()

        self.setWindowTitle("Phynance Manager")
        self.show()

    def calculate_required_monthly_payments(self, state):
        """Calculates the required monthly payments for a state.

        Args:
            state (str): The state selected in the dropdown.
        """
        if state != "Select a state...":
            grocery_cost = round(coli.get_state_cost(state, "grocery") / 12, 2)
            housing_cost = round(coli.get_state_cost(state, "housing") / 12, 2)
            utilities_cost = round(coli.get_state_cost(state, "utilities") / 12, 2)
            transportation_cost = round(coli.get_state_cost(state, "transportation") / 12, 2)
            misc_cost = round(coli.get_state_cost(state, "misc") / 12, 2)

            self.groceriesBox.setValue(grocery_cost)
            self.housingBox.setValue(housing_cost)
            self.utilitiesBox.setValue(utilities_cost)
            self.transportationBox.setValue(transportation_cost)
            self.miscBox.setValue(misc_cost)

            self.update_total_payments_box()
            self.update_expenses()

    def update_total_payments_box(self):
        """Sums up the costs in each category and updates the total monthly payments box."""
        grocery_cost = self.groceriesBox.value()
        housing_cost = self.housingBox.value()
        utilities_cost = self.utilitiesBox.value()
        transportation_cost = self.transportationBox.value()
        misc_cost = self.miscBox.value()
        self.total_expenses = round(grocery_cost + housing_cost + utilities_cost + transportation_cost + misc_cost, 2)

        self.totalBox.setText("{:.2f}".format(self.total_expenses))

    def add_expense(self):
        """Add an expense given the date, description, recipient, and amount."""
        self.expenses.append(
            {
                "date": self.expenseCalendar.selectedDate().toString("M/d/yyyy"),
                "description": self.expenseDescriptionBox.text(),
                "transfer": self.expenseTransferBox.text(),
                "amount": self.expenseAmountBox.value()
            }
        )
        self.update_expenses()

    def remove_expenses(self):
        """Remove a selection of expenses from the list."""
        selections = self.expensesTable.selectedItems()
        rows_to_delete = reversed(
            sorted(list({selection.row() for selection in selections}))
        )

        for row in rows_to_delete:
            del self.expenses[row]

        self.update_expenses()

    def update_expenses(self):
        """Update the expenses table to correctly show the expenses in the order they were added."""
        self.expensesTable.clearContents()
        self.expensesTable.setRowCount(len(self.expenses))

        expense_costs = []
        for index, expense in enumerate(self.expenses):
            self.expensesTable.setItem(index, 0, QTableWidgetItem(expense["date"]))
            self.expensesTable.setItem(index, 1, QTableWidgetItem(expense["description"]))
            self.expensesTable.setItem(index, 2, QTableWidgetItem(expense["transfer"]))
            self.expensesTable.setItem(index, 3, QTableWidgetItem("${:.2f}".format(expense['amount'])))

            expense_costs.append(expense["amount"])

        self.grand_total_expenses = round(sum(expense_costs) + self.total_expenses, 2)
        self.grandTotalExpensesBox.setText("{:.2f}".format(self.grand_total_expenses))

        self.update_balance()

    def add_asset(self):
        """Add an asset given the date, description, and value."""
        self.assets.append(
            {
                "date": self.assetCalendar.selectedDate().toString("M/d/yyyy"),
                "description": self.assetDescriptionBox.text(),
                "value": self.assetValueBox.value()
            }
        )
        self.update_assets()

    def remove_assets(self):
        """Remove a selection of assets from the list."""
        selections = self.assetsTable.selectedItems()
        rows_to_delete = reversed(
            sorted(list({selection.row() for selection in selections}))
        )

        for row in rows_to_delete:
            del self.assets[row]

        self.update_assets()

    def update_assets(self):
        """Update the assets table to correctly show the assets in the order they were added."""
        self.assetsTable.clearContents()
        self.assetsTable.setRowCount(len(self.assets))

        asset_values = []
        for index, asset in enumerate(self.assets):
            self.assetsTable.setItem(index, 0, QTableWidgetItem(asset["date"]))
            self.assetsTable.setItem(index, 1, QTableWidgetItem(asset["description"]))
            self.assetsTable.setItem(index, 2, QTableWidgetItem("${:.2f}".format(asset['value'])))

            asset_values.append(asset["value"])

        self.grand_total_assets = round(sum(asset_values), 2)
        self.grandTotalAssetsBox.setText("{:.2f}".format(self.grand_total_assets))

        self.update_balance()

    def update_balance(self):
        """Update the seven-segment display for the balance."""
        self.income = self.incomeBox.value()
        self.balance = round(self.income + self.grand_total_assets - self.grand_total_expenses, 2)
        self.balanceDisplay.display(self.balance)

        self.update_allotments()

    def update_flat_percentage(self, selection):
        """Hide the dollar sign / percent label depending on the selection.

        Args:
            selection (str): Either "Flat" or "Percentage".
        """
        self.flatLabel.setHidden(selection == "Percentage")
        self.percentageLabel.setHidden(selection == "Flat")

    def add_allotment(self):
        """Add an allotment given the category, priority, amount, and flat / percentage."""
        self.allotments.append(
            {
                "category": self.categoryBox.text(),
                "priority": self.priorityBox.value(),
                "amount": self.allotmentAmountBox.value(),
                "fp": self.flatOrPercentage.currentText(),
                "result": "",
                "remainder": ""
            }
        )
        self.update_allotments()

    def remove_allotments(self):
        """Remove a selection of allotments from the list."""
        selections = self.allotmentsTable.selectedItems()
        rows_to_delete = reversed(
            sorted(list({selection.row() for selection in selections}))
        )

        for row in rows_to_delete:
            del self.allotments[row]

        self.update_allotments()

    def update_allotments(self):
        """Update the allotments table to correctly show the allotments in priority order. 1 is the highest priority."""
        self.allotmentsTable.clearContents()
        self.allotmentsTable.setRowCount(len(self.allotments))

        self.amount_left = self.balance

        self.allotments = sorted(self.allotments, key=lambda k: k["priority"])

        for allotment in self.allotments:
            if allotment["fp"] == "Flat":
                allotment["result"] = allotment["amount"]
                self.amount_left -= allotment["amount"]
            else:
                deduction = round(self.amount_left * (allotment["amount"] / 100), 2)
                allotment["result"] = deduction
                self.amount_left -= deduction
            self.amount_left = round(self.amount_left, 2)
            allotment["remainder"] = self.amount_left

        for index, allotment in enumerate(self.allotments):
            self.allotmentsTable.setItem(index, 0, QTableWidgetItem(allotment["category"]))
            self.allotmentsTable.setItem(index, 1, QTableWidgetItem(str(allotment["priority"])))
            if allotment["fp"] == "Flat":
                self.allotmentsTable.setItem(index, 2, QTableWidgetItem("${:.2f}".format(allotment["amount"])))
            else:
                self.allotmentsTable.setItem(index, 2, QTableWidgetItem("{:.2f}%".format(allotment["amount"])))
            self.allotmentsTable.setItem(index, 3, QTableWidgetItem("${:.2f}".format(allotment["result"])))
            self.allotmentsTable.setItem(index, 4, QTableWidgetItem("${:.2f}".format(allotment["remainder"])))

    def change_to_light_theme(self):
        """Change to the default theme."""
        self.setStyleSheet(self.light_theme)

    def change_to_dark_theme(self):
        """Change to qdarkstyle's dark theme."""
        self.setStyleSheet(self.dark_theme)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    sys.exit(app.exec_())
