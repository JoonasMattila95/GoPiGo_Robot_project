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

signals:
    void finished();

public slots:
    void myConnectedSlot();
    void myBytesWrittenSlot(qint64 bytes);
    void receive();

private:
    QTcpSocket * socket;
};

#endif // MYTCPCLIENT_H
