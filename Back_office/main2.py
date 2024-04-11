from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from DirecteurEtude import MyDirecteurEtude

app = QApplication(sys.argv)

window = MyDirecteurEtude()

window.show()
app.exec()



