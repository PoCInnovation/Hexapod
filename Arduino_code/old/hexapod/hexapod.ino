#include <WiFi.h>
#include <WiFiClient.h>
#include <SoftwareSerial.h>
#include <WiFiAP.h>

const byte TRIGGER_PIN = 13;
const byte ECHO_PIN = 12;

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

void send_ultrassound_data(WiFiClient &client)
{
    float mesure = get_ultrassound_data();

    Serial.println(mesure); // debug print
    if (client) {
        Serial.println("Sending via WIFI :"); // debug print
        client.println(mesure);
    }
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
    init_web_server((char*)"Hexapod_wifi", (char*)"poc");
    init_ultrassound();
}

void get_client_string(WiFiClient &client)
{
    const int STR_LEN = 1024;

    char str[1024];
    char c;
    int i = 1;

    str[0] = '#';
    while ((c = client.read()) != -1 && i < STR_LEN - 5) {
        if (c == '!')
            break;
        str[i] = c;
        i += 1;
    }
    str[i] = '\0';
    Serial.println(str);
}

void loop()
{
    WiFiClient client = server.available();   // listen for incoming clients

    if (client) {
        Serial.println("New Client.");           // print a message out the serial port
        while (client.connected()) {            // loop while the client's connected
            if (client.available()) {
                get_client_string(client);
            }
        }
        client.stop();
        Serial.println("Client Disconnected.");
    }
    send_ultrassound_data(client);
}
