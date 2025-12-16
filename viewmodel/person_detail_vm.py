from PyQt5.QtCore import QObject, pyqtSignal
from database.database import SessionLocal
from models.models import Person


class PersonDetailViewModel(QObject):
    saved = pyqtSignal()
    error = pyqtSignal(str)
    loaded = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.person_id = None 
        self.code = ""
        self.name = ""
        self.family = ""
        self.is_active = False

    def set_code(self, value):
        self.code = value

    def set_name(self, value):
        self.name = value

    def set_family(self, value):
        self.family = value

    def set_is_active(self, value):
        self.is_active = value


    def save(self):
        try:
            session = SessionLocal()
            
            if self.person_id: 
                person = session.query(Person).filter_by(id=self.person_id).first()
                if not person:
                    self.error.emit("Person not found for update")
                    return
                person.code = self.code
                person.name = self.name
                person.family = self.family
                person.is_active = self.is_active
            else:  
                person = Person(
                    code=self.code,
                    name=self.name,
                    family=self.family,
                    is_active=self.is_active
                )
                session.add(person)

            session.commit()
            session.close()
            self.saved.emit()

        except Exception as e:
            self.error.emit(str(e))

    def load_person(self, person_id):
        try:
            session = SessionLocal()
            person = session.query(Person).filter_by(id=person_id).first()
            session.close()

            if not person:
                self.error.emit("Person not found")
                return

            # 👈 ذخیره id شخص
            self.person_id = person.id

            # آپدیت state
            self.code = person.code or ""
            self.name = person.name or ""
            self.family = person.family or ""
            self.is_active = bool(person.is_active)

            # اطلاع به View
            self.loaded.emit({
                "code": self.code,
                "name": self.name,
                "family": self.family,
                "is_active": self.is_active
            })

        except Exception as e:
            self.error.emit(str(e))
