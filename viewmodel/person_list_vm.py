from PyQt5.QtCore import QObject, pyqtSignal
from database.database import SessionLocal
from models.models import Person


class PersonListViewModel(QObject):
    data_loaded = pyqtSignal(list)
    error = pyqtSignal(str)

    def load_persons(self):
        try:
            session = SessionLocal()
            persons = session.query(Person).all()
            session.close()

            result = []
            for p in persons:
                result.append({
                    "id": p.id,
                    "code": p.code,
                    "name": p.name,
                    "family": p.family,
                    "is_active": p.is_active
                })

            self.data_loaded.emit(result)

        except Exception as e:
            self.error.emit(str(e))
