#include "client.h"

void send_info_lidar(WiFiClient client)
{
    float distance_mm = get_ultrassound_data();

    client.print(distance_mm / 10.0, 2);
    client.println(F(" cm"));
}

void get_client_movement()
{
    const int STR_LEN = 32;
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
    portBoardHexapod.println(str);
    Serial.println(str); //debug
}

void get_client_string(WiFiClient client)
{
    char c = client.read();

    if (c == '#')
        get_client_movement(client);
    else if (c == '$')
        send_info_lidar(client);
}
