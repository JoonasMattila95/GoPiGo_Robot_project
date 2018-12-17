#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    feeder = new QString;
    feeder_rep = 0;

    ui->setupUi(this);
    client = new MyTcpClient;
    QObject::connect(client,SIGNAL(debug()),this,SLOT(debug_update()));
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
}

void MainWindow::label_feeder(QString feeder_appender)      //debug ruudun tekstinsyöttäjä
{

    if(feeder_rep == 0)
    {
        feeder->append(feeder_appender);
        ui->debug_label->setText(*feeder);

        holder1 = feeder_appender.toStdString();
        feeder_rep ++;
    }

    else if(feeder_rep == 1)
    {
        feeder->append(QString::fromStdString(holder1)+"\r\n");
        feeder->append(feeder_appender);
        ui->debug_label->setText(*feeder);

        holder2 = feeder_appender.toStdString();
        feeder_rep ++;
    }

    else if (feeder_rep == 2)
    {
        feeder->append(QString::fromStdString(holder1)+"\r\n");

        feeder->append(QString::fromStdString(holder2)+"\r\n");
        feeder->append(feeder_appender);
        ui->debug_label->setText(*feeder);

        holder1 = holder2;
        holder2 = feeder_appender.toStdString();
    }

    feeder->clear();

}

void MainWindow::debug_update()
{
    label_feeder(QString::fromStdString(client->debug_handler()));
}

void MainWindow::on_connect_button_clicked()
{
  client->connectToServer();
}

void MainWindow::on_resume_Button_clicked()
{
    client->resume_f();
}
