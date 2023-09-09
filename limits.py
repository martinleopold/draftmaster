'''Draw hard clip limits, P1, P2 and the origin'''

PORTRAIT = False # Adds RO(90) command
SHOW_CENTERED_AREA = False # Adds commands to translate coords to paper center, shows maximal printable centered area

from draftmaster import *
import draftmaster as dm

open()
IN()

# Rotate plotter coordinate system
if PORTRAIT:
    RO(90)
    IP() # Reset P1 and P2 -> 15 mm (600 units) inside the hard clip limits 
print(f'orientation: {"portrait" if PORTRAIT else "landscape"}')

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

if SHOW_CENTERED_AREA:
    shift = (39-15) * 40 / 2 # 12 mm
    if PORTRAIT:
        # move p1 and p2 to the right
        IP(op[0] + shift, op[1], op[2] + shift, op[3])
    else:
        # move p1 and p2 down
        IP(op[0], op[1] - shift, op[2], op[3] - shift)

    # scale so that old coordinates of p1 and p2 correspond to the new locations
    p1x, p1y, p2x, p2y = op # op are old coordinates of p1 and p2
    SC(p1x, p2x, p1y, p2y) # scale coordinate system
    # SC(p1x, 1, p1y, 1, 2)
    
    SP(1)
    
    # draw maximum area after shift
    if PORTRAIT:
        # coord system shifted to the right by IP/SC (+ shift)
        # left needs to go right (+ shift): total 2 * shift = 24 mm
        # right needs to go back left (- shift): total 0 mm
        bl = ( oh[0] + shift, oh[1] )
        tr = ( oh[2] - shift, oh[3] )
        tl = ( oh[0] + shift, oh[3] )
        br = ( oh[2] - shift, oh[1] )
    else:
        # coord system shifted down by IP/SC (- shift)
        # top needs to go down (- shift): total -2 * shift = -24 mm
        # bottom needs to go up (+ shift): total 0 mm
        bl = ( oh[0], oh[1] + shift )
        tr = ( oh[2], oh[3] - shift )
        tl = ( oh[0], oh[3] - shift )
        br = ( oh[2], oh[1] + shift )
    
    # maximum (centered area)
    PA(*bl)
    EA(*tr)
    
    # mark center
    SM('*')
    PA(0, 0)
    SM()
    
    # diagonals
    PA(*bl)
    PD(*tr)
    PU()
    PA(*tl)
    PD(*br)
    PU()

SP(0)
close()
