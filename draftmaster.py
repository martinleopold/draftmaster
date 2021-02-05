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
    # See page 3-14
    '''DF, Default
    USE: Set certain graphics functions to their predefined default settings. Use this instruction to return the plotter to a known state while maintaining the current locations of P1 and P2. When you use DF at the beginning of a program, unwanted graphics parameters such as character size, slant, or scaling are not inherited from another program.
    '''
    return _cmd('DF;')

def IN(partial=False):
    # See page 3-17
    '''IN, Initialize
    USE: Resets most plotter functions to their default settings. Use this instruction to return the plotter to a known state and to cancel settings that may have been changed by a previous program.
    '''
    if partial:
        return _cmd('IN-1;')
    else:
        return _cmd('IN;')

def IP(p1x=None, p1y=None, p2x=None, p2y=None):
    # See page 3-19
    '''IP, Input P1 and P2
    USE: Allows you to establish new or default locations for the scaling points P1 and P2. P1 and P2 are used by the scaling instruction (SC) to establish user-unit scaling. The IP instruction is often used to ensure that a plot is always the same size, regardless of where P1 and P2 might have been set from the front panel or the size of media loaded in the plotter. This instruction can also be used in advanced techniques such as plotting mirror images, enlarging/reducing plots, and enlarging/reducing relative character size or direction (refer to Chapters 7 and 9).
    '''
    if p1x == None:
        return _cmd('IP;')
    elif p2x == None:
        return _cmd(f'IP{p1x},{p1y};')
    else:
        return _cmd(f'IP{p1x},{p1y},{p2x},{p2y};')

def SC(xmin=None, xmax_xfactor=None, ymin=None, ymax_yfactor=None, type=None, left=None, bottom=None):
    # See page 3-21
    '''SC, Scale
    USE: Establishes a user-unit coordinate system by mapping user-defined coordinate values onto the scaling points P1 and P2. Thus, you can plot in units convenient to your application. In addition, you can use this instruction to establish automatic isotropic scaling or to relocate the origin and set a specific ratio of plotter units to user units. For a discussion of the basic concept of scaling, refer to Scaling in Chapter 2.
    '''
    if xmin == None:
        return _cmd('SC;')
    elif type == None:
        return _cmd(f'SC{xmin},{xmax_xfactor},{ymin},{ymax_yfactor};')
    elif left == None:
        return _cmd(f'SC{xmin},{xmax_xfactor},{ymin},{ymax_yfactor},{type};')
    else:
        return _cmd(f'SC{xmin},{xmax_xfactor},{ymin},{ymax_yfactor},{type},{left},{bottom};')

# Chapter 4: Drawing Lines and Rectangles

def EA(x, y):
    # See page 4-7
    '''EA, Edge Rectangle Absolute
    USE: Defines and outline a rectangle using absolute coordinates. Use the EA instruction to create charts that require rectangles; for example, bar charts, flow charts, and organization charts.
    '''
    return _cmd(f'EA{x},{y};')

def ER(x, y):
    # See page 4-9
    '''ER, Edge Rectangle Relative
    USE: Defines and outlines a rectangle using relative coordinates. Use ER to create charts that require rectangles; for example, bar charts, flow charts, and organization charts.
    '''
    return _cmd(f'ER{x},{y};')

def PA(x=None, y=None):
    # See page 4-11
    '''PA, Plot Absolute
    USE: Establishes absolute plotting and moves the pen to the specified absolute coordinates using the current pen position.
    '''
    if x == None:
        return _cmd('PA;')
    else:
        return _cmd(f'PA{x},{y};')

def PD(x=None, y=None):
    # See page 4-12
    '''PD, Pen Down
    USE: Lowers the pen onto the writing surface for drawing.
    '''
    if x == None:
        return _cmd('PD;')
    else:
        return _cmd(f'PD{x},{y};')

def PR(x=None, y=None):
    # See page 4-14
    '''PR, Plot Relative
    USE: Establishes relative plotting and moves the pen to specified points, each sucessive move relative to the current pen location.
    '''
    if x == None:
        return _cmd('PR;')
    else:
        return _cmd(f'PR{x},{y};')

def PU(x=None, y=None):
    # See page 4-16
    '''PU, Pen Up
    USE: Raises the pen from the plotting surface. Use this instruction to move the pen to the beginning of the next line.
    '''
    if x == None:
        return _cmd('PU;')
    else:
        return _cmd(f'PU{x},{y};')

def SP(pen_number=None):
    # See page 4-17
    '''SP, Select Pen
    USE: Loads specified pen into the pen holder or returns the current pen to the carousel. Use the SP instruction to change pen colors or widths during a plot. At the end of every program, use SP to return the pen to the carousel.
    '''
    if pen_number == None:
        return _cmd('SP;')
    else:
        return _cmd(f'SP{pen_number};')

# Part II – Advanced Plotting
# Chapter 5: Enhancing Your Plots

def FT(type=None, spacing=None, angle=None):
    # See page 5-6
    '''FT, Fill Type
    USE: Selects the shading pattern used to fill polygons (FP), rectangles (RA or RR), or wedges (WG). Use this instruction to enhance plots with solid fill, parallel lines (hatching), cross-hatching, or a fill pattern you designed using the user-defined fill type (UF) instruction.
    '''
    if type == None:
        return _cmd('FT;')
    elif spacing == None:
        return _cmd(f'FT{type};')
    elif angle == None:
        return _cmd(f'FT{type},{spacing};')
    else:
        return _cmd(f'FT{type},{spacing},{angle};')

def LT():
    # See page 5-9
    '''LT, Line Type
    USE: 
    TODO
    '''
    return _cmd('XY;')

# Chapter 6: Drawing Circles, Arcs, and Wedges

# Chapter 7: Labeling Your Plots

def LB(string, terminator = chr(3)):
    '''LB, Label
    TODO
    '''
    return _cmd(string + terminator)

# Chapter 8: Drawing Polygons and Using the Polygon Buffer

# Chapter 9: Changing Picture Area and Orientation

def OH():
    '''OH, Output Hard-Clip Limits
    Outputs the X,Y coordinates of the current hard-clip limits. Use this instruction to determine the plotter unit dimensions of the area in which plotting can occur.
    '''
    return _cmd('OH;')

def OP():
    '''OP, Output P1 and P2
    Outputs the X,Y coordinates (in plotter units) of the current scaling points P1 and P2. Use this instruction to determine the numeric coordinates of P1 and P2 when they have been set manually, and to help compute the number of plotter units per user unit when scaling is on. This instruction can also be used with the input (IW) instruction to programmatically set the window to P1 and P2.
    '''
    return _cmd('OP;')

def OW():
    '''OW, Output Window
    Outputs the X,Y coordinates of the lower-left and upper-right corners of the window area in which plotting can occur. This instruction is especially useful when the window area (defined by IW) extends beyond the hard-clip limits;
    '''
    return _cmd('OW;')

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


def OK():
    # page 10-17
    '''OK, Output Key
    Outputs a number that indicates which, if any, of the front-panel function keys has been pressed. Use this instruction in conjunction with the WD instruction when designing interactive programs.
    '''
    return _cmd('OK;')

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

def OD():
    # page 11-8
    '''OD, Output Digitized Point and Pen Status
    Outputs the X,Y coordinates and up/down pen position associated with the last digitized point. Use this instruction  after the DP instruction to return the coordinates of the digitized point to your computer.
    '''
    return _cmd('OD;')

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

def ESC_A():
    # page 15-7
    '''ESC.A, Output Identification
    USE: Outputs the plotter's model number and firmware revision level.
    '''
    return _cmd('\x1b.A');

def ESC_B():
    # page 15-8
    '''ESC.B, Output Buffer Space
    USE: Outputs the plotter's currently available logical I/O buffer space.
    '''
    return _cmd('\x1b.B');

def ESC_E():
    # page 15-8
    '''ESC.E, Output Extended Error
    USE: Outputs the error number for any I/O error related to device-control instructions and clears the error message from the front-panel display. Use this instruction when debugging a program to determine which errors have occured (if any). Additionally, if you are using the RS-232-C interface, you can use ESC.E with ESC.@ to do block I/O error checking.
    '''
    return _cmd('\x1b.E');

def ESC_J():
    # page 15-11
    '''ESC.J, Abort Device-Control
    USE: Aborts any device-control instruction that may be partially decoded or executed. Use this instruction in an initialization sequence when you first access the plotter.
    '''
    return _cmd('\x1b.J');

def ESC_K():
    # page 15-12
    '''ESC.K, Abort Graphics
    Aborts any partially decoded HP-GL instruction and discards remaining instructions in the I/O, pen sort, bidirectional, and vector buffers. Use this instruction as part of an initialization sequence when starting a new program or to terminate plotting of HP-GL instructions in the buffer.
    '''
    return _cmd('\x1b.K');

def ESC_L():
    # page 15-13
    '''ESC.L, Output Buffer Size When Empty
    Outputs the size (in bytes) of the logical I/O buffer. The response is not transmitted by the plotter until the buffer is empty.
    '''
    return _cmd('\x1b.L');

def ESC_O():
    # page 15-14
    '''ESC.O, Output Extended Status
    Outputs the plotter's extended status. Use this instruction to obtain information about the current operating status of the plotter.
    '''
    return _cmd('\x1b.O');

# def ESC_Q(): TODO

def ESC_R():
    # page 15-19
    '''ESC.R, Reset
    Resets certain I/O conditions to power-up default states. Use this instruction to establish known conditions when starting a new plot.
    '''
    return _cmd('\x1b.R');

def ESC_S(n):
    # page 15-20
    '''ESC.S, Output Configurable Memory Size
    Outputs the total memory size of user-definable RAM, or the memory space available in one of its five buffers: the physical I/O buffer, polygon buffer, downloadable character buffer, vector buffer, and pen sort buffer. Use this instruction to determine how much memory is currently allocated to each buffer or to confirm the allocation performed by GM, ESC.T, or ESC.R.
    '''
    return _cmd(f'\x1b.S{n}:');

# Chapter 16: Interfacing and Handshaking



# Make all those uppercase commands available as lowercase as well
def _add_lowercase():
    g = globals()
    cmds = list( filter(lambda g: len(g) == 2 and g.isupper(), globals()) )
    for cmd in cmds:
        g[cmd.lower()] = g[cmd]
_add_lowercase()