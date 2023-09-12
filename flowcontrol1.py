# check hardwire flow control
# with loopback cable (RX + TX, RTS + CTS, DSR + DTR)
# rts/cts flow control implemented manually

import serial
import time

ser = serial.Serial('/dev/tty.usbserial-A700CYY0', rtscts = False, dsrdtr=False)  # open serial port

buffer_high = 100
buffer_low = 50

c = 0 # global counter

def write(n = 1):
    global c
    if n == 1: 
        print(f'   sent {c+1}')
    elif n > 1: 
        print(f'   sent {c+1}–{c+n}')
    for i in range(n):
        c += 1
        ser.write(f'{c}\n'.encode('utf-8'))
        # ser.flush()

def read():
    data = ser.read_until()[:-1].decode('utf-8')
    print(f'   recv {data}')
    return data

def check(c=True):
    return '☒' if c == True else '☐'


def read_loop():
    print('read')
    print(f'   buffer {ser.in_waiting}')
    if ser.in_waiting >= buffer_high:
        ser.rts = False
    elif ser.in_waiting <= buffer_low:
        ser.rts = True
    read()

def write_loop():
    if ser.cts:
        print('write')
        write(10)

while True:
    # print(f'set: RTS {check(ser.rts)} DTR {check(ser.dtr)}    get: CTS {check(ser.cts)} DSR {check(ser.dsr)}')
    #time.sleep(0.5)
    # ser.rts = not ser.rts
    # ser.dtr = not ser.dtr
    write_loop()
    read_loop()
    time.sleep(0.1)
    
