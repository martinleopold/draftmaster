# check hardwire flow control
# with two serial interfaces + crossover cable
# rts/cts flow control by pyserial

import serial
import time
from threading import Thread 
import signal

DEV1 = '/dev/tty.usbserial-A700CYY0' # reader
DEV2 = '' # writer

DRY_RUN = True

if not DRY_RUN:
    ser1 = serial.Serial(DEV1, rtscts = True, dsrdtr = False) # reader
    ser2 = serial.Serial(DEV2, rtscts = True, dsrdtr = False) # writer

c = 0 # global counter

def write(n = 1):
    global c
    if n == 1: 
        print(f'   sent {c+1}')
    elif n > 1: 
        print(f'   sent {c+1}–{c+n}')
    for i in range(n):
        c += 1
        if not DRY_RUN:
            ser2.write(f'{c}\n'.encode('utf-8'))
            ser2.flush()

def read():
    if not DRY_RUN:
        data = ser1.read_until()[:-1].decode('utf-8')
    print(f'   recv {data}')
    return data

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

def quit(sig, frame):
    exit()

signal.signal(signal.SIGINT, quit)

t1 = Thread(target = read_loop, daemon = True)
t2 = Thread(target = write_loop, daemon = True)
t1.start()
t2.start()
t1.join()
