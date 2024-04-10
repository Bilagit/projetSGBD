from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from respclasse import Myrespclasse

app = QApplication(sys.argv)

window = Myrespclasse()

window.show()
app.exec()

