from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QTableView,
    QPushButton, QMessageBox
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from person.list.person_list_vm import PersonListViewModel
from person.detail.person_detail_view import PersonDetailView


class PersonListView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons")
        self.resize(600, 400)

        self.vm = PersonListViewModel()

        self.layout = QVBoxLayout(self)

        self.table = QTableView()
        self.layout.addWidget(self.table)

        self.add_btn = QPushButton("Add Person")
        self.layout.addWidget(self.add_btn)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["ID", "Code", "Name", "Family", "Active"]
        )
        self.table.setModel(self.model)

        self._connect_ui()
        self._connect_vm()

        self.vm.load_persons()

    def _connect_ui(self):
        self.add_btn.clicked.connect(self.add_person)
        self.table.doubleClicked.connect(self.edit_person)

    def _connect_vm(self):
        self.vm.data_loaded.connect(self.fill_table)
        self.vm.error.connect(self.show_error)

    def fill_table(self, persons):
        self.model.setRowCount(0)

        for p in persons:
            row = [
                QStandardItem(str(p["id"])),
                QStandardItem(p["code"]),
                QStandardItem(p["name"]),
                QStandardItem(p["family"]),
                QStandardItem("Yes" if p["is_active"] else "No")
            ]
            self.model.appendRow(row)

    def add_person(self):
        dlg = PersonDetailView()
        if dlg.exec_():
            self.vm.load_persons()

    def edit_person(self, index):
        row = index.row()
        person_id = int(self.model.item(row, 0).text())

        dlg = PersonDetailView(person_id=person_id)
        if dlg.exec_():
            self.vm.load_persons()

    def show_error(self, msg):
        QMessageBox.critical(self, "Error", msg)
