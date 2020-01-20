#!/usr/bin/python

import spidev
from random import random
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)


spi=spidev.SpiDev()
spi.open(0, 0)

def readADC(channel):
    if channel >15 or channel<0:
        return -1
    r=spi.xfer2([1, 8+channel<<4, 0])
    v=((r[1]&3)<<8)+r[2]
    print(v)
    return v

while True:
    pitch = readADC(0)
    
    sender.send_message('/osc_msg', pitch)
    <F12><F11>
sleep(.2)
