from PySide6.QtCore import Qt
from ui_RP import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyRP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("RP")
        
        self.icon_name_widget.setHidden(True)
        
        self.ens_1.clicked.connect(self.switch_to_page_enseignement)
        self.ens_2.clicked.connect(self.switch_to_page_enseignement)
        
        self.eva_1.clicked.connect(self.switch_to_page_fiche)
        self.eva_2.clicked.connect(self.switch_to_page_fiche)
        
        self.men_1.clicked.connect(self.switch_to_page_mensuel)
        self.men_2.clicked.connect(self.switch_to_page_mensuel)
        
        self.cons_1.clicked.connect(self.switch_to_page_consultation)
        self.cons_2.clicked.connect(self.switch_to_page_consultation)
        
        self.avis_1.clicked.connect(self.switch_to_page_avis)
        self.avis_2.clicked.connect(self.switch_to_page_avis)
        
        self.rap_1.clicked.connect(self.switch_to_page_rapport)
        self.rap_2.clicked.connect(self.switch_to_page_rapport)
        
    def switch_to_page_enseignement(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_page_fiche(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_to_page_mensuel(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_page_consultation(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_page_avis(self):
        self.stackedWidget.setCurrentIndex(4)
    def switch_to_page_rapport(self):
        self.stackedWidget.setCurrentIndex(5)
    
