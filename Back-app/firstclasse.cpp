#include "firstclasse.h"
#include "./ui_firstclasse.h"

FirstClasse::FirstClasse(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::FirstClasse)
{
    ui->setupUi(this);
}

FirstClasse::~FirstClasse()
{
    delete ui;
}
