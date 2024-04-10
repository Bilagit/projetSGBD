from PySide6.QtCore import Qt
from ui_respclasse import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Myrespclasse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Resposta Classe")
        
        self.icon_name_widget.setHidden(True)
        
        self.compte_1.clicked.connect(self.switch_to_page_compte_rendu)
        self.compte_2.clicked.connect(self.switch_to_page_compte_rendu)
        
        self.verification_1.clicked.connect(self.switch_to_page_verification)
        self.verification_2.clicked.connect(self.switch_to_page_verification)
        
        self.fiche_1.clicked.connect(self.switch_to_page_evaluation)
        self.fiche_2.clicked.connect(self.switch_to_page_evaluation)
        
        self.suivi_1.clicked.connect(self.switch_to_page_suivi)
        self.suivi_2.clicked.connect(self.switch_to_page_suivi)
        
        self.transmission_1.clicked.connect(self.switch_to_page_transmission)
        self.transmission_2.clicked.connect(self.switch_to_page_transmission)
        
    def switch_to_page_compte_rendu(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_page_verification(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_to_page_evaluation(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_page_suivi(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_page_transmission(self):
        self.stackedWidget.setCurrentIndex(4)
    
