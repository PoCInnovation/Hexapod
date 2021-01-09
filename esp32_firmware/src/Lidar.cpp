#include "Lidar.hpp"
#include "lidar_protocol.h"

#define START_BYTE 0xA5

Lidar::Lidar() : _lidarSerial(115200)
{

}

void Lidar::start()
{
    _lidarSerial.write(START_BYTE);
    _lidarSerial.write(LIDAR_CMD_SCAN);
}

void Lidar::stop()
{
    _lidarSerial.write(START_BYTE);
    _lidarSerial.write(LIDAR_CMD_STOP);
}