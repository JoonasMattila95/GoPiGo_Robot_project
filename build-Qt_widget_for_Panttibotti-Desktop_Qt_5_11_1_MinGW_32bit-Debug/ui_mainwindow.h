/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QPushButton *photoreg_bypass_button;
    QPushButton *close_button;
    QPushButton *stop_button;
    QLabel *debug_label;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(860, 414);
        MainWindow->setStyleSheet(QLatin1String("QMainWindow\n"
"{\n"
"background-image:url(:/materiaali/tekstuuri.jpg);\n"
"}"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(0, 250, 861, 131));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(5, 5, 5, 5);
        photoreg_bypass_button = new QPushButton(gridLayoutWidget);
        photoreg_bypass_button->setObjectName(QStringLiteral("photoreg_bypass_button"));
        photoreg_bypass_button->setMinimumSize(QSize(240, 40));
        photoreg_bypass_button->setStyleSheet(QLatin1String("QPushButton\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:white;\n"
"border-radius:6px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:rgb(85, 255, 255);\n"
"}s"));

        gridLayout->addWidget(photoreg_bypass_button, 2, 1, 1, 1);

        close_button = new QPushButton(gridLayoutWidget);
        close_button->setObjectName(QStringLiteral("close_button"));
        close_button->setMinimumSize(QSize(240, 40));
        close_button->setStyleSheet(QLatin1String("QPushButton\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:white;\n"
"border-radius:6px;\n"
"	font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:rgb(85, 255, 255);\n"
"}s"));

        gridLayout->addWidget(close_button, 2, 3, 1, 1);

        stop_button = new QPushButton(gridLayoutWidget);
        stop_button->setObjectName(QStringLiteral("stop_button"));
        stop_button->setMinimumSize(QSize(240, 40));
        stop_button->setStyleSheet(QLatin1String("QPushButton\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:white;\n"
"border-radius:6px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border: 2px solid rgb(0, 85, 255);\n"
"background-color:rgb(85, 255, 255);\n"
"}s"));

        gridLayout->addWidget(stop_button, 2, 2, 1, 1);

        debug_label = new QLabel(centralWidget);
        debug_label->setObjectName(QStringLiteral("debug_label"));
        debug_label->setGeometry(QRect(10, 40, 841, 201));
        debug_label->setStyleSheet(QLatin1String("QLabel\n"
"{\n"
"background-color:white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 2px solid rgb(0, 85, 255);\n"
"border-radius:6px;\n"
"}"));
        debug_label->setAlignment(Qt::AlignCenter);
        MainWindow->setCentralWidget(centralWidget);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        photoreg_bypass_button->setText(QApplication::translate("MainWindow", "Ohita kuvantunnistus", nullptr));
        close_button->setText(QApplication::translate("MainWindow", "Sulje sovellus", nullptr));
        stop_button->setText(QApplication::translate("MainWindow", "H\303\244t\303\244seis", nullptr));
        debug_label->setText(QApplication::translate("MainWindow", "Debug_ruutu", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
