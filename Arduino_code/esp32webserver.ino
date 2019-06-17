#include <WiFi.h>
#include <WiFiClient.h>
#include <SoftwareSerial.h>
#include <WiFiAP.h>

const byte TRIGGER_PIN = 13;
const byte ECHO_PIN = 12;
const int STR_LEN = 32;

WiFiServer server(80);
SoftwareSerial port(2, 15);

void init_ultrassound()
{
    pinMode(TRIGGER_PIN, OUTPUT);
    digitalWrite(TRIGGER_PIN, LOW);
    pinMode(ECHO_PIN, INPUT);
    Serial.println("Ultrassounds pins init done");
}

float get_ultrassound_data()
{
    const unsigned long MEASURE_TIMEOUT = 25000UL;
    const float SOUND_SPEED = 340.0 / 1000;

    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
    long measure = pulseIn(ECHO_PIN, HIGH, MEASURE_TIMEOUT);
    return measure / 2.0 * SOUND_SPEED;
}

void init_web_server(char *ssid, char *password)
{
    Serial.println("Configuring access point...");
    WiFi.softAP(ssid);
    IPAddress myIP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(myIP);
    server.begin();
    Serial.println("Server started");
}

void setup()
{
    Serial.begin(115200);
    port.begin(9600);
    init_web_server((char *)"Hexapod_wifi", (char *)"poc");
    init_ultrassound();
}

void send_info_lidar(WiFiClient client)
{
    float distance_mm = get_ultrassound_data();
//    client.println("HTTP/1.1 200 OK");
//    client.println("Content-type:text/html");
//    client.println();

    client.print(distance_mm / 10.0, 2);
    client.println(F(" cm"));
//  delay(100);
//  client.println();
}

void get_client_movement()
{
    char str[STR_LEN];
    char c;
    int i = 1;

    str[0] = '#';
    while ((c = client.read()) != -1 && i < STR_LEN) {
        if (c == '!')
            break;
        str[i] = c;
        i += 1;
    }
    str[i] = '\0';
    port.println(str);

    //debug
    Serial.println(str);
}

void get_client_string(WiFiClient client)
{
    char c = client.read();

    if (c == '#')
        get_client_movement(client);
    else if (c == '$')
        send_info_lidar(client);
}

void loop()
{
    WiFiClient client = server.available();   // listen for incoming clients

    if (client) {
        Serial.println("New Client.");          // print a message out the serial port
        while (client.connected()) {            // loop while the client's connected
            if (client.available()) {
                get_client_string(client);
            }
        }
        client.stop();
        Serial.println("Client Disconnected.");
    }
}
