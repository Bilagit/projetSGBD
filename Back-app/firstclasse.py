from ui_firstclasse import Ui_FirstClasse
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyFirstClasse(QMainWindow, Ui_FirstClasse):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Menu Edudiant")

        self.icon_only_widget.setHidden(True)

        self.dashboard1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardPage)

        self.profil1.clicked.connect(self.switch_to_profilPage)
        self.profil2.clicked.connect(self.switch_to_profilPage)

        self.cours1.clicked.connect(self.switch_to_coursPage)
        self.cours2.clicked.connect(self.switch_to_coursPage)

        self.syllabus1.clicked.connect(self.switch_to_syllabusPage)
        self.syllabus2.clicked.connect(self.switch_to_syllabusPage)

        self.avis1.clicked.connect(self.switch_to_avisPage)
        self.avis2.clicked.connect(self.switch_to_avisPage)

    def switch_to_dashboardPage(self):
        self.widget.setCurrentIndex(0)    

    def switch_to_profilPage(self):
        self.widget.setCurrentIndex(1) 

    def switch_to_coursPage(self):
        self.widget.setCurrentIndex(2)     


    def switch_to_syllabusPage(self):
        self.widget.setCurrentIndex(3)    

    def switch_to_avisPage(self):
        self.widget.setCurrentIndex(4)