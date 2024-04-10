#include "diecteuretude.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DiecteurEtude w;
    w.show();
    return a.exec();
}
