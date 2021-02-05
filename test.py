from functools import partial
import serial
from draftmaster import *

ser = serial.Serial('/dev/tty.usbserial-A700CYY0', rtscts=True, dsrdtr=True)
print(ser.name)

def write(str):
    ser.write(str.encode('ASCII'))

def read():
    res = ser.read_until(b'\r')
    res = res[:-1].decode('ASCII')
    return res

write(IN())

write(OA())
print(f'OA: {read()}')

write(OC())
print(f'OC: {read()}')

write(OE())
print(f'OE: {read()}')

write(OF())
print(f'OF: {read()}')

write(OG())
print(f'OG: {read()}')

write(OI())
print(f'OI: {read()}')

write(OL())
print(f'OL: {read()}')

write(OO())
print(f'OO: {read()}')

write(OS())
print(f'OS: {read()}')

write(OT())
print(f'OT: {read()}')

write(OH())
print(f'OH: {read()}')

write(OP())
print(f'OP: {read()}')

write(OW())
print(f'OW: {read()}')

write(OK())
print(f'OK: {read()}')

write(OD())
print(f'OD: {read()}')

write(ESC_A())
print(f'ESC.A: {read()}')

write(ESC_B())
print(f'ESC.B: {read()}')

write(ESC_E())
print(f'ESC.E: {read()}')

write(ESC_L())
print(f'ESC.L: {read()}')

write(ESC_O())
print(f'ESC.O: {read()}')

for n in range(7):
    write(ESC_S(n))
    print(f'ESC.S{n}: {read()}')

ser.close()


# ser.write('hello')
# ser.read() # read one byte
# ser.readuntil


