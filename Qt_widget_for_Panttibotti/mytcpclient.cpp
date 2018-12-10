#include "mytcpclient.h"

MyTcpClient::MyTcpClient(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket;
}

MyTcpClient::~MyTcpClient()
{
    delete socket;
    socket = nullptr;
}

void MyTcpClient::connect_f()
{
    socket->connectToHost("127.0.0.1", 5550);   //yhdistetään porttiin 5550
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
