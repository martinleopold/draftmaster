'''
check flow control support
'''

import draftmaster as dm
import termios

dm.open('/dev/tty.usbserial-A700CYY0')
# print(dir(dm._ser))

[iflag, oflag, cflag, lflag, ispeed, ospeed, cc] = termios.tcgetattr(dm._ser.fd)
# print(cc)

print(dir(termios))

print(termios.TIOCM_DSR)
print(termios.TIOCM_DTR)
print(termios.VMIN)
print(termios.VTIME)
print(termios.CRTSCTS)
# print(termios.CNEW_RTSCTS)

print(termios.IXANY)
print(termios.IXON)
print(termios.IXOFF)

# -> dtr/dsr is probably not supported on posix (linux/macos)
# win source code of pyserial has code for it

# -> xon / xoff seems to be available