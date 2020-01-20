# oheye
Oh Eye for Raspberry Pi 

16 analog inputs for the Pi. Requires SPI to be enabled in the Pi's configuration. Uses two MCP3008 10-bit A to D converters.

There's a Python library on the Python Package Index (https://pypi.org/project/oheye/) that you can install from the command line with Pip:

<pre>  sudo pip install oheye</pre>
  
Take a look at the ohEyePython directory for a few examples:

<pre>
#!/usr/bin/python

from oheye import analog_in 
import time

while True:
    for i in range(15):
        value = analog_in.read(i)
        print "%4d" % value,
    time.sleep(0.2)
    print;
</pre>

You can also use the Pd example in that directory to use the ohEye from Pure Data. That requires the WiringPi Pd external:

 http://nyu-waverlylabs.org/rpi-gpio/
 