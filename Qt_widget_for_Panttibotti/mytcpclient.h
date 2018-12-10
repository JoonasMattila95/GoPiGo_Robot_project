#ifndef MYTCPCLIENT_H
#define MYTCPCLIENT_H

#include <QObject>
#include <QTcpSocket>
#include <iostream>

using namespace std;

class MyTcpClient : public QObject
{
    Q_OBJECT
public:
    explicit MyTcpClient(QObject *parent = nullptr);
    ~MyTcpClient();
    void connect_f();
    void disconnect_f();
    void stop_f();
    void skip_f();

signals:
    void finished();

public slots:


private:
    QTcpSocket * socket;
};

#endif // MYTCPCLIENT_H
