'''Draw hard clip limits and 0,0'''
from draftmaster import *
import draftmaster as dm

open('/dev/tty.usbserial-A700CYY0')
IN()

OH() # output hard clip limits
oh = read()
print(f'hard clip limits: {oh}')

SP(1)
PA(*oh[:2])
EA(*oh[2:]) # edge rectangle absolute

# mark at the center of the plot
SM('*')
PA(0, 0)
SP(0)
close()
