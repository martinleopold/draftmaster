'''
check flow control support
'''

import draftmaster as dm
import termios

# USE_XONXOFF = True

dm.open('/dev/tty.usbserial-A700CYY0', rtscts=False, xonxoff=True)
# print(dir(dm._ser))

dm.set_read_timeout(5)

def print_flags():
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
# print_flags()



# -> dtr/dsr is probably not supported on posix (linux/macos)
# win source code of pyserial has code for it
# -> xon / xoff seems to be available

# if USE_XONXOFF:
#     dm.ESC_P(1) # set xon/xoff handshake mode (mode 1)
# else:
#     dm.ESC_P(3) # hardwire (mode 3)

# dm.ESC_P(1) # set xon/xoff handshake mode (mode 1) with some default values

dm.ESC_P(1) # set hardwire defaults
# dm.ESC_P(0) # set no handshake defaults
dm.ESC_I('', '', 17) # xon trigger character 17
dm.ESC_N('', 19) # xoff trigger character 19
# dm.ESC_M()

# dm._ser.xonxoff = True

dm.ESC_L()
bs = dm.read() # buffer size
print(f'buffer size: {bs}')

dm.ESC_E()
ee = dm.read() # buffer size
print(f'extended error: {ee}')

dm.IN()

dm.OP() # output P1 and P2
op = dm.read()
print(f'p1 and p2: {op}')

# dm.close()
# exit()


cc=0 # cycle count

# move around the P1, P2 box, then go to origin
def cycle():
    global cc
    dm.PD(op[0], op[1]) # P1
    dm.PD(op[0], op[3]) # P1X, P2Y
    dm.PD(op[2], op[3]) # P2
    dm.PD(op[2], op[1]) # P2X, P1Y
    dm.PD(0, 0)
    cc += 1

def cycles(n=1):
    for i in range(n):
        cycle()
        if i % 100 == 0:
            dm.ESC_B()
            b = dm.read()
        print(f'cycles: {cc}; points: {cc*5}; plotter buffer: {b}/{bs}')

cycles(1000);

dm.close(1)