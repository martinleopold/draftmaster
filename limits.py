'''Draw hard clip limits, P1, P2 and the origin'''
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

SP(1)
PA(*oh[:2])
EA(*oh[2:]) # edge rectangle absolute

# mark at the center of the plot
SM('*')
PA(0, 0)

# mark p1 and p2
p1 = op[:2]
p2 = op[2:]
SM('*')
PA(*p1)
SM()
LO(16) # below and centered
LB('P1')

SM('*')
PA(*p2)
SM()
LO(14) # above and centered
LB('P2')

SP(0)
close()
