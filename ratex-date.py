#!/usr/bin/python

# set current time and date on Ratex exchange rate board using system time

# change chr(1) to 0 to use 12 hour time instead, and update format string

import serial
import time

PASSWORD='2222'

s = serial.Serial()
s.baudrate=9600
s.port = '/dev/ttyUSB0'

s.open()
s.write(chr(14) + PASSWORD + chr(161) + chr(1) + time.strftime('%w%y%m%d%H%M%S') + chr(14))
s.close()
