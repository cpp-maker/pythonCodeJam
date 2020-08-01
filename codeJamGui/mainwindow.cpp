#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle(tr("Password Generator"));
    this->setStyleSheet("background-color: #447777");
    this->setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Expanding);
}

MainWindow::~MainWindow()
{
    delete ui;
}

