import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from window import Ui_MainWindow

import coli


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.stateSelect.currentTextChanged.connect(self.calculate_required_payments)

        self.groceriesBox.valueChanged.connect(self.update_total_payments)
        self.housingBox.valueChanged.connect(self.update_total_payments)
        self.utilitiesBox.valueChanged.connect(self.update_total_payments)
        self.transportationBox.valueChanged.connect(self.update_total_payments)
        self.miscBox.valueChanged.connect(self.update_total_payments)

        self.addButton.clicked.connect(self.add_expense)
        self.removeButton.clicked.connect(self.remove_expenses)

        self.expenses = []
        self.total_cost = 0

    def calculate_required_payments(self, state):
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

            self.update_total_payments()
            self.update_expenses()

    def update_total_payments(self):
        grocery_cost = self.groceriesBox.value()
        housing_cost = self.housingBox.value()
        utilities_cost = self.utilitiesBox.value()
        transportation_cost = self.transportationBox.value()
        misc_cost = self.miscBox.value()
        self.total_cost = round(grocery_cost + housing_cost + utilities_cost + transportation_cost + misc_cost, 2)

        self.totalBox.setText("{:.2f}".format(self.total_cost))

    def add_expense(self):
        self.expenses.append(
            {
                "date": self.calendarWidget.selectedDate().toString("M/d/yyyy"),
                "description": self.descriptionBox.text(),
                "transfer": self.transferBox.text(),
                "amount": self.amountBox.value()
            }
        )
        self.update_expenses()

    def remove_expenses(self):
        selections = self.expensesTable.selectedItems()
        rows_to_delete = reversed(
            sorted(list({selection.row() for selection in selections}))
        )

        for row in rows_to_delete:
            del self.expenses[row]

        self.update_expenses()

    def update_expenses(self):
        self.expensesTable.clearContents()
        self.expensesTable.setRowCount(len(self.expenses))

        expense_costs = []
        for index, expense in enumerate(self.expenses):
            self.expensesTable.setItem(index, 0, QTableWidgetItem(expense["date"]))
            self.expensesTable.setItem(index, 1, QTableWidgetItem(expense["description"]))
            self.expensesTable.setItem(index, 2, QTableWidgetItem(expense["transfer"]))
            self.expensesTable.setItem(index, 3, QTableWidgetItem("${:.2f}".format(expense['amount'])))

            expense_costs.append(expense["amount"])

        grand_total = round(sum(expense_costs) + self.total_cost, 2)
        self.grandTotalBox.setText("{:.2f}".format(grand_total))

if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("Phynance Manager")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
