from draftmaster import *
import draftmaster as dm

open('/dev/tty.usbserial-A700CYY0')
IN()

SP(1) # pick pen 1
# PT(0.7) # pen thickness (default 0.3)
FT() # solid bidirectional fill
PA(0,0) # center of plottable area
WG(4072,0,360) # filled disc
CI(4072) # circle outline

PA(-7303, -5309) # bottom left corner (landscape format)
SI(0.1425, 0.1875) # label size (half of default)
LB('2021-02-11   r=10.18cm') # plot the label

SP(0) # return pen
close()
