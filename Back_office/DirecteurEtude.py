from PySide6.QtCore import Qt
from ui_DirecteurEtude import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyDirecteurEtude(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("DirecteurEtude")
        
        self.icon_name_widget.setHidden(True)
        
        self.PV_1.clicked.connect(self.switch_to_page_PV)
        self.PV_2.clicked.connect(self.switch_to_page_PV)
        
        self.SEM_1.clicked.connect(self.switch_to_page_Sem)
        self.SEM_2.clicked.connect(self.switch_to_page_Sem)
        
    def switch_to_page_PV(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_page_Sem(self):
        self.stackedWidget.setCurrentIndex(1)
   
    

