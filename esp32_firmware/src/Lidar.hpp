#ifndef LIDAR_HPP
#define LIDAR_HPP

#include "HardwareSerial.h"

class Lidar {
    public:
        Lidar();
        void start();
        void stop();

    private:
        HardwareSerial _lidarSerial;
};

#endif // LIDAR_HPP
