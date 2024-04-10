#ifndef FIRSTCLASSE_H
#define FIRSTCLASSE_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class FirstClasse;
}
QT_END_NAMESPACE

class FirstClasse : public QMainWindow
{
    Q_OBJECT

public:
    FirstClasse(QWidget *parent = nullptr);
    ~FirstClasse();

private:
    Ui::FirstClasse *ui;
};
#endif // FIRSTCLASSE_H
