# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'respclasse.ui'
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
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1457, 1021)
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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 00-58-39.png"))

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.compte_1 = QPushButton(self.icon_only_widget)
        self.compte_1.setObjectName(u"compte_1")
        self.compte_1.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 12-33-46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compte_1.setIcon(icon)
        self.compte_1.setCheckable(True)
        self.compte_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.compte_1)

        self.verification_1 = QPushButton(self.icon_only_widget)
        self.verification_1.setObjectName(u"verification_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-33-53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verification_1.setIcon(icon1)
        self.verification_1.setCheckable(True)
        self.verification_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.verification_1)

        self.fiche_1 = QPushButton(self.icon_only_widget)
        self.fiche_1.setObjectName(u"fiche_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-34-51.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fiche_1.setIcon(icon2)
        self.fiche_1.setCheckable(True)
        self.fiche_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.fiche_1)

        self.suivi_1 = QPushButton(self.icon_only_widget)
        self.suivi_1.setObjectName(u"suivi_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-36-10.png", QSize(), QIcon.Normal, QIcon.Off)
        self.suivi_1.setIcon(icon3)
        self.suivi_1.setCheckable(True)
        self.suivi_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.suivi_1)

        self.transmission_1 = QPushButton(self.icon_only_widget)
        self.transmission_1.setObjectName(u"transmission_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 12-36-27.png", QSize(), QIcon.Normal, QIcon.Off)
        self.transmission_1.setIcon(icon4)
        self.transmission_1.setCheckable(True)
        self.transmission_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.transmission_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 580, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-45-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);	\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	color: white;\n"
"	text-align:left;\n"
"	height: 30px;\n"
"	border:none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 00-58-39.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.compte_2 = QPushButton(self.icon_name_widget)
        self.compte_2.setObjectName(u"compte_2")
        self.compte_2.setIcon(icon)
        self.compte_2.setCheckable(True)
        self.compte_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.compte_2)

        self.verification_2 = QPushButton(self.icon_name_widget)
        self.verification_2.setObjectName(u"verification_2")
        self.verification_2.setIcon(icon1)
        self.verification_2.setCheckable(True)
        self.verification_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.verification_2)

        self.fiche_2 = QPushButton(self.icon_name_widget)
        self.fiche_2.setObjectName(u"fiche_2")
        self.fiche_2.setIcon(icon2)
        self.fiche_2.setCheckable(True)
        self.fiche_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fiche_2)

        self.suivi_2 = QPushButton(self.icon_name_widget)
        self.suivi_2.setObjectName(u"suivi_2")
        self.suivi_2.setIcon(icon3)
        self.suivi_2.setCheckable(True)
        self.suivi_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.suivi_2)

        self.transmission_2 = QPushButton(self.icon_name_widget)
        self.transmission_2.setObjectName(u"transmission_2")
        self.transmission_2.setIcon(icon4)
        self.transmission_2.setCheckable(True)
        self.transmission_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.transmission_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 580, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.icon_name_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-58-39.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(30, 30))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(339, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-06-07.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(339, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-10-46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_compte_rendu = QWidget()
        self.page_compte_rendu.setObjectName(u"page_compte_rendu")
        self.label_4 = QLabel(self.page_compte_rendu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 250, 511, 111))
        font1 = QFont()
        font1.setPointSize(50)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.page_compte_rendu)
        self.page_verification = QWidget()
        self.page_verification.setObjectName(u"page_verification")
        self.label_5 = QLabel(self.page_verification)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 240, 331, 131))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_5.setFont(font2)
        self.stackedWidget.addWidget(self.page_verification)
        self.page_evaluation = QWidget()
        self.page_evaluation.setObjectName(u"page_evaluation")
        self.label_6 = QLabel(self.page_evaluation)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 210, 281, 161))
        self.label_6.setFont(font2)
        self.stackedWidget.addWidget(self.page_evaluation)
        self.page_suivi = QWidget()
        self.page_suivi.setObjectName(u"page_suivi")
        self.label_7 = QLabel(self.page_suivi)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 160, 241, 171))
        self.label_7.setFont(font2)
        self.stackedWidget.addWidget(self.page_suivi)
        self.page_transmission = QWidget()
        self.page_transmission.setObjectName(u"page_transmission")
        self.label_8 = QLabel(self.page_transmission)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 200, 341, 161))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.page_transmission)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1457, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.transmission_1.toggled.connect(self.transmission_2.setChecked)
        self.suivi_1.toggled.connect(self.suivi_2.setChecked)
        self.fiche_1.toggled.connect(self.fiche_2.setChecked)
        self.verification_1.toggled.connect(self.verification_2.setChecked)
        self.compte_1.toggled.connect(self.compte_2.setChecked)
        self.compte_2.toggled.connect(self.compte_1.setChecked)
        self.verification_2.toggled.connect(self.verification_1.setChecked)
        self.fiche_2.toggled.connect(self.fiche_1.setChecked)
        self.suivi_2.toggled.connect(self.suivi_1.setChecked)
        self.transmission_2.toggled.connect(self.transmission_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.compte_1.setText("")
        self.verification_1.setText("")
        self.fiche_1.setText("")
        self.suivi_1.setText("")
        self.transmission_1.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Chef_D\u00e9partement", None))
        self.compte_2.setText(QCoreApplication.translate("MainWindow", u"Compte_rendu", None))
        self.verification_2.setText(QCoreApplication.translate("MainWindow", u"V\u00e9rification_enseignements", None))
        self.fiche_2.setText(QCoreApplication.translate("MainWindow", u"Fiche_evaluation", None))
        self.suivi_2.setText(QCoreApplication.translate("MainWindow", u"Suivi_mensuel", None))
        self.transmission_2.setText(QCoreApplication.translate("MainWindow", u"Transmission_PV", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"D\u00e9connexion", None))
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Compte_rendu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Verification_enseignements", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fiche_evaluation", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page_suivi", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Transmission_PV", None))
    # retranslateUi

