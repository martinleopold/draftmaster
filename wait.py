from draftmaster import *
import draftmaster as dm
import time

dm._monitor = True

open('/dev/tty.usbserial-A700CYY0')
IN()
SP(0)
PA(0,0)
CI(4000) # draw circle in the air
SP(0)
# input("Press Enter to continue...")
close()
