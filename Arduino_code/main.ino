#include "server.h"
#include "ultrasound.h"
#include <SoftwareSerial.h>
#include <WiFiClient.h>

Server server(80, "Hexapod_Wifi", "Poc2018");
Ultrasound ultrassound(13, 12);
SoftwareSerial portBoardHexapod(2, 15); // le port sur lequel on envoie les donnees sur l'hexapod

void setup()
{
    Serial.begin(115200);
    portBoardHexapod.begin(9600);
    server.start();
    ultrassound.init();
}

void loop()
{
    // We can't have more than 1 client connected
    WiFiClient client = server.available(); // listen for incoming clients

    if (client) {
        Serial.println("New Client."); // print a message out the serial port
        while (client.connected()) {   // loop while the client's connected
            if (client.available()) {
                get_client_string(client);
            }
        }
        client.stop();
        Serial.println("Client Disconnected.");
    }
}
