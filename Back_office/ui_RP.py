# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RP.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1432, 844)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);	\n"
"}\n"
"QPushButton{\n"
"	color: white;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 00-58-39.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.ens_1 = QPushButton(self.icon_only_widget)
        self.ens_1.setObjectName(u"ens_1")
        icon = QIcon()
        icon.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-33-53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ens_1.setIcon(icon)
        self.ens_1.setIconSize(QSize(20, 20))
        self.ens_1.setCheckable(True)
        self.ens_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ens_1)

        self.eva_1 = QPushButton(self.icon_only_widget)
        self.eva_1.setObjectName(u"eva_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-34-51.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eva_1.setIcon(icon1)
        self.eva_1.setIconSize(QSize(20, 20))
        self.eva_1.setCheckable(True)
        self.eva_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.eva_1)

        self.men_1 = QPushButton(self.icon_only_widget)
        self.men_1.setObjectName(u"men_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-36-10.png", QSize(), QIcon.Normal, QIcon.Off)
        self.men_1.setIcon(icon2)
        self.men_1.setIconSize(QSize(20, 20))
        self.men_1.setCheckable(True)
        self.men_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.men_1)

        self.cons_1 = QPushButton(self.icon_only_widget)
        self.cons_1.setObjectName(u"cons_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-36-35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cons_1.setIcon(icon3)
        self.cons_1.setIconSize(QSize(20, 20))
        self.cons_1.setCheckable(True)
        self.cons_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cons_1)

        self.avis_1 = QPushButton(self.icon_only_widget)
        self.avis_1.setObjectName(u"avis_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-37-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.avis_1.setIcon(icon4)
        self.avis_1.setIconSize(QSize(20, 20))
        self.avis_1.setCheckable(True)
        self.avis_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.avis_1)

        self.rap_1 = QPushButton(self.icon_only_widget)
        self.rap_1.setObjectName(u"rap_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-37-59.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rap_1.setIcon(icon5)
        self.rap_1.setIconSize(QSize(20, 20))
        self.rap_1.setCheckable(True)
        self.rap_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.rap_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 418, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_8 = QPushButton(self.icon_only_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon6 = QIcon()
        icon6.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-45-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.pushButton_8.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);	\n"
"	color: white;\n"
"}\n"
"QPushButton{\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_4 = QLabel(self.icon_name_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 00-58-39.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.ens_2 = QPushButton(self.icon_name_widget)
        self.ens_2.setObjectName(u"ens_2")
        self.ens_2.setIcon(icon)
        self.ens_2.setIconSize(QSize(20, 20))
        self.ens_2.setCheckable(True)
        self.ens_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ens_2)

        self.eva_2 = QPushButton(self.icon_name_widget)
        self.eva_2.setObjectName(u"eva_2")
        self.eva_2.setIcon(icon1)
        self.eva_2.setIconSize(QSize(20, 20))
        self.eva_2.setCheckable(True)
        self.eva_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.eva_2)

        self.men_2 = QPushButton(self.icon_name_widget)
        self.men_2.setObjectName(u"men_2")
        self.men_2.setIcon(icon2)
        self.men_2.setIconSize(QSize(20, 20))
        self.men_2.setCheckable(True)
        self.men_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.men_2)

        self.cons_2 = QPushButton(self.icon_name_widget)
        self.cons_2.setObjectName(u"cons_2")
        self.cons_2.setIcon(icon3)
        self.cons_2.setIconSize(QSize(20, 20))
        self.cons_2.setCheckable(True)
        self.cons_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.cons_2)

        self.avis_2 = QPushButton(self.icon_name_widget)
        self.avis_2.setObjectName(u"avis_2")
        self.avis_2.setIcon(icon4)
        self.avis_2.setIconSize(QSize(20, 20))
        self.avis_2.setCheckable(True)
        self.avis_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.avis_2)

        self.rap_2 = QPushButton(self.icon_name_widget)
        self.rap_2.setObjectName(u"rap_2")
        self.rap_2.setIcon(icon5)
        self.rap_2.setIconSize(QSize(20, 20))
        self.rap_2.setCheckable(True)
        self.rap_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.rap_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 418, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.icon_name_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_5 = QVBoxLayout(self.main_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_widget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_19 = QPushButton(self.header_widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"border:none;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-58-39.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setIconSize(QSize(30, 30))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_19)

        self.horizontalSpacer_3 = QSpacerItem(317, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_2 = QLineEdit(self.header_widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton_20 = QPushButton(self.header_widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        icon8 = QIcon()
        icon8.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-06-07.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon8)
        self.pushButton_20.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_20)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalSpacer_5 = QSpacerItem(317, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_21 = QPushButton(self.header_widget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-10-46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon9)
        self.pushButton_21.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_21)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.page_enseignement = QWidget()
        self.page_enseignement.setObjectName(u"page_enseignement")
        self.label_2 = QLabel(self.page_enseignement)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 240, 341, 121))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.stackedWidget.addWidget(self.page_enseignement)
        self.page_fiche = QWidget()
        self.page_fiche.setObjectName(u"page_fiche")
        self.label_5 = QLabel(self.page_fiche)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 230, 211, 121))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.page_fiche)
        self.page_mensuel = QWidget()
        self.page_mensuel.setObjectName(u"page_mensuel")
        self.label_6 = QLabel(self.page_mensuel)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 260, 181, 121))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.page_mensuel)
        self.page_consultation = QWidget()
        self.page_consultation.setObjectName(u"page_consultation")
        self.label_7 = QLabel(self.page_consultation)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 260, 341, 121))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.page_consultation)
        self.page_avis = QWidget()
        self.page_avis.setObjectName(u"page_avis")
        self.label_8 = QLabel(self.page_avis)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 250, 281, 121))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.page_avis)
        self.page_rapport = QWidget()
        self.page_rapport.setObjectName(u"page_rapport")
        self.label_9 = QLabel(self.page_rapport)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 260, 231, 121))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.page_rapport)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1432, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.rap_1.toggled.connect(self.rap_2.setChecked)
        self.avis_1.toggled.connect(self.avis_2.setChecked)
        self.cons_1.toggled.connect(self.cons_2.setChecked)
        self.men_1.toggled.connect(self.men_2.setChecked)
        self.eva_1.toggled.connect(self.eva_2.setChecked)
        self.ens_1.toggled.connect(self.ens_2.setChecked)
        self.ens_2.toggled.connect(self.ens_1.setChecked)
        self.eva_2.toggled.connect(self.eva_1.setChecked)
        self.men_2.toggled.connect(self.men_1.setChecked)
        self.cons_2.toggled.connect(self.cons_1.setChecked)
        self.avis_2.toggled.connect(self.avis_1.setChecked)
        self.rap_2.toggled.connect(self.rap_1.setChecked)
        self.pushButton_8.toggled.connect(self.statusbar.close)
        self.pushButton_10.toggled.connect(self.statusbar.close)
        self.pushButton_10.toggled.connect(self.statusbar.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.ens_1.setText("")
        self.eva_1.setText("")
        self.men_1.setText("")
        self.cons_1.setText("")
        self.avis_1.setText("")
        self.rap_1.setText("")
        self.pushButton_8.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Responsable_Pedagogique", None))
        self.ens_2.setText(QCoreApplication.translate("MainWindow", u"V\u00e9rification_enseignements", None))
        self.eva_2.setText(QCoreApplication.translate("MainWindow", u"Fiche_evaluation", None))
        self.men_2.setText(QCoreApplication.translate("MainWindow", u"Suivi_mensuel", None))
        self.cons_2.setText(QCoreApplication.translate("MainWindow", u"Consultation_cahier_texte", None))
        self.avis_2.setText(QCoreApplication.translate("MainWindow", u"Recueil_Avis_Etudiants", None))
        self.rap_2.setText(QCoreApplication.translate("MainWindow", u"Rapport_Mensuel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Deconnexion", None))
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Verification Enseignements", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fiche Evaluation", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Suivi Mensuel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Consultation Cahier Texte", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Recueil Avis Etudiants", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rapport Mensuel", None))
    # retranslateUi

