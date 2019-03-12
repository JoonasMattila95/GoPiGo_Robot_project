#include "mytcpclient.h"

MyTcpClient::MyTcpClient(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket();
    connect(socket, SIGNAL(connected()),this, SLOT(myConnectedSlot()));
    connect(socket, SIGNAL(readyRead()),this, SLOT(receive()));
    connect(socket, SIGNAL(disconnected()),this, SLOT(myDisconnectedSlot()));
}

MyTcpClient::~MyTcpClient()
{
    delete socket;
    socket = nullptr;
}

void MyTcpClient::connectToServer()
{
    debug_send("Connecting To Server");
    socket->connectToHost("192.168.43.81", 5550);
    if(!socket->waitForConnected(100))
    {

        QString data = "Error: ";
        data.append(socket->errorString());
        debug_send(data.toStdString());
    }


}

void MyTcpClient::myConnectedSlot()
{
    debug_send("Client Connected To Server");
}

void MyTcpClient::myDisconnectedSlot()
{
    debug_send("Client disconnected from server");
}

void MyTcpClient::stop_f()
{
    socket->write("STOP");
    debug_send("Emergency stop pressed");
}


void MyTcpClient::skip_f()
{
    socket->write("BYPASS");
    debug_send("Photo recognition bypassed");
}

void MyTcpClient::disconnect_f()
{
    socket->close();

}

void MyTcpClient::receive()
{
    cout << "vastaanotettu:";
    QString data = socket->readLine();
    debug_send(data.toStdString());
}


string MyTcpClient::debug_handler()
{
   return info;
}

void MyTcpClient::debug_send(string debug_message)
{
    info = debug_message;
    emit debug();
}

void MyTcpClient::resume_f()
{
    socket->write("CONTINUE");
    debug_send("Emergency stop cleared");
}
