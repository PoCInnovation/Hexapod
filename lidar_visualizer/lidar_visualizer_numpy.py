import threading
import PyLidar3
import matplotlib.pyplot as plt
import math
import time
import sys

x = []
y = []

def draw():
    plt.figure(1)
    plt.cla()
    plt.ylim(-9000, 9000)
    plt.xlim(-9000, 9000)
    plt.scatter(x, y, c='r', s=8)

    plt.pause(0.001)


def start(port):
    global x, y
    for _ in range(360):
        x.append(0)
        y.append(0)

    Obj = PyLidar3.YdLidarG4(port)
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        t = time.time()  # start time
        while (time.time() - t) < 30:  # scan for 30 seconds
            data = next(gen)
            for angle in range(0, 360):
                if(data[angle] > 1000):
                    x[angle] = data[angle] * math.cos(math.radians(angle))
                    y[angle] = data[angle] * math.sin(math.radians(angle))
            draw()
        plt.show()
        Obj.StopScanning()
        Obj.Disconnect()
    else:
        print("Error connecting to device")


if __name__ == '__main__':
    start(sys.argv[1])
