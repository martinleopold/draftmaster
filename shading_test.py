from draftmaster import *
import draftmaster as dm

dm._debug = True
# dm._dry = True

P = 20 # pen thickness in plotter units (1 mm = 40 units)

def lines(shading_percent):
    '''lines per unit length to stroke to achieve shading percentage'''
    return int( shading_percent / (100/P) )

def spacing(shading_percent):
    '''spacing of lines to achieve shading percentage'''
    l = lines(shading_percent)
    if l == 0: return 600
    return int( 400 / l )

open('/dev/tty.usbserial-A700CYY0')
IN()
SP(1)
offset = -15.5 * 400 # offset to center
for i in range(21): # 0 .. 20
    position = int(i * (400 + 200) + offset)
    shading = i * 5
    spacing_ = spacing(shading)
    print(f'step {i}:  position={position}  shading={shading}%  spacing={spacing_}')
    PA(position-200, 0-200)
    if i > 0:
        FT(3, spacing_, 45) # parallel lines (type, pacing, angle)
        RR(400, 400) # fill rectangle relative
    ER(400, 400) # edge rectangle relative
SP(0)
close()