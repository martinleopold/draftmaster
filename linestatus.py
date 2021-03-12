# check status lines: cts, dsr, ri

import serial
import time

ser = serial.Serial('/dev/tty.usbserial-A700CYY0', rtscts = True, dsrdtr=False)  # open serial port

def check(c=True):
    return '☒' if c == True else '☐'

ser.write(b'IN;')

while True:
    print(f'RTS {check(ser.rts)}   DTR {check(ser.dtr)}   CTS {check(ser.cts)}   DSR {check(ser.dsr)}   RI {check(ser.ri)}   CD {check(ser.cd)}')
    ser.write(b'PD-5000,-5000,5000,5000;'*100)
    time.sleep(1)
