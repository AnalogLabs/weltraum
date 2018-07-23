# log_gps.py
# Read GPS coordinates, velocity, altitude from USB module in real time and
# Log coordinates to file 
# Author: Omar Metwally, MD 
#         omar@analog.earth
# License: ANALOG LABS

import serial, sys, os
from time import time

ser = serial.Serial('/dev/ttyACM0')
latitude = ''
longitude = ''# fleetfox.py

import serial, sys, os
from time import time, sleep
from random import randint
from sys import argv

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

ser = serial.Serial('/dev/ttyACM0')
latitude = '' 
longitude = ''
altitude = ''
velocity = ''
description = ''

if len(argv) > 1:
    description = ' '.join(argv[1:])
    print('Description of GPS trace: ',description)

while True:
                line = str(ser.readline())
                print('GPS data: ',line)

                if '$GPGGA' in line:
                    line = line.split(',')
                    #print(str(line[2]), str(line[4]))
                    lat_dd = float(str(line[2])[0:2])
                    lat_mm = float(str(line[2])[2:])/60
                    latitude = lat_dd + lat_mm
                    if line[3].lower() == 's':
                        latitude = latitude * -1
                    long_dd = float(str(line[4])[0:3]) 
                    long_mm = float(str(line[4][3:]))/60
                    longitude = long_dd + long_mm
                    if line[5].lower() == 'w':
                        longitude = longitude * -1
                    print('Longitude: ', longitude)
                    print('Latitude: ', latitude)

                    altitude = float(line[9])
                    print('Altitude: ', altitude, ' meters')
               
                if '$GPVTG' in line:
                    line = line.split(',K')
                    velocity = float(line[0].split(',')[-1])
                    print('Velocity: ',str(velocity),' km/hr')

                if len(str(longitude))*len(str(latitude))*len(str(altitude))*len(str(velocity)) > 0:
                        print('Writing coordinates, altitude, velocity, and description to file: ',longitude, latitude, altitude, velocity, description)
                        filehandle = open('/home/pi/Desktop/way.csv', 'a')
                        filehandle.write(str(longitude)+', '+str(latitude)+', '+str(altitude)+', '+str(velocity)+', '+str(time())+', '+description+'\n')
                        filehandle.close()
                        location_string = str(latitude)+', '+str(longitude)

                        longitude =''
                        latitude = ''
                        altitude = ''
                        velocity = ''
                        print("LED on")
                        GPIO.output(18,GPIO.HIGH)
                        sleep(5)
                        print("LED off")
                        GPIO.output(18,GPIO.LOW)
                        sleep(5)


