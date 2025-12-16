from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.person_detail_ui import Ui_Dialog
from viewmodel.person_detail_vm import PersonDetailViewModel


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









# from PyQt5.QtWidgets import QDialog,QLineEdit, QPushButton, QCheckBox, QMessageBox
# from person_detail_ui import Ui_Dialog

# from database import SessionLocal
# from models import Person


# class PersonDetailView(QDialog):
#     def __init__(self):
#         super().__init__()

#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)

#         # دیکشنری داده‌ها
#         self.data = {
#             'is_active': False
#         }

#         # گرفتن ویجت‌ها
#         self.code_input = self.ui.lineEdit
#         self.name_input = self.ui.lineEdit_2
#         self.family_input = self.ui.lineEdit_3

#         self.active_checkbox = self.ui.activeCheckBox

#         self.create_btn = self.ui.pushButton_5  # OK
#         self.cancel_btn = self.ui.pushButton_6  # Cancel

#         self._connect_signals()

#     def _connect_signals(self):
#         self.code_input.textChanged.connect(
#             lambda v: self.set_field('code', v)
#         )
#         self.name_input.textChanged.connect(
#             lambda v: self.set_field('name', v)
#         )
#         self.family_input.textChanged.connect(
#             lambda v: self.set_field('family', v)
#         )

#         self.active_checkbox.stateChanged.connect(
#             lambda v: self.set_field('is_active', bool(v))
#         )

#         self.create_btn.clicked.connect(self.create_object)
#         self.cancel_btn.clicked.connect(self.reject)

#     def set_field(self, key, value):
#         self.data[key] = value

#     def create_object(self):
#         # چاپ در کنسول
#         print("Saved data:")
#         print(self.data)

#         # ذخیره در دیتابیس
#         session = SessionLocal()

#         person = Person(
#             code=self.data.get('code'),
#             name=self.data.get('name'),
#             family=self.data.get('family'),
#             is_active=self.data.get('is_active')
#         )

#         session.add(person)
#         session.commit()
#         session.close() 

#         QMessageBox.information(self, "Success", "Person saved successfully!")
        

#         self.accept()
    
#     def load_person(self, person_id):
#         session = SessionLocal()
#         person = session.query(Person).filter_by(id=person_id).first()
#         session.close()

#         if not person:
#             QMessageBox.warning(self, "Error", "Person not found!")
#             return

#         # پر کردن فرم با داده‌ها
#         self.code_input.setText(person.code or "")
#         self.name_input.setText(person.name or "")
#         self.family_input.setText(person.family or "")
#         self.active_checkbox.setChecked(person.is_active or False)

