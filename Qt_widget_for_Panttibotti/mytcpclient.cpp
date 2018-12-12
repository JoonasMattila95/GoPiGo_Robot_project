#include "mytcpclient.h"

MyTcpClient::MyTcpClient(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket();
    qDebug() << "1: Socket Created" << endl;
    connect(socket, SIGNAL(connected()),this, SLOT(myConnectedSlot()));
    connect(socket, SIGNAL(bytesWritten(qint64)),this, SLOT(myBytesWrittenSlot(qint64)));
    connect(socket, SIGNAL(readyRead()),this, SLOT(receive()));
}

MyTcpClient::~MyTcpClient()
{
    delete socket;
    socket = nullptr;
    qDebug() << "10: Socket Deleted";
}

void MyTcpClient::connectToServer()
{
    qDebug() << "2: Connecting To Server";
    socket->connectToHost("192.168.43.81", 5550);
    if(!socket->waitForConnected(300))
    {
        qDebug() << "Error: " << socket->errorString();
        socket->deleteLater();
        exit(0);
    }

}

void MyTcpClient::myConnectedSlot()
{
    qDebug() << "3: Client Connected To Server" << endl;
    qDebug() << "4: Write message To Server.";
    socket->write("Terve");
}

void MyTcpClient::myBytesWrittenSlot(qint64 bytes)
{
    qDebug() << "5:" << bytes << " bytes written." << endl;
    qDebug() << "6: Wait for Server to answer..." << endl;
}

void MyTcpClient::stop_f()
{
    socket->write("STOP");
}


void MyTcpClient::skip_f()
{
    socket->write("OHITUS");
}

void MyTcpClient::receive()
{
    cout << "vastaanotettu:";
    QString data = socket->readLine();
    cout << data.toStdString() << endl;
}
