#!/usr/bin/env python
#------------------------------------------------------
#
#		This is a program for PCF8591 Module.
#
#		Warnng! The Analog input MUST NOT be over 3.3V!
#    
#		In this script, we use a poteniometer for analog
#   input, and a LED on AO for analog output.
#
#		you can import this script to another by:
#	import PCF8591 as ADC
#	
#	ADC.Setup(Address)  # Check it by sudo i2cdetect -y -1
#	ADC.read(channal)	# Channal range from 0 to 3
#	ADC.write(Value)	# Value range from 0 to 255		
#
#------------------------------------------------------
# Sound module name : Just search Arduino sound module or or raspberry pi sound module in english. -> 5V / Aout pin of Sound sensor connect to AIN2 pin of A/DC Converter
# A/DC converter name : PCF8591 -> 3.3V / SDA, SCL pins of A/DC converter connect to SDA, SCL pins of raspberry pi 
# Humidity and temperature Sensor name : dht11 -> (5V or 3.3V) / Signal pin of Humidity Sensor connect to pin07(GPIO 04)
import smbus
import time
import subprocess
import sys
import Adafruit_DHT # you shuld install this package. How to install? -> Refer 'https://gorakgarak.tistory.com/686' this site.
# Humidity Sensor SETUP
sensor = Adafruit_DHT.DHT11
pin = '4' #pin07(GPIO 04)

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y 1' in terminal.
def setup(Addr):
    
    global address
    address = Addr

def read(chn): #channel
    try:
        if chn == 0:
            bus.write_byte(address,0x40)
        if chn == 1:
            bus.write_byte(address,0x41)
        if chn == 2:
            bus.write_byte(address,0x42)
        if chn == 3:
            bus.write_byte(address,0x43)
        bus.read_byte(address) # dummy read to start conversion
    except Exception, e:
        print "Address: %s" % address
        print e
    return bus.read_byte(address)

def write(val):
    try:
        temp = val # move string value to temp
        temp = int(temp) # change string to integer
        # print temp to see on terminal else comment out
        bus.write_byte_data(address, 0x40, temp)
    except Exception, e:
        print "Error: Device address: 0x%2X" % address
        print e

# Find address of A/DC Converter at Raspberry pi
# if error occures at this part, you should install i2cdetect. How to install? -> Google it!
result = subprocess.check_output('sudo i2cdetect -y 1', shell=True)
address = 0
for idx, line in enumerate(result.split('\n')):
    if idx == 0:
        continue
    for num in line.split(' '):
        if ':' not in num and '-' not in num and len(num) != 0:
            address = int(num, 16)

setup(address)

def getLight():
    if address == 0:
        return -1
    else:
        return read(1)

def getSound(): # Sound module connect to 5V
    if address == 0:
        return -1
    else:
        return read(2)

def getHumidityTemperature():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return humidity, temperature
    except:
        print("except")
        return -1, -1
'''
def getTemperature():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)  # GPIO27 (BCM notation)
        return temperature
    except:
        return -1
'''