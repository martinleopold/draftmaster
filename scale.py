'''
test scaling, setting origin and axis
'''
from draftmaster import *
import draftmaster as dm

open('/dev/tty.usbserial-A700CYY0')

IN()

OH() # output hard clip limits
oh = read()
print(f'hard clip limits: {oh}')

OP() # output P1 and P2
op = read()
print(f'       p1 and p2: {op}')

# edge hard clip limits
SP(1)
PA(*oh[:2])
EA(*oh[2:]) # edge rectangle absolute

SC(0, 500, 500, 0, 1) # scale isotropic, origin is top left, y is down

# draw a square 
PA(0,0)
EA(500,500)

# mark origin
SM('*')
PA(0,0)

SP(0)
close()
