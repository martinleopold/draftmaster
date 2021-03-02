# label print number 4 
from draftmaster import *
# import draftmaster as dm

LABEL_TEXT = '(#4) 2021-02-11   r=10.18cm'
LABEL_SIZE = 0.5

open('/dev/tty.usbserial-A700CYY0')
IN()

OH() # output hard clip limits
oh = read()
print(f'hard clip limits: {oh}') # X_LL, Y_LL, X_UR, Y_UR

# Seen as landscape format (because x axis is always parallel to longer paper edge)
bottom_left  = oh[:2]
top_right    = oh[2:]
bottom_right = ( oh[2], oh[1] )
top_left     = ( oh[0], oh[3] )
print(f' bottom left: {bottom_left}')
print(f'bottom right: {bottom_right}')
print(f' bottom left: {top_left}')
print(f'   top right: {top_right}')


SI(0.285*LABEL_SIZE, 0.375*LABEL_SIZE) # label size (half of default)
DI(0, -1) # label direction absolute; seen in landscape orientation this a rotation from the horizontal by 90 deg cw.

SP(1)
PA(*top_left)
LB(LABEL_TEXT)
SP(0)

close()
