from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.person_detail_ui import Ui_Dialog
from person.detail.person_detail_vm import PersonDetailViewModel


class PersonDetailView(QDialog):
    def __init__(self, person_id=None):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.vm = PersonDetailViewModel()

        self._connect_ui()
        self._connect_vm()

        
        if person_id is not None:
            self.vm.load_person(person_id)

    def _connect_ui(self):
        self.ui.lineEdit.textChanged.connect(self.vm.set_code)
        self.ui.lineEdit_2.textChanged.connect(self.vm.set_name)
        self.ui.lineEdit_3.textChanged.connect(self.vm.set_family)
        self.ui.activeCheckBox.stateChanged.connect(
            lambda v: self.vm.set_is_active(bool(v))
        )

        self.ui.pushButton_5.clicked.connect(self.vm.save)
        self.ui.pushButton_6.clicked.connect(self.reject)

    def _connect_vm(self):
        self.vm.saved.connect(self.on_saved)
        self.vm.error.connect(self.on_error)
        self.vm.loaded.connect(self.on_loaded)  

    def on_loaded(self, data):
        self.ui.lineEdit.setText(data["code"])
        self.ui.lineEdit_2.setText(data["name"])
        self.ui.lineEdit_3.setText(data["family"])
        self.ui.activeCheckBox.setChecked(data["is_active"])

    def on_saved(self):
        QMessageBox.information(self, "Success", "Person saved successfully!")
        self.accept()

    def on_error(self, message):
        QMessageBox.critical(self, "Error", message)


