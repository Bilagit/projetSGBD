#ifndef DIECTEURETUDE_H
#define DIECTEURETUDE_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class DiecteurEtude;
}
QT_END_NAMESPACE

class DiecteurEtude : public QMainWindow
{
    Q_OBJECT

public:
    DiecteurEtude(QWidget *parent = nullptr);
    ~DiecteurEtude();

private:
    Ui::DiecteurEtude *ui;
};
#endif // DIECTEURETUDE_H
