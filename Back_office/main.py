from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from ChefDepart import MyChefDepart

app = QApplication(sys.argv)

window = MyChefDepart()

window.show()
app.exec()

