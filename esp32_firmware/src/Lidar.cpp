#include "Lidar.hpp"
#include "lidar_protocol.h"

Lidar::Lidar() : _lidarSerial(115200)
{

}

void Lidar::start()
{
    _lidarSerial.write(LIDAR_CMD_SCAN);
}

void Lidar::stop()
{
    _lidarSerial.write(LIDAR_CMD_STOP);
}