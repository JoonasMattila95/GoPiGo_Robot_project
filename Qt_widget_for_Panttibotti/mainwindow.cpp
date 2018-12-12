#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    client = new MyTcpClient;

    client->connect_f();

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_stop_button_clicked()       //hätäseis
{
    client->stop_f();
}

void MainWindow::on_photoreg_bypass_button_clicked() //kuvantunnistuksen ohitus
{
    client->skip_f();
}

void MainWindow::on_close_button_clicked() //apin sulkemisnappi
{
    client->disconnect_f();
    emit client->finished();
}

void MainWindow::on_pushButton_clicked()
{
    client->receive();
}
