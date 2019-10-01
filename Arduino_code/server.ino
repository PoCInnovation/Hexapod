#include "server.h"

Server::Server(int port, char *ssid, char *password)
{
    m_port = port;
    m_ssid = ssid;
    m_password = password;
}

Server::~Server() {}

void Server::start()
{
    Serial.println("Configuring access point...");
    /* if we just give the ssid, then there won't be any required password to connect to the wifi
        to set a password, just do :
            WiFi.softAP(m_ssid.c_str(), m_password.c_str());
    */
    WiFi.softAP(m_ssid.c_str());
    m_ip = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(m_ip);
    server.begin();
    Serial.println("Server started");
}

WiFiClient Server::is_available()
{
    return m_wifiserver.is_available();
}
