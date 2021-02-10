from draftmaster import *
import draftmaster as dm

open('/dev/tty.usbserial-A700CYY0')
IN()
SP(1)
FT() # solid bidirectional
PA(0,0)
WG(4072,0,360)
CI(4072)
SP(0)
input("Press Enter to continue...")
close()
