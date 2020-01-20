#!/usr/bin/python

from oheye import analog_in 
import time

while True:
    for i in range(15):
        value = analog_in.read(i)
        print "%4d" % value,
    time.sleep(0.2)
    print;
