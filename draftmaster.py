# HP GL Instructions (Graphics instructions, output instructions)
# Device Control Instructions

# Numbers accepted: -8 388 608 (-2e23) to 8 388 607 (2e23-1)

# Coordinate System:
# x ... long side of paper
# y ... short side of paper
# origin is bottom left ()+x is right, +y is up)

# Units:
# Plotter Units: 1 pu = 0.025mm or 0.00098 in

def _cmd(str):
    return str

# See page TODO
_hpgl_error_numbers = ['No error', 'Instruction not recognized', 'Wrong number of parameters', 'Out-of range parameter, or illegal character', 'Not used', 'Unknown character set', 'Position overflow (not reported with default E-mask value)', 'Buffer overflow for polygons']

# See page 14-24
_status_bits = ['Pen down', 'P1 or P2 newly established; cleared by OP', 'Digitized point available; cleared by OD', 'Initialized; cleared by OS', 'Ready for data (buffer empty)', 'Error, cleared by OE', 'Request service (always 0 for OS; or 1 for HP-IB serial poll)', 'Not used (always set to "0")']

# Chapter 3: Beginning Your HP-GL Program

def DF():
    '''DF, Default
    USE: Set certain graphics functions to their predefined default settings.
    '''
    return _cmd('DF;')

def IN(partial=False):
    '''IN, Initialize
    USE: Resets most plotter functions to their default settings.
    '''
    if partial:
        return _cmd('IN-1;')
    else:
        return _cmd('IN;')

def IP(p1x, p1y, p2x, p2y):
    '''IP, Input P1 and P2
    TODO
    '''
    return _cmd('IP;')

def SC():
    '''SC, Scale
    TODO
    '''
    return _cmd('SC;')

# Chapter 4: Drawing Lines and Rectangles

def EA(x, y):
    '''EA, Edge Rectangle Absolute
    TODO
    '''
    return _cmd(f'EA{x},{y};')

def ER(x, y):
    '''ER, Edge Rectangle Relative
    TODO
    '''
    return _cmd(f'ER{x},{y};')

def PA(x, y):
    '''PA, Plot Absolute
    TODO
    '''
    return _cmd(f'PA{x},{y};')

def PD(x, y):
    '''PD, Pen Down
    TODO
    '''
    return _cmd(f'PD{x},{y};')

def PR(x, y):
    '''PR, Plot Relative
    TODO
    '''
    return _cmd(f'PR{x},{y};')

def PU(x, y):
    '''PU, Pen Up
    TODO
    '''
    return _cmd(f'PU{x},{y};')

def SP(pen_number=None):
    '''SP, Select Pen
    TODO
    '''
    if pen_number == None:
        return _cmd(f'SP;')
    else:
        return _cmd(f'SP{pen_number};')

# Part II – Advanced Plotting
# Chapter 5: Enhancing Your Plots

# Chapter 6: Drawing Circles, Arcs, and Wedges

# Chapter 7: Labeling Your Plots

def LB(string, terminator = chr(3)):
    '''LB, Label
    TODO
    '''
    return _cmd(string + terminator)

# Chapter 8: Drawing Polygons and Using the Polygon Buffer

# Chapter 9: Changing Picture Area and Orientation

# Chapter 10: Advanced Pen Control and Front-Panel Interaction

def AP(n = None):
    '''AP, Automatic Pen Operations
    USE: Controls automatic pen operations such as returning a pen to the carousel if it has been in the older without drawing for a certain time.
    TODO
    '''
    if n == None:
        return _cmd('AP;')
    else:
        return _cmd(f'AP{n};')

def AS(pen_acceleration = None, pen_number = None):
    '''AS, Acceleration Select
    USE: Sets pen acceleration for one or all pens. The default acceleration is suitable for all recommended pen and media combinations. Slowing the acceleration may improve line quality if you are using heavier than recommended media.
    TODO
    '''
    if pen_acceleration == None:
        return _cmd('AS;')
    elif pen_number == None:
        return _cmd(f'AP{pen_acceleration};')
    else:
        return _cmd(f'AP{pen_acceleration},{pen_number};') 

def CV(n = None):
    '''CV, Curved Line Generator
    USE: Collects vectors (line segments) in the vector buffer so that they can be plotted as a group. This allows the plotter to plot in a continuous motion, rather than stopping and starting at each vector endpoint. As a result, curves appear smoother.
    TODO: is input delay a seperate parameter?
    '''
    if n == None:
        return _cmd('CV;')
    else:
        return _cmd(f'CV{n};')

def FS(pen_force = None, pen_number = None):
    '''FS, Force Select
    USE: Sets pen pressure to the paper for one or all pens. Use this instruction to optimize pen life and line quality for each pen and paper combination.
    TODO
    '''
    if pen_force == None:
        return _cmd('FS;')
    elif pen_number == None:
        return _cmd(f'FS{pen_force};')
    else:
        return _cmd(f'FS{pen_force},{pen_number};')

def NR():
    '''NR, Not Ready
    USE: Programmatically simulates pressing the front-panel View button. However, you cannot take the plotter out of the View state with the NR instruction.
    TODO
    '''
    return _cmd('NR;')

def VS(pen_velocity = None, pen_number = None):
    '''VS, Velocity Select
    USE: Specifies pen speed. Use the instruction to optimize pen life and line quality for each pen and media combination. Create a slightly thicker line on any media by slowing the pen speed.
    TODO
    '''
    if pen_velocity == None:
        return _cmd('VS;')
    elif pen_number == None:
        return _cmd(f'VS{pen_velocity};')
    else:
        return _cmd(f'VS{pen_velocity},{pen_number};')

# Part III – Special Applications
# Chapter 11: Digitizing

# Chapter 12: Rollfeed Instructions and Long-Axis Printing

# Chapter 13: Alternate Character Sets and User-Designed Characters

# Part IV – Interfacing, Handshaking, Output, and Device Control
# Chapter 14: Obtaining Information from the Plotter

def GC(count_number = None):
    '''GC, Group Count
    USE: Assigns a number known as the 'group count,' which is the number that will be output by the OG instruction. The group count is an arbitrary number that you assign at the beginning of a data block in spooling applications (typically in an RS-232-C configuration with a mainframe computer). Use this instruction in conjunction with the OG instruction to monitor the successful transfer of data blocks.
    TODO
    '''
    if count_number == None:
        return _cmd('GC;')
    else:
        return _cmd(f'GC{count_number};')

def IM(E_mask_value = None, S_mask_value = None, P_mask_value = None):
    '''IM, Input Mask
    USE: Controls which HP-GL errors are reported. If you are using an HP-IB interface, you can also use IM to control the conditions that cause an HP-IB service reques or a positive response to a parallel poll.
    TODO
    '''
    if E_mask_value == None:
        return _cmd('IM;')
    elif S_mask_value == None:
        return _cmd(f'IM{E_mask_value};')
    elif P_mask_value == None:
        return _cmd(f'IM{E_mask_value},{S_mask_value};')
    else:
        _cmd(f'IM{E_mask_value},{S_mask_value},{P_mask_value};')

def OA():
    '''OA, Output Actual Pen Status
    USE: Outputs the current pen location (in plotter units) and up/down position. You can use this information to position a label of figure, to determine the parameters of some desired window, or to determine the pen's current location if it has been moved using front-panel Cursor Control buttons.
    TODO
    '''
    return _cmd('OA;')

def OC():
    '''OC, Output Commanded Pen Status
    USE: Outputs the location and up/down position of the last commanded move. Use this instruction to position a label or determine the parameters of an instruction that tried to move the pen beyond the limits of some window. You can also use this instruction when you want to know the pen's location in user units. 
    TODO
    '''
    return _cmd('OC;')

def OE():
    '''OE, Output Error
    USE: Outputs a number corresponding to the type of HP-GL error (if any) received by the plotter after the most recent IN instruction, front-panel reset, or OE instruction. Use this instruction for debugging programs.
    TODO
    '''
    return _cmd('OE;')

def OF():
    '''OF, Output Factors
    USE: Outputs the number of plotter units per millimetre in each axis. This instruction lets you use the plotter with software that needs to know the size of a plotter unit.
    TODO
    '''
    return _cmd('OF;')

def OG():
    '''OG, Output Group Count
    USE: Outputs the data block number of the current group count and whether the escape function has been activated. Use this instruction at the end of a data block in spooling applications, where it is important to know the current data block number and whether the data block has been transferred.
    TODO
    '''
    return _cmd('OG;')

def OI():
    '''OI, Output Identification
    Outputs the plotter's identifying model number. This information is useful in a remote operating configuration (where several plotters are connected to the computer) to determine which plotter model is on-line, or when software needs the plotter's model number.
    TODO
    '''
    return _cmd('OI;')

def OL():
    '''OL, Output Label Length
    Output information about the label contained in the label buffer.
    TODO
    '''
    return _cmd('OL;')

def OO():
    '''OO, Output Options
    Outputs eight option parameters indicating features implemented on the plotter. Some software packages use this feature to determine which plotter capabilities exist.
    TODO
    '''
    return _cmd('OO;')

def OS():
    '''OS, Output Status
    Outputs the decimal value of the status byte. Use this instruction in debugging operations and in digitizing applications.
    TODO
    '''
    return _cmd('OS;')

def OT():
    '''OT, Output Carousel Type
    The OT instruction outputs information on the type of carousel loaded and the stalls occupied.
    TODO
    '''
    return _cmd('OT;')

# Chapter 15: Device-Control Instructions

# Chapter 16: Interfacing and Handshaking



# Make all those uppercase commands available as lowercase as well
def _add_lowercase():
    g = globals()
    cmds = list( filter(lambda g: len(g) == 2 and g.isupper(), globals()) )
    for cmd in cmds:
        g[cmd.lower()] = g[cmd]
_add_lowercase()