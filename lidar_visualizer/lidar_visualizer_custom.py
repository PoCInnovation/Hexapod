#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import serial
import math
import sys
import time
import struct
from dataclasses import dataclass, field
from typing import List

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# debug define
DEBUG_NO_HUD=1

@dataclass
class scanData:
    packet_header: int = 0# 0x55AA
    packet_type: int = 0 # 0 or 1
    sample_quantity: int = 0
    starting_angle: int = 0
    end_angle: int = 0
    check_code: int = 0
    sampling_data: List[int] = field(default_factory=list)


class Controller:
    def __init__(self, port):
        self.port = port
        self.baud = 230400
        self.con = serial.Serial(self.port, self.baud, serial.EIGHTBITS,
                                 serial.PARITY_NONE, serial.STOPBITS_ONE)
        self.con.flush()
        self.con.flushInput()
        self.con.read_all()
        self.is_started = False

    def _send(self, payload):
        self.con.write(payload)


    def start(self):
        self._send(bytearray([0xA5, 0x60]))
        self.is_started = True


    def stop(self):
        self.is_started = False
        self._send(bytearray([0xA5, 0x65]))

    def convert_scan_data_header(self, packet):
        d = [hex(x) for x in packet]
        s = scanData()
        s.packet_header = int(d[1], 16) + int(d[0], 16)
        s.packet_type = int(d[2], 16)
        s.sample_quantity = int(d[3], 16)
        s.starting_angle = int(d[4], 16) + int(d[5], 16)
        s.end_angle = int(d[6], 16) + int(d[7], 16)
        s.check_code = int(d[8], 16) + int(d[9], 16)
        return s


    def read(self):
        if self.is_started == False:
            return None
        data = self.con.read(10)
        d = [hex(x) for x in data]
        if data[0] == 0xAA:
            scan_data = self.convert_scan_data_header(data)
            if scan_data.sample_quantity > 0:
                points = self.con.read(2 * scan_data.sample_quantity)
                d = [hex(x) for x in points]
                p = []
                for i in range(0, len(d), 2):
                    p.append(int(d[i], 16) + int(d[i+1], 16))
                print(p)


                # print(points)


class Gui:
    def __init__(self, controller):
        self.controller = controller

        pygame.init()
        self.screen = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Lidar Visualizer')

        if not DEBUG_NO_HUD:
            pygame.font.init()
            self.font = pygame.font.SysFont("arialttf", 30)
        else:
            self.font = None


    def draw_radar_view(self):
        radar_center = (350, 350)
        for i in range(1, 5):
            pygame.draw.circle(self.screen, GREEN, radar_center, i*80, width=2)
        pygame.draw.circle(self.screen, GREEN, radar_center, 18)

        radar_len = 325
        for i in range(12):
            angle = i * 30
            x = int(radar_center[0] + math.cos(math.radians(angle)) * radar_len)
            y = int(radar_center[1] + math.sin(math.radians(angle)) * radar_len)
            pygame.draw.line(self.screen, GREEN, radar_center, (x,y), width=1)

    def draw_hud(self):
        textsurface = self.font.render('Controls', True, WHITE)
        self.screen.blit(textsurface, (900, 10))

        textsurface = self.font.render('S -> Start Lidar', True, WHITE)
        self.screen.blit(textsurface, (910, 100))

        textsurface = self.font.render('T -> Stop Lidar', True, WHITE)
        self.screen.blit(textsurface, (910, 150))

        textsurface = self.font.render('P -> Toggle freeze screen', True, WHITE)
        self.screen.blit(textsurface, (910, 200))

    def draw(self):
        self.draw_radar_view()
        pygame.draw.line(self.screen, WHITE, (850, 0), (850, 720), width=5)
        if not DEBUG_NO_HUD:
            self.draw_hud()


    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_s:
                        print("Start")
                        self.controller.start()
                    elif event.key == pygame.K_t:
                        print("Stop")
                        self.controller.stop()

            self.controller.read()
            self.screen.fill(BLACK)
            self.draw()
            pygame.display.flip()

    def quit(self):
        self.controller.stop()
        pygame.quit()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("USAGE: ./lidar_visualizer PORT")
    c = Controller(sys.argv[1])
    g = Gui(c)
    g.start()
    g.quit()
