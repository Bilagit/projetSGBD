from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from firstclasse import MyFirstClasse

app = QApplication(sys.argv)

window = MyFirstClasse()

window.show()
app.exec()