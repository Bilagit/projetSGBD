# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstclasse.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_FirstClasse(object):
    def setupUi(self, FirstClasse):
        if not FirstClasse.objectName():
            FirstClasse.setObjectName(u"FirstClasse")
        FirstClasse.resize(592, 439)
        FirstClasse.setStyleSheet(u"\n"
"background-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(FirstClasse)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setGeometry(QRect(0, 10, 51, 401))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"text-align:center;\n"
"color:white;\n"
"height:30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"}")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 41, 40))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/images/profil.png"))
        self.label.setScaledContents(True)
        self.sign2 = QPushButton(self.icon_only_widget)
        self.sign2.setObjectName(u"sign2")
        self.sign2.setGeometry(QRect(0, 380, 41, 21))
        icon = QIcon()
        icon.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sign2.setIcon(icon)
        self.sign2.setCheckable(True)
        self.sign2.setAutoExclusive(True)
        self.widget = QWidget(self.icon_only_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 60, 51, 221))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboard1 = QPushButton(self.widget)
        self.dashboard1.setObjectName(u"dashboard1")
        icon1 = QIcon()
        icon1.addFile(u":/images/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard1.setIcon(icon1)
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard1)

        self.profil1 = QPushButton(self.widget)
        self.profil1.setObjectName(u"profil1")
        icon2 = QIcon()
        icon2.addFile(u":/images/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profil1.setIcon(icon2)
        self.profil1.setCheckable(True)
        self.profil1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profil1)

        self.cours1 = QPushButton(self.widget)
        self.cours1.setObjectName(u"cours1")
        icon3 = QIcon()
        icon3.addFile(u":/images/task-query-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cours1.setIcon(icon3)
        self.cours1.setCheckable(True)
        self.cours1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cours1)

        self.syllabus1 = QPushButton(self.widget)
        self.syllabus1.setObjectName(u"syllabus1")
        icon4 = QIcon()
        icon4.addFile(u":/images/syllabus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.syllabus1.setIcon(icon4)
        self.syllabus1.setCheckable(True)
        self.syllabus1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.syllabus1)

        self.avis1 = QPushButton(self.widget)
        self.avis1.setObjectName(u"avis1")
        icon5 = QIcon()
        icon5.addFile(u":/images/avis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.avis1.setIcon(icon5)
        self.avis1.setCheckable(True)
        self.avis1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.avis1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setGeometry(QRect(60, 10, 151, 401))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.icon_name_widget.setFont(font)
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"text-align:left;\n"
"color:white;\n"
"height:30px;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/image.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboard2 = QPushButton(self.icon_name_widget)
        self.dashboard2.setObjectName(u"dashboard2")
        self.dashboard2.setStyleSheet(u"")
        self.dashboard2.setIcon(icon1)
        self.dashboard2.setIconSize(QSize(15, 15))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setChecked(False)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)

        self.profil2 = QPushButton(self.icon_name_widget)
        self.profil2.setObjectName(u"profil2")
        self.profil2.setIcon(icon2)
        self.profil2.setCheckable(True)
        self.profil2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profil2)

        self.cours2 = QPushButton(self.icon_name_widget)
        self.cours2.setObjectName(u"cours2")
        self.cours2.setIcon(icon3)
        self.cours2.setCheckable(True)
        self.cours2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.cours2)

        self.syllabus2 = QPushButton(self.icon_name_widget)
        self.syllabus2.setObjectName(u"syllabus2")
        self.syllabus2.setIcon(icon4)
        self.syllabus2.setCheckable(True)
        self.syllabus2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.syllabus2)

        self.avis2 = QPushButton(self.icon_name_widget)
        self.avis2.setObjectName(u"avis2")
        self.avis2.setIcon(icon5)
        self.avis2.setCheckable(True)
        self.avis2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.avis2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.sign1 = QPushButton(self.icon_name_widget)
        self.sign1.setObjectName(u"sign1")
        self.sign1.setStyleSheet(u"QWidget {\n"
"	rgb(0, 0, 0)\n"
"}")
        self.sign1.setIcon(icon)
        self.sign1.setCheckable(True)
        self.sign1.setChecked(False)
        self.sign1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.sign1)

        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(215, 10, 371, 41))
        self.header_widget.setStyleSheet(u"background-color: rgb(208, 242, 255);")
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.header_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"background-color: rgb(94, 150, 255);\n"
"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(25, 25))
        self.pushButton_13.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(12, 12))
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton_14)

        self.horizontalSpacer_2 = QSpacerItem(85, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/profil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_15)

        self.mainWidjet = QWidget(self.centralwidget)
        self.mainWidjet.setObjectName(u"mainWidjet")
        self.mainWidjet.setGeometry(QRect(217, 60, 371, 351))
        self.mainWidjet.setStyleSheet(u"background-color: rgb(201, 246, 255);")
        FirstClasse.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FirstClasse)
        self.statusbar.setObjectName(u"statusbar")
        FirstClasse.setStatusBar(self.statusbar)

        self.retranslateUi(FirstClasse)
        self.pushButton_13.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_13.toggled.connect(self.icon_name_widget.setVisible)
        self.avis1.toggled.connect(self.avis2.setChecked)
        self.syllabus1.toggled.connect(self.syllabus2.setChecked)
        self.cours1.toggled.connect(self.cours2.setChecked)
        self.profil1.toggled.connect(self.profil2.setChecked)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.profil2.toggled.connect(self.profil1.setChecked)
        self.cours2.toggled.connect(self.cours1.setChecked)
        self.syllabus2.toggled.connect(self.syllabus1.setChecked)
        self.avis2.toggled.connect(self.avis1.setChecked)
        self.sign1.toggled.connect(FirstClasse.close)
        self.sign2.toggled.connect(FirstClasse.close)

        QMetaObject.connectSlotsByName(FirstClasse)
    # setupUi

    def retranslateUi(self, FirstClasse):
        FirstClasse.setWindowTitle(QCoreApplication.translate("FirstClasse", u"FirstClasse", None))
        self.label.setText("")
        self.sign2.setText("")
        self.profil1.setText("")
        self.cours1.setText("")
        self.syllabus1.setText("")
        self.avis1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("FirstClasse", u"Responsable Classe", None))
        self.dashboard2.setText(QCoreApplication.translate("FirstClasse", u"Dashboard", None))
        self.profil2.setText(QCoreApplication.translate("FirstClasse", u"Profil", None))
        self.cours2.setText(QCoreApplication.translate("FirstClasse", u"Constater Effectivite Cours", None))
        self.syllabus2.setText(QCoreApplication.translate("FirstClasse", u"Syllabus", None))
        self.avis2.setText(QCoreApplication.translate("FirstClasse", u"Avis Etudiant", None))
        self.sign1.setText(QCoreApplication.translate("FirstClasse", u"Deconnexion", None))
        self.pushButton_13.setText("")
        self.lineEdit.setText(QCoreApplication.translate("FirstClasse", u"Search", None))
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
    # retranslateUi

