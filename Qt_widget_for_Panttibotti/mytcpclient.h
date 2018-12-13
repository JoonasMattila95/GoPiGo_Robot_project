#ifndef MYTCPCLIENT_H
#define MYTCPCLIENT_H

#include <QObject>
#include <QTcpSocket>
#include <iostream>
#include <QIODevice>

using namespace std;

class MyTcpClient : public QObject
{
    Q_OBJECT
public:
    explicit MyTcpClient(QObject *parent = nullptr);
    ~MyTcpClient();
    void stop_f();
    void skip_f();
    void connectToServer();
    void disconnect_f();

    string debug_handler();
    void debug_send(string debug_message);

signals:
    void finished();
    void debug();

public slots:
    void myConnectedSlot();
    void receive();
    void myDisconnectedSlot();

private:
    QTcpSocket * socket;
    string info;
};

#endif // MYTCPCLIENT_H
