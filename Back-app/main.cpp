#include "firstclasse.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    FirstClasse w;
    w.show();
    return a.exec();
}
