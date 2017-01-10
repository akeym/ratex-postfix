#!/usr/bin/env python
import serial
import urllib2
import time

KEY_CODE     = chr(1)
KEY_START    = chr(2)
KEY_END      = chr(3)
KEY_LEFT     = chr(4)
KEY_RIGHT    = chr(6)
KEY_CLEAR    = chr(8)
KEY_DOWN     = chr(13)
KEY_RETURN   = chr(13)
KEY_LOCK     = chr(14)
KEY_FLASH    = chr(15)
KEY_TIMER    = chr(162)
KEY_LIGHT    = chr(163)
KEY_POWER    = chr(164)
KEY_UP       = chr(18)
KEY_CONTROL  = chr(20)
KEY_CLOCK    = chr(26)
KEY_SPACE    = chr(32)
KEY_POINT    = chr(46)
ATTR_FLASH   = chr(129)
ATTR_NOFLASH = chr(128)
PASSWORD = '2222'
ROWS = 12
COLS = 2
BAUD = 9600

s = serial.Serial()
s.baudrate = BAUD
s.port = '/dev/ttyUSB0'
s.open()

row = 1
col = 1
data = urllib2.urlopen("http://cactus.nws.oregonstate.edu/smtp.csv").readlines()

for line in data:
    attr1 = chr(128)
    attr2 = chr(128)

    sline = line.strip('\n').split(',')
    if sline == ['']:
        break
    if int(sline[1]) > 1000:
	attr1=chr(129)
    if int(sline[2]) > 1000:
        attr2=chr(129)
    cmd = KEY_CONTROL+PASSWORD+'{:02d}{:02d}{:6d}'.format(row,col,int(sline[1]))+attr1+KEY_RETURN+'{:02d}{:02d}{:6d}'.format(row,col+6,int(sline[2]))+attr2+KEY_RETURN+KEY_END
    s.write(cmd)
    if row == 2:
        row = 1
        col = col + 1
    else:
        row = 2
    time.sleep(.1)

s.close()





