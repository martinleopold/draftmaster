'''
testing (buffer?) errors by sucessively drawing more and more points on a circle
result: close command needs to wait for all data to get across
'''
from draftmaster import *
import draftmaster as dm
import math

N = 100
D = 2000

def circle():
    p = []
    for i in range(N):
        a = 2 * math.pi / N * i
        p.append( (int(D * math.cos(a)), int(D * math.sin(a))) )
    return p

points = circle()
first = points[0] 
rest = points[1:]

dm._debug = True
dm._dry = False

open('/dev/tty.usbserial-A700CYY0')
IN()
SP(1) # pick pen 1
PA(0,0) # move to center
PA(*first) # move to first point
for p in rest:
    PD(*p)
PD(*first)
PU()
SP(0)
close(-1) # wait indefinitely
