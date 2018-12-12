#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <mytcpclient.h>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_stop_button_clicked();

    void on_photoreg_bypass_button_clicked();

    void on_close_button_clicked();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
    MyTcpClient * client;
};

#endif // MAINWINDOW_H
