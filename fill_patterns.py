from draftmaster import *
import draftmaster as dm

# PT() # pen thickness
# AS() # acceleration select
# FS() # force select
# VS() # velocity select

dm._debug = True
# dm._dry = True

R = 20 * 40

# # plot no 21)
# open('/dev/tty.usbserial-A700CYY0')
# IN()
# SP(1)
# 
# PA(-70*40, 0)
# FT(1) # solid bidirectional
# WG(R, 0, 360)
# EW(R, 0, 360)
# 
# PA(-25*40, 0)
# FT(2) # solid unidirectional
# WG(R, 0, 360)
# EW(R, 0, 360)
# 
# PA(25*40, 0)
# FT(3) # parallel lines
# WG(R, 0, 360)
# EW(R, 0, 360)
# 
# PA(70*40, 0)
# FT(4) # cross-hatch
# WG(R, 0, 360)
# EW(R, 0, 360)
# 
# SP(0)
# close()

# plot no 22)
open('/dev/tty.usbserial-A700CYY0')
IN()
SP(1)

PA(-115*40, 0)
FT(3, 2*40, 45) # parallel lines (type, pacing, angle)
WG(R, 0, 360)
EW(R, 0, 360)

PA(-70*40, 0)
FT(3, 4*40, 25) # parallel lines
WG(R, 0, 360)
EW(R, 0, 360)

PA(-25*40, 0)
FT(3, 6*40, 80) # parallel lines
WG(R, 0, 360)
EW(R, 0, 360)

PA(25*40, 0)
FT(4, 2*40, 45)  # cross-hatch
WG(R, 0, 360)
EW(R, 0, 360)

PA(70*40, 0)
FT(4, 4*40, 25) # cross-hatch
WG(R, 0, 360)
EW(R, 0, 360)

PA(115*40, 0)
FT(4, 6*40, 80) # cross-hatch
WG(R, 0, 360)
EW(R, 0, 360)

SP(0)
close()
