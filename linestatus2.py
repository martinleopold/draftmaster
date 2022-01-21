# check setting RTS, DTR and getting CTS, DSR

import serial
import time

ser = serial.Serial('/dev/tty.usbserial-A700CYY0', rtscts = True, dsrdtr=True)  # open serial port

def check(c=True):
    return '☒' if c == True else '☐'

while True:
    print(f'set: RTS {check(ser.rts)} DTR {check(ser.dtr)}    get: CTS {check(ser.cts)} DSR {check(ser.dsr)}')
    time.sleep(0.5)
    ser.rts = not ser.rts
    ser.dtr = not ser.dtr
