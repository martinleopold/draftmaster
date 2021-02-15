from draftmaster import *
# import draftmaster as dm

LABEL = '(#7) 2021-02-15'

open('/dev/tty.usbserial-A700CYY0')
IN()
OH() # output hard clip limits
oh = read()
print(f'hard clip limits: {oh}')

bottom_left = oh[:2]
print(f'bottom left: {bottom_left}')

SI(0.1425, 0.1875) # label size (half of default)
SP(1)
PA(*bottom_left)
LB(LABEL)
SP(0)
close()
