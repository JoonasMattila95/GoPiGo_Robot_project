#include "mytcpclient.h"

MyTcpClient::MyTcpClient(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket;
    connect(socket,SIGNAL(readyRead()),socket,SLOT(receive()));
    emit socket->readyRead();

}

MyTcpClient::~MyTcpClient()
{
    delete socket;
    socket = nullptr;
}

void MyTcpClient::connect_f()
{
    socket->connectToHost("192.168.43.81", 5550);   //yhdistetään porttiin 5550
    cout << "Connecting to Server" << endl;
}

void MyTcpClient::disconnect_f()
{
    socket->disconnectFromHost();
    cout << "Disconnected from the Server" << endl;
}

void MyTcpClient::stop_f()
{
    socket->write("Halt boi");
}


void MyTcpClient::skip_f()
{
    socket->write("skip photo");
}

void MyTcpClient::receive()
{
    cout << "vastaanotettu:";
    QString data = socket->readLine();
    cout << data.toStdString() << endl;
}
