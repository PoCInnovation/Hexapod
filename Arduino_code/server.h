#ifndef SERVER_H
#define SERVER_H

#include <WiFi.h>
#include <WiFiAP.h>

class Server
{
private:
    int m_port;
    String m_ssid;
    String m_password;
    IPAddress m_ip;
    WiFiServer m_wifiserver;

public:
    Server(int port, String ssid, String password);
    ~Server();
    void start();
    WiFiClient is_available();
};

#endif