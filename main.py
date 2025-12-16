import sys
from PyQt5.QtWidgets import QApplication
from views.person_list_view import PersonListView


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dlg = PersonListView()
    dlg.exec_()

    sys.exit(app.exec_())
