/********************************************************************************
** Form generated from reading UI file 'firstclasse.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FIRSTCLASSE_H
#define UI_FIRSTCLASSE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FirstClasse
{
public:
    QWidget *centralwidget;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *FirstClasse)
    {
        if (FirstClasse->objectName().isEmpty())
            FirstClasse->setObjectName("FirstClasse");
        FirstClasse->resize(800, 600);
        centralwidget = new QWidget(FirstClasse);
        centralwidget->setObjectName("centralwidget");
        FirstClasse->setCentralWidget(centralwidget);
        menubar = new QMenuBar(FirstClasse);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 17));
        FirstClasse->setMenuBar(menubar);
        statusbar = new QStatusBar(FirstClasse);
        statusbar->setObjectName("statusbar");
        FirstClasse->setStatusBar(statusbar);

        retranslateUi(FirstClasse);

        QMetaObject::connectSlotsByName(FirstClasse);
    } // setupUi

    void retranslateUi(QMainWindow *FirstClasse)
    {
        FirstClasse->setWindowTitle(QCoreApplication::translate("FirstClasse", "FirstClasse", nullptr));
    } // retranslateUi

};

namespace Ui {
    class FirstClasse: public Ui_FirstClasse {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FIRSTCLASSE_H
