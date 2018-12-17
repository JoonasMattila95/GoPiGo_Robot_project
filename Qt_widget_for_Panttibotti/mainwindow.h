#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <mytcpclient.h>
#include <QString>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void label_feeder(QString feeder_appender);

private slots:
    void on_stop_button_clicked();

    void on_photoreg_bypass_button_clicked();

    void on_close_button_clicked();

    void debug_update();

    void on_connect_button_clicked();

    void on_resume_Button_clicked();

private:
    Ui::MainWindow *ui;
    MyTcpClient * client;
    QString * feeder;
    string holder1,holder2;
    int feeder_rep;
};

#endif // MAINWINDOW_H
