# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DirecteurEtude.ui'
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
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 882)
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
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 00-58-39.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.PV_1 = QPushButton(self.icon_only_widget)
        self.PV_1.setObjectName(u"PV_1")
        icon = QIcon()
        icon.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-11 14-50-36.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PV_1.setIcon(icon)
        self.PV_1.setCheckable(True)
        self.PV_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.PV_1)

        self.SEM_1 = QPushButton(self.icon_only_widget)
        self.SEM_1.setObjectName(u"SEM_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-11 14-48-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SEM_1.setIcon(icon1)
        self.SEM_1.setCheckable(True)
        self.SEM_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.SEM_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 616, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.icon_only_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-45-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_4)


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
"}\n"
"")
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

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.PV_2 = QPushButton(self.icon_name_widget)
        self.PV_2.setObjectName(u"PV_2")
        self.PV_2.setIcon(icon)
        self.PV_2.setCheckable(True)
        self.PV_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.PV_2)

        self.SEM_2 = QPushButton(self.icon_name_widget)
        self.SEM_2.setObjectName(u"SEM_2")
        self.SEM_2.setIcon(icon1)
        self.SEM_2.setCheckable(True)
        self.SEM_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.SEM_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 616, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_6 = QPushButton(self.icon_name_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_9 = QPushButton(self.header_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 01-58-39.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_9.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_10 = QPushButton(self.header_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon4 = QIcon()
        icon4.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-06-07.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_10)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_11 = QPushButton(self.header_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon5 = QIcon()
        icon5.addFile(u":/images/Capture d\u2019\u00e9cran du 2024-04-10 10-10-46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_11)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_PV = QWidget()
        self.page_PV.setObjectName(u"page_PV")
        self.label_4 = QLabel(self.page_PV)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 250, 171, 121))
        font = QFont()
        font.setFamilies([u"aakar"])
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.page_PV)
        self.page_Sem = QWidget()
        self.page_Sem.setObjectName(u"page_Sem")
        self.label_5 = QLabel(self.page_Sem)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 300, 511, 121))
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.page_Sem)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1038, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_9.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_9.toggled.connect(self.icon_name_widget.setVisible)
        self.SEM_1.toggled.connect(self.SEM_2.setChecked)
        self.PV_1.toggled.connect(self.PV_2.setChecked)
        self.PV_2.toggled.connect(self.PV_1.setChecked)
        self.SEM_2.toggled.connect(self.SEM_1.setChecked)
        self.pushButton_4.toggled.connect(MainWindow.close)
        self.pushButton_6.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.PV_1.setText("")
        self.SEM_1.setText("")
        self.pushButton_4.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Directeur_Etude", None))
        self.PV_2.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.SEM_2.setText(QCoreApplication.translate("MainWindow", u"Rapport Semestre", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Deconnexion", None))
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"P.V", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rapport Semestre", None))
    # retranslateUi

