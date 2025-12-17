from PyQt5.QtCore import QObject, pyqtSignal
from database.database import SessionLocal
from person.detail.person_models import PersonModel


class PersonDetailViewModel(QObject):
    saved = pyqtSignal()
    error = pyqtSignal(str)
    loaded = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.model = PersonModel()

    def set_code(self, v):
        self.model.code = v

    def set_name(self, v):
        self.model.name = v

    def set_family(self, v):
        self.model.family = v

    def set_is_active(self, v):
        self.model.is_active = v

    def load_person(self, person_id):
        try:
            db = SessionLocal()
            self.model.id = person_id
            data = self.model.load(db)
            db.close()
            self.loaded.emit(data)
        except Exception as e:
            self.error.emit(str(e))

    def save(self):
        try:
            db = SessionLocal()
            self.model.save(db)
            db.close()
            self.saved.emit()
        except Exception as e:
            self.error.emit(str(e))
