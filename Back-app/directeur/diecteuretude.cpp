#include "diecteuretude.h"
#include "./ui_diecteuretude.h"

DiecteurEtude::DiecteurEtude(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::DiecteurEtude)
{
    ui->setupUi(this);
}

DiecteurEtude::~DiecteurEtude()
{
    delete ui;
}
