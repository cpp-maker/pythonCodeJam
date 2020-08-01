/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QLabel *infoLabel;
    QLabel *infoLabel1;
    QLineEdit *inputField;
    QPushButton *buttonToGo;
    QLabel *newPassLabel;
    QLineEdit *showNewPass;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(390, 139);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        formLayoutWidget = new QWidget(centralwidget);
        formLayoutWidget->setObjectName(QString::fromUtf8("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(10, 0, 371, 91));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        infoLabel = new QLabel(formLayoutWidget);
        infoLabel->setObjectName(QString::fromUtf8("infoLabel"));

        formLayout->setWidget(0, QFormLayout::LabelRole, infoLabel);

        infoLabel1 = new QLabel(formLayoutWidget);
        infoLabel1->setObjectName(QString::fromUtf8("infoLabel1"));

        formLayout->setWidget(0, QFormLayout::FieldRole, infoLabel1);

        inputField = new QLineEdit(formLayoutWidget);
        inputField->setObjectName(QString::fromUtf8("inputField"));

        formLayout->setWidget(1, QFormLayout::LabelRole, inputField);

        buttonToGo = new QPushButton(formLayoutWidget);
        buttonToGo->setObjectName(QString::fromUtf8("buttonToGo"));
        buttonToGo->setAutoDefault(false);
        buttonToGo->setFlat(false);

        formLayout->setWidget(1, QFormLayout::FieldRole, buttonToGo);

        newPassLabel = new QLabel(formLayoutWidget);
        newPassLabel->setObjectName(QString::fromUtf8("newPassLabel"));

        formLayout->setWidget(2, QFormLayout::LabelRole, newPassLabel);

        showNewPass = new QLineEdit(formLayoutWidget);
        showNewPass->setObjectName(QString::fromUtf8("showNewPass"));

        formLayout->setWidget(2, QFormLayout::FieldRole, showNewPass);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 390, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        buttonToGo->setDefault(false);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        infoLabel->setText(QCoreApplication::translate("MainWindow", "Password generator", nullptr));
        infoLabel1->setText(QCoreApplication::translate("MainWindow", "Push button to make a password", nullptr));
        inputField->setInputMask(QString());
        inputField->setText(QCoreApplication::translate("MainWindow", "Enter pass length", nullptr));
        buttonToGo->setText(QCoreApplication::translate("MainWindow", "Go!", nullptr));
        newPassLabel->setText(QCoreApplication::translate("MainWindow", "New password", nullptr));
        showNewPass->setText(QCoreApplication::translate("MainWindow", "New password will show here", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
