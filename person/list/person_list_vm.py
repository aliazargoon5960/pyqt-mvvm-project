from PyQt5.QtCore import QObject, pyqtSignal
from database.database import SessionLocal
from person.list.person_list_model import PersonListModel


class PersonListViewModel(QObject):
    data_loaded = pyqtSignal(list)
    error = pyqtSignal(str)

    def load_persons(self):
        try:
            db = SessionLocal()
            data = PersonListModel.get_all(db)
            db.close()
            self.data_loaded.emit(data)
        except Exception as e:
            self.error.emit(str(e))
