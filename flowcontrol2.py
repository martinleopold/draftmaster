# check hardwire flow control
# with loopback cable (RX + TX, RTS + CTS, DSR + DTR)
# rts/cts flow control by pyserial

import serial
import time
from threading import Thread 

ser = serial.Serial('/dev/tty.usbserial-A700CYY0', rtscts = True, dsrdtr=False)  # open serial port

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
    while True:
        print('read')
        print(f'   buffer {ser.in_waiting}')
        read()
        # time.sleep(0.1)

def write_loop():
    while True:
        print('write')
        write(2)
        # time.sleep(0.1)


t1 = Thread(target = read_loop)
t2 = Thread(target = write_loop)
t1.start()
t2.start()
t1.join()
exit()

