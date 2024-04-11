from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from RP import MyRP

app = QApplication(sys.argv)

window = MyRP()

window.show()
app.exec()


