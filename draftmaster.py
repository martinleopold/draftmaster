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

def _check_args(forms, args):
    '''Check if args correspond to at least one of the allowed forms. If not, a value error is raised.
    Returns an enumeration of arg names and values of the first valid form that was found.
    '''
    arg_names = [ arg_name for arg_name in args if args[arg_name] != None] # List of argument names that were provided
    for required_args in forms:
        if set(arg_names) == set(required_args):
            return [ (arg_name, args[arg_name]) for arg_name in arg_names ] # Return enumeration of arg name and arg value
    raise TypeError(f'Argument error. Args given: {arg_names}. Allowed forms: {", ".join(map(str, forms))}')

def _join_args(args, sep=','):
    '''Takes an enumeration of arg names and values and returns a string of joined arg values'''
    def stringify(val): # support iterables (by joining them)
        if '__iter__' in dir(val): return sep.join(map(str, val))
        return str(val)
    return sep.join( [stringify(arg_value) for _, arg_value in args] )

# Make all those uppercase commands available as lowercase as well
def _add_lowercase():
    from keyword import kwlist
    g = globals()
    cmds = list( filter(lambda g: len(g) == 2 and g.isupper(), g) )
    for cmd in cmds:
        cmd_new = cmd.lower()
        g[cmd_new] = g[cmd]
        # add trailing _ if the new command name is a reserved word (e.g. in, if, is, or)
        if cmd_new in kwlist: g[cmd_new + '_'] = g[cmd]



# See page 14-15
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
    _check_args([
        [],
        ['partial']
    ], locals())
    if partial:
        return _cmd('IN-1;')
    else:
        return _cmd('IN;')

def IP(p1x=None, p1y=None, p2x=None, p2y=None):
    # See page 3-19
    '''IP, Input P1 and P2
    USE: Allows you to establish new or default locations for the scaling points P1 and P2. P1 and P2 are used by the scaling instruction (SC) to establish user-unit scaling. The IP instruction is often used to ensure that a plot is always the same size, regardless of where P1 and P2 might have been set from the front panel or the size of media loaded in the plotter. This instruction can also be used in advanced techniques such as plotting mirror images, enlarging/reducing plots, and enlarging/reducing relative character size or direction (refer to Chapters 7 and 9).
    '''
    args = _check_args([
        [],
        ['p1x', 'p1y'],
        ['p1x', 'p1y', 'p2x', 'p2y']
    ], locals())
    args = _join_args(args)
    return _cmd(f'IP{args};')

def SC(xmin=None, xmax_xfactor=None, ymin=None, ymax_yfactor=None, type=None, left=None, bottom=None):
    # See page 3-21
    '''SC, Scale
    USE: Establishes a user-unit coordinate system by mapping user-defined coordinate values onto the scaling points P1 and P2. Thus, you can plot in units convenient to your application. In addition, you can use this instruction to establish automatic isotropic scaling or to relocate the origin and set a specific ratio of plotter units to user units. For a discussion of the basic concept of scaling, refer to Scaling in Chapter 2.
    '''
    args = _check_args([
        [],
        ['xmin', 'xmax_xfactor', 'ymin', 'ymax_yfactor'],
        ['xmin', 'xmax_xfactor', 'ymin', 'ymax_yfactor', 'type'],
        ['xmin', 'xmax_xfactor', 'ymin', 'ymax_yfactor', 'type', 'left', 'bottom']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SC{args};')

# Chapter 4: Drawing Lines and Rectangles

def EA(x, y):
    # See page 4-7
    '''EA, Edge Rectangle Absolute
    USE: Defines and outline a rectangle using absolute coordinates. Use the EA instruction to create charts that require rectangles; for example, bar charts, flow charts, and organization charts.
    '''
    _check_args([
        ['x', 'y']
    ], locals())
    return _cmd(f'EA{x},{y};')

def ER(x, y):
    # See page 4-9
    '''ER, Edge Rectangle Relative
    USE: Defines and outlines a rectangle using relative coordinates. Use ER to create charts that require rectangles; for example, bar charts, flow charts, and organization charts.
    '''
    _check_args([
        ['x', 'y']
    ], locals())
    return _cmd(f'ER{x},{y};')

def PA(*x_y):
    # See page 4-11
    '''PA, Plot Absolute
    USE: Establishes absolute plotting and moves the pen to the specified absolute coordinates using the current pen position.
    '''
    coord_list = ",".join( map(str, x_y) )
    return _cmd(f'PA{coord_list};')

def PD(*x_y):
    # See page 4-12
    '''PD, Pen Down
    USE: Lowers the pen onto the writing surface for drawing.
    '''
    coord_list = ",".join( map(str, x_y) )
    return _cmd(f'PD{coord_list};')

def PR(*x_y):
    # See page 4-14
    '''PR, Plot Relative
    USE: Establishes relative plotting and moves the pen to specified points, each sucessive move relative to the current pen location.
    '''
    coord_list = ",".join( map(str, x_y) )
    return _cmd(f'PR{coord_list};')

def PU(*x_y):
    # See page 4-16
    '''PU, Pen Up
    USE: Raises the pen from the plotting surface. Use this instruction to move the pen to the beginning of the next line.
    '''
    coord_list = ",".join( map(str, x_y) )
    return _cmd(f'PU{coord_list};')

def SP(pen_number=None):
    # See page 4-17
    '''SP, Select Pen
    USE: Loads specified pen into the pen holder or returns the current pen to the carousel. Use the SP instruction to change pen colors or widths during a plot. At the end of every program, use SP to return the pen to the carousel.
    '''
    args = _check_args([
        [],
        ['pen_number']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SP{args};')

# Part II – Advanced Plotting
# Chapter 5: Enhancing Your Plots

def FT(type=None, spacing=None, angle=None):
    # See page 5-6
    '''FT, Fill Type
    USE: Selects the shading pattern used to fill polygons (FP), rectangles (RA or RR), or wedges (WG). Use this instruction to enhance plots with solid fill, parallel lines (hatching), cross-hatching, or a fill pattern you designed using the user-defined fill type (UF) instruction.
    '''
    args = _check_args([
        [],
        ['type'],
        ['type', 'spacing'],
        ['type', 'spacing', 'angle'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'FT{args};')

def LT(pattern_number=None, pattern_length=None):
    # See page 5-9
    '''LT, Line Type
    USE: Specifies the line pattern to be used when drawing lnies and nonsolid fill types. Use LT to emphasize or de-emphasize plotted lines and shapes.
    '''
    args = _check_args([
        [],
        ['pattern_number'],
        ['pattern_number', 'pattern_length']
    ], locals())
    args = _join_args(args)
    return _cmd(f'LT{args};')

def PT(pen_thickness=None):
    # See page 5-12
    '''PT, Pen Thickness
    USE: Determines the spacing between the parallel lines in solid fill patterns according to the pen tip thickness.
    '''
    args = _check_args([
        [],
        ['pen_thickness'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'PT{args};')

def RA(x, y):
    # See page 5-14
    '''RA, Fill Rectangle Absolute
    USE: Deines and fills a rectangle using absolute coordinates. Use this instruction to fill rectangular shapes in bar charts, logos, and other plots. To outline a rectangle using absolute coordinates, use the EA instruction.
    '''
    _check_args([
        ['x', 'y']
    ], locals())
    return _cmd(f'RA{x},{y};')

def RR(x, y):
    # See page 5-16
    '''RA, Fill Rectangle Relative
    USE: Deines and fills a rectangle using relative coordinates. Use this instruction to fill rectangular shapes in bar charts, logos, and other plots. To outline a rectangle using relative coordinates, use the ER instruction.
    '''
    _check_args([
        ['x', 'y']
    ], locals())
    return _cmd(f'RR{x},{y};')

def SM(character=None, character2=None):
    # See page 5-18
    '''SM, Symbol Mode
    USE: Draws the specified symbol at each X,Y coordinate point. Use symbol mode to create scattergrams, indicate points on geometric drawings, and differentiate data points on multi-line graphs.
    '''
    args = _check_args([
        [],
        ['character'],
        ['character', 'character2']
    ], locals())
    if (character != None and len(character) != 1):
        raise ValueError('Only a single character is allowed for parameter character')
    if (character2 != None and len(character2) != 1):
        raise ValueError('Only a single character is allowed for parameter character2')
    args = _join_args(args)
    return _cmd(f'SM{args};')

def TL(positive_tick=None, negative_tick=None):
    # See page 5-20
    '''TL, Tick Length
    USE: Specifies the length of the tick marks produced by the tick instructions (XT and YT). Use this instruction to adjust both the positive and negative portions of tick marks, and to establish a tick length for drawing grids.
    '''
    args = _check_args([
        [],
        ['positive_tick'],
        ['positive_tick', 'negative_tick']
    ], locals())
    args = _join_args(args)
    return _cmd(f'TL{args};')

def UF(gap1=None, gap2=None, gap3=None, gap4=None, gap5=None, gap6=None, gap7=None, gap8=None, gap9=None, gap10=None, gap11=None, gap12=None, gap13=None, gap14=None, gap15=None, gap16=None, gap17=None, gap18=None, gap19=None, gap20=None):
    # See page 5-23
    '''UF, User-Defined Fill Type
    USE: Defines a fill pattern composed of 'gaps' between parallel lines such as a semilog or candy-stripe effect. All fil instructions (FP, RA, RR, and WG) can use this fill type.
    '''
    args = _check_args([
        [],
        ['gap1'],
        ['gap1', 'gap2'],
        ['gap1', 'gap2', 'gap3'],
        ['gap1', 'gap2', 'gap3'],
        ['gap1', 'gap2', 'gap3', 'gap4'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15', 'gap16'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15', 'gap16', 'gap17'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15', 'gap16', 'gap17', 'gap18'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15', 'gap16', 'gap17', 'gap18', 'gap19'],
        ['gap1', 'gap2', 'gap3', 'gap4', 'gap5', 'gap6', 'gap7', 'gap8', 'gap9', 'gap10', 'gap11', 'gap12', 'gap13', 'gap14', 'gap15', 'gap16', 'gap17', 'gap18', 'gap19', 'gap20']
    ], locals())
    args = _join_args(args)
    return _cmd(f'UF{args};')

def XT():
    # See page 5-28
    '''XT, X-Tick
    USE: Draws a vertical (parallel to the Y-axis) tick at the current pen location. Use this instruction to draw vertical tick marks on axes, grid lines, or lines centered on or starting at the current pen location.
    '''
    return _cmd('XT;')

def YT():
    # See page 5-29
    '''YT, Y-Tick
    USE: Draws a horizontal (parallel to the X-axis) tick at the current pen location. Use this instruction to draw horizontal tick marks on axes, grid lines, or lines centered on or starting at the current pen location.
    '''
    return _cmd('YT;')

# Chapter 6: Drawing Circles, Arcs, and Wedges

def AA(x, y, arc_angle, chord_tolerance=None):
    # See page 6-7
    # Corrected chord_angle parameter to chord_tolerance
    '''AA, Arc Absolute
    USE: Draws an arc, using absolute coordinates, that starts at the current pen location and uses the specified center point.
    '''
    args = _check_args([
        ['x', 'y', 'arc_angle'],
        ['x', 'y', 'arc_angle', 'chord_tolerance']
    ], locals())
    args = _join_args(args)
    return _cmd(f'AA{args};')

def AR(x, y, arc_angle, chord_tolerance=None):
    # See page 6-9
    # Corrected chord_angle parameter to chord_tolerance
    '''AR, Arc Relative
    USE: Draws an arc, using relative coordinates, that starts at the current pen location and uses the specified center point.
    '''
    args = _check_args([
        ['x', 'y', 'arc_angle'],
        ['x', 'y', 'arc_angle', 'chord_tolerance']
    ], locals())
    args = _join_args(args)
    return _cmd(f'AR{args};')

def CI(radius, chord_tolerance=None):
    # See page 6-11
    '''CI, Circle
    USE: Draws a circle using the specified radius and chord tolerance. If you want a filled circle, refer to the WG or PM instruction.
    '''
    args = _check_args([
        ['radius'],
        ['radius', 'chord_tolerance']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CI{args};')

def CT(n=None):
    # See page 6-15
    '''CT, Chord Tolerance
    USE: Determines whether the chord tolerance parameter of the CI, AA, AR, EW, WG instructions is interpreted as a chord angle in degrees or as a deviation distance in current units.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CT{args};')

def EW(radius, start_angle, sweep_angle, chord_tolerance=None):
    # See page 6-17
    # Corrected chord_angle parameter to chord_tolerance
    '''EW, Edge Wedge
    USE: Outlines any wedge. Use this instruction to draw sectors of pie charts.
    '''
    args = _check_args([
        ['radius', 'start_angle', 'sweep_angle'],
        ['radius', 'start_angle', 'sweep_angle', 'chord_tolerance'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'EW{args};')

def WG(radius, start_angle, sweep_angle, chord_tolerance=None):
    # See page 6-21
    # Corrected chord_angle parameter to chord_tolerance
    '''WG, Fill Wedge
    USE: Defines and fills any wedge. Use this instruction to draw filled sectors of a pie chart.
    '''
    args = _check_args([
        ['radius', 'start_angle', 'sweep_angle'],
        ['radius', 'start_angle', 'sweep_angle', 'chord_tolerance'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'WG{args};')

# Chapter 7: Labeling Your Plots

def BL(cc=None, terminator='\x03'):
    # See page 7-11
    '''BL, Buffer Label
    USE: Stores a label in the label buffer. You can then use the output length (OL) instruction to determine its space requirement prior to drawing it. Or, you can use the plot buffered label (PB) instruction to repeatedly plot this label.
    '''
    args = _check_args([
        ['terminator'],
        ['cc', 'terminator'],
    ], locals())
    args = _join_args(args, sep='')
    if len(args) > 150:
        raise ValueError('cc can be up to 150 including control characters and the label terminator')
    return _cmd(f'BL{args}') # Note this command doesn't end with ';'

def CP(spaces=None, lines=None):
    # See page 7-13
    '''CP, Character Plot
    USE: Moves the pen the specified number of character plot cells from the current pen location (e.g., to indent or center a label).
    '''
    args = _check_args([
        [],
        ['spaces', 'lines'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'CP{args};')

def DI(run=None, rise=None):
    # See page 7-16
    '''DI, Direction Absolute
    USE: Specifies the direction in which labels are drawn, independent of P1 and P2 settings. Use this instruction to change lebeling direction when you are labeling curves in line charts, schematic drawings, blueprints, and survey boundaries.
    '''
    args = _check_args([
        [],
        ['run', 'rise'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'DI{args};')

def DR(run=None, rise=None):
    # See page 7-22
    '''DR, Relative Direction
    USE: Specifies the direction in which labels are drawn, relative to the scaling points P1 and P2. Label direction is adjusted wehen P1 and P2 change so that labels maintain the same relationship to the plotted data. Use DI if you want label direction to be independent of P1 and P2.
    '''
    args = _check_args([
        [],
        ['run', 'rise'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'DR{args};')

def DT(label_terminator=None):
    # See page 7-27
    '''DT, Define Label Terminator
    USE: Specifies the character to be used as the label terminator. Use this instruction to define a new label terminator if your computer cannot use the default label terminator (ETX, decimal code 3).
    '''
    args = _check_args([
        [],
        ['label_terminator'],
    ], locals())
    args = _join_args(args)
    if len(args) not in [0, 1]:
        raise ValueError('label_terminator must be exactly one character')
    if args in [chr(0), chr(5), chr(10), chr(27), ';']:
        raise ValueError('label_terminator cannot be NULL, LF, ESC, ENQ and ;')
    return _cmd(f'DT{args};')

def DV(n=None):
    # See page 7-29
    '''DV, Direction Vertical
    USE: Specifies vertical mode as the direction for subsequent labels. Use this instruction to 'stack' horizontal characters in a column. This is especially useful when using the Kanji character set (refer to Appendix D).
    '''
    args = _check_args([
        [],
        ['n'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'DV{args};')

def ES(spaces=None, lines=None):
    # See page 7-31
    '''ES, Extra Space
    USE: Adjusts space between characters and lines of labels without affecting character size.
    '''
    args = _check_args([
        [],
        ['spaces'],
        ['spaces', 'lines']
    ], locals())
    args = _join_args(args)
    return _cmd(f'ES{args};')
    
def LB(cc, terminator='\x03'):
    # See page 7-33
    '''LB, Label
    USE: Plots text using the currently defined character set.
    '''
    args = _check_args([
        ['cc', 'terminator'],
    ], locals())
    args = _join_args(args, '')
    if len(args) > 150:
        raise ValueError('cc can be up to 150 including control characters and the label terminator')
    return _cmd(f'LB{args}') # Note this command doesn't end with ';'

def LO(position_number=None):
    # See page 7-35
    '''LO, Label origin
    USE: Positions labels relative to current pen location. Use LO to center, left justify, or right justify labels. The label can be drawn above or below the current pen location and can also be offset by an amount equal to 1/2 the character's width and height.
    '''
    args = _check_args([
        [],
        ['position_number']
    ], locals())
    args = _join_args(args)
    return _cmd(f'LO{args};')

def PB():
    # See page 7-38
    '''PB, Print Buffered Label
    USE: Prints the contents of the label buffer.
    '''
    return _cmd('PB;')

def SI(width=None, height=None):
    # See page 7-39
    '''SI, Absolute Character Size
    USE: The SI instruction specifies the size of labeling characters in centimetres. Use this instruction to establish character sizing that is not dependent on the settings of P1 and P2.
    '''
    args = _check_args([
        [],
        ['width', 'height']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SI{args};')

def SL(tangent=None):
    # See page 7-42
    '''SL, Character Slant
    USE: The SL instruction specifies the slant at which labels are drawn. Use this instruction to create slanted text for emphasis, or to reestablish upright labeling after an SL instruction with parameters has been in effect.
    '''
    args = _check_args([
        [],
        ['tangent']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SL{args};')

def SR(width=None, height=None):
    # See page 7-45
    '''SR, Relative Character Size
    USE: The SR instruction specifies the size of characters as a percentage of the distance between P1 and P2. Use this instruction to establish relative character sizes so if the P1/P2 distance changes, the character sizes adjust to occupy the same relative amount of space.
    '''
    args = _check_args([
        [],
        ['width', 'height']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SR{args};')

# Chapter 8: Drawing Polygons and Using the Polygon Buffer

def EP():
    # See page 8-15
    '''EP, Edge Polygon
    USE: Outlines the polygon currently stored in the polygon buffer. Use this instruction to edge polygons that you defined in polygon mode and with the rectangle and wedge instructions (RA, RR, and WG).
    '''
    return _cmd('EP;')

def FP():
    # See page 8-17
    '''FP, Fill Polygon
    USE: Fills the polygon currently in the polygon buffer. Use FP to fill polygons defined in polygon mode and by the edge rectangle and wedge instructions (EA, ER, and EW).
    '''
    return _cmd('FP;')

def GM(polygon_buffer=None, downloadable_character_buffer=None, reserved_buffer=None, vector_buffer=None, pen_sort_buffer=None):
    # See page 8-19
    '''GM, Graphics Memory
    USE: Allocates memory to four of the five buffers in the configurable graphics memory.
    '''
    args = _check_args([
        [],
        ['polygon_buffer'],
        ['polygon_buffer', 'downloadable_character_buffer'],
        ['polygon_buffer', 'downloadable_character_buffer', 'reserved_buffer'],
        ['polygon_buffer', 'downloadable_character_buffer', 'reserved_buffer', 'vector_buffer'],
        ['polygon_buffer', 'downloadable_character_buffer', 'reserved_buffer', 'vector_buffer', 'pen_sort_buffer'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'GM{args};')

def PM(n=None):
    # See page 8-21
    '''PM, Polygon Mode Instruction
    USE: Enters polygon mode for defining shapes such as block letters, logos, surface charts, or any unique or intricate area, and exits for subsequent filling and/or edging. Fills polygons using the fill polygon (FP) instruction and/or outline them using the edge polygon (EP) instruction.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'PM{args};')

# Chapter 9: Changing Picture Area and Orientation

def IW(x1=None, y1=None, x2=None, y2=None):
    # See page 9-8
    '''IW, Input Window
    USE: Defines a rectangular area, or window, that establishes soft-clip limits. Subsequent programmed pen motion will be restricted to this area. Use this instruction when you want to be sure that your plot falls within a specific plotting area.
    '''
    args = _check_args([
        [],
        ['x1', 'y1', 'x2', 'y2']
    ], locals())
    args = _join_args(args)
    return _cmd(f'IW{args};')

def OH():
    # See page 9-11
    '''OH, Output Hard-Clip Limits
    USE: Outputs the X,Y coordinates of the current hard-clip limits. Use this instruction to determine the plotter unit dimensions of the area in which plotting can occur.
    '''
    return _cmd('OH;')

def OP():
    # See page 9-12
    '''OP, Output P1 and P2
    USE: Outputs the X,Y coordinates (in plotter units) of the current scaling points P1 and P2. Use this instruction to determine the numeric coordinates of P1 and P2 when they have been set manually, and to help compute the number of plotter units per user unit when scaling is on. This instruction can also be used with the input (IW) instruction to programmatically set the window to P1 and P2.
    '''
    return _cmd('OP;')

def OW():
    # See page 9-13
    '''OW, Output Window
    USE: Outputs the X,Y coordinates of the lower-left and upper-right corners of the window area in which plotting can occur. This instruction is especially useful when the window area (defined by IW) extends beyond the hard-clip limits;
    '''
    return _cmd('OW;')

def RO(n=None):
    # See page 9-14
    '''RO, Rotate Coordinate System
    USE: Rotates the plotter's coordinate system 90 degrees about the plotter-unit coordinate origin. This instruction allow you to orient your plot vertically or horizontally.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'RO{args};')

# Chapter 10: Advanced Pen Control and Front-Panel Interaction

def AP(n=None):
    # See page 10-4
    '''AP, Automatic Pen Operations
    USE: Controls automatic pen operations such as returning a pen to the carousel if it has been in the older without drawing for a certain time.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'AP{args};')

def AS(pen_acceleration=None, pen_number=None):
    # See page 10-6
    '''AS, Acceleration Select
    USE: Sets pen acceleration for one or all pens. The default acceleration is suitable for all recommended pen and media combinations. Slowing the acceleration may improve line quality if you are using heavier than recommended media.
    '''
    args = _check_args([
        [],
        ['pen_acceleration'],
        ['pen_acceleration', 'pen_number']
    ], locals())
    args = _join_args(args)
    return _cmd(f'AS{args};')

def CV(n=None, input_delay=None):
    # See page 10-7
    # Note: Added input_delay parameter
    '''CV, Curved Line Generator
    USE: Collects vectors (line segments) in the vector buffer so that they can be plotted as a group. This allows the plotter to plot in a continuous motion, rather than stopping and starting at each vector endpoint. As a result, curves appear smoother.
    '''
    args = _check_args([
        [],
        ['n'],
        ['n', 'input_delay'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'CV{args};')

def FS(pen_force=None, pen_number=None):
    # See page 10-9
    '''FS, Force Select
    USE: Sets pen pressure to the paper for one or all pens. Use this instruction to optimize pen life and line quality for each pen and paper combination.
    '''
    args = _check_args([
        [],
        ['pen_force'],
        ['pen_force', 'pen_number'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'FS{args};')

def GP(group_number=None, pen_number=None, number_of_pens=None, length=None):
    # See page 10-11
    '''GP, Group Pen
    USE: Assigns pens of the same type/color to a group in order to extend the effective writing distance beyond the life of one pen.
    '''
    args = _check_args([
        [],
        ['group_number'],
        ['group_number', 'pen_number'],
        ['group_number', 'pen_number', 'number_of_pens'],
        ['group_number', 'pen_number', 'number_of_pens', 'length'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'GP{args};')

def KY(key=None, function=None):
    # See page 10-13
    '''KY, Define Key
    USE: Assigns a predefined function to one of the front-panel function keys. Use this instruction in conjunction with the WD instruction when designing interactive programs.
    '''
    args = _check_args([
        [],
        ['key'],
        ['key', 'function']
    ], locals())
    args = _join_args(args)
    return _cmd(f'KY{args};')

def NR():
    # See page 10-16
    '''NR, Not Ready
    USE: Programmatically simulates pressing the front-panel View button. However, you cannot take the plotter out of the View state with the NR instruction.
    '''
    return _cmd('NR;')

def OK():
    # See page 10-17
    '''OK, Output Key
    Outputs a number that indicates which, if any, of the front-panel function keys has been pressed. Use this instruction in conjunction with the WD instruction when designing interactive programs.
    '''
    return _cmd('OK;')

def SG(pen_number=None):
    # See page 10-19
    '''SG, Select Pen Group
    USE: Allows the plotter to select a predesignated group of pens. Use this instruction with the GP instruction to extend the effective writing distance beyond the limits of one pen.
    '''
    args = _check_args([
        [],
        ['pen_number']
    ], locals())
    args = _join_args(args)
    return _cmd(f'SG{args};')

def VS(pen_velocity=None, pen_number=None):
    # See page 10-20
    '''VS, Velocity Select
    USE: Specifies pen speed. Use the instruction to optimize pen life and line quality for each pen and media combination. Create a slightly thicker line on any media by slowing the pen speed.
    '''
    args = _check_args([
        [],
        ['pen_velocity'],
        ['pen_velocity', 'pen_number']
    ], locals())
    args = _join_args(args)
    return _cmd(f'VS{args};')

def WD(cc=None, terminator='\x03'):
    # See page 10-22
    '''WD, Write to Display
    USE: Specifies pen speed. Use the instruction to optimize pen life and line quality for each pen and media combination. Create a slightly thicker line on any media by slowing the pen speed.
    '''
    args = _check_args([
        ['terminator'],
        ['cc', 'terminator']
    ], locals())
    args = _join_args(args, sep='')
    if len(args) > 32 + len(terminator):
        raise ValueError('cc can only be up to 32 characters')
    for c in args[:-len(terminator)]:
        if c in [chr(0), chr(3), chr(5), chr(27), chr(127)]:
            raise ValueError('cc cannot contain NULL, ETX, ENQ, ESC and DEL')
    return _cmd(f'WD{args}') # Note this command doesn't end with ';'

# Part III – Special Applications
# Chapter 11: Digitizing

def DC():
    # See page 11-6
    '''DC, Digitize Clear
    USE: Terminates digitze mode. For example, if you are using an interrupt routine in a digitizing program to branch to another plotting function, use DC to clear the digitize mode immediately after branching.
    '''
    return _cmd('DC;')

def DP():
    # See page 11-7
    '''DP, Digitize Point
    USE: Returns the X,Y coordinates of a selected point on a plot to the computer for later use. Use this instruction to input data for a graphics program or to obtain the coordinates of a point or points on a plot.
    '''
    return _cmd('DP;')

def OD():
    # See page 11-8
    '''OD, Output Digitized Point and Pen Status
    USE: Outputs the X,Y coordinates and up/down pen position associated with the last digitized point. Use this instruction  after the DP instruction to return the coordinates of the digitized point to your computer.
    '''
    return _cmd('OD;')

# Chapter 12: Rollfeed Instructions and Long-Axis Printing

def AF():
    # See page 12-9
    '''AF, Advance Full Page
    USE: Advances roll media one full page length and establishes the origin at the center of the new page.
    '''
    return _cmd('AF;')

def AH():
    # See page 12-10
    '''AH, Advance Half Page
    USE: Advances roll media one half page length and establishes the origin at the center of the new page.
    '''
    return _cmd('AH;')

def EC(n=None):
    # See page 12-11
    '''EC, Enable Cut Line
    USE: Draws a dashed cut line between 'pages' on roll media to indicate where to cut the media. Used with AF, AH, and PG instructions.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'EC{args};')

def FR():
    # See page 12-12
    '''FR, Frame Advance
    USE: Advances media to the next plot frame and calculates a relative coordinate system for that frame. Use FR to do multi-frame long-axis plotting.
    '''
    return _cmd('FR;')

def PG(n=None):
    # See page 12-13
    '''PG, Page Feed
    USE: Advances roll media one page length and establishes the plotter-unit origin at the center of the new page.
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args)
    return _cmd(f'PG{args};')

def PS(length=None, width=None):
    # See page 12-14
    # Note: Corrected AF to AH in use instruction
    '''PS, Page Size
    USE: Changes the size of the hard clip limits while keeping the origin in the center of the plot. This allows for variable length page advances with the AF, AH, FR and PG instructions.
    '''
    args = _check_args([
        [],
        ['length'],
        ['length', 'width']
    ], locals())
    args = _join_args(args)
    return _cmd(f'PS{args};')

# Chapter 13: Alternate Character Sets and User-Designed Characters

def CA(set=None):
    # See page 13-21
    '''CA, Designate Alternate Character Set
    USE: Designates a character set as the alternate character set to be used in labeling instructions. Use this instruction to provide an additional character set that you can easily access in a program.
    '''
    args = _check_args([
        [],
        ['set']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CA{args};')

def CC(chord_angle=None):
    # See page 13-23
    '''CC, Character Chord Angle
    USE: Sets the chord angle that determines the smoothness of characters drawn when you select one of the arc-font character sets for labeling.
    '''
    args = _check_args([
        [],
        ['chord_angle']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CC{args};')

def CM(switch_mode=None, fallback_mode=None):
    # See page 13-25
    '''CM, Character Selection Mode
    USE: Specifies mode of character set selection and usage. Read Choosing Other Character Selection Modes earlier in this chapter to determine if you need this instruction.
    '''
    args = _check_args([
        [],
        ['switch_mode'],
        ['switch_mode', 'fallback_mode']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CM{args};')

def CS(set=None):
    # See page 13-27
    '''CS, Designate Standard Character Set
    USE: Designates a character set as the standard character set for labeling instructions. Use this instruction to change the default ANSI ASCII English set to one with characters appropriate to your application. This instruction is particularly useful if you plot most of your labels in a language other than English.
    '''
    args = _check_args([
        [],
        ['set']
    ], locals())
    args = _join_args(args)
    return _cmd(f'CS{args};')

def DL(character_number=None, *coordinates):
    # See page 13-28
    '''DL, Define Downloadable Character
    USE: Allows you to design characters and stores them in a buffer for repeated use.
    '''
    if len(coordinates) == 0: del coordinates # Remove if empty, for argument check to work properly
    args = _check_args([
        [],
        ['character_number'],
        ['character_number', 'coordinates']
    ], locals())
    args = _join_args(args)
    return _cmd(f'DL{args};')

def DS(slot=None, set=None):
    # See page 13-32
    '''DS, Designate Character Set into Slot
    USE: Designates up to four character sets to be immediately available for plotting. Used with ISO character sets and modes.
    '''
    args = _check_args([
        [],
        ['slot', 'set']
    ], locals())
    args = _join_args(args)
    return _cmd(f'DS{args};')

def IV(slot=None, left=None):
    # See page 13-34
    '''IV, Invoke Character Slot
    USE: Invokes a character slot into either the right or left half of the in-use code table. Primarily used with ISO modes of character selection.
    '''
    args = _check_args([
        [],
        ['slot'],
        ['slot', 'left']
    ], locals())
    args = _join_args(args)
    return _cmd(f'IV{args};')

def SA():
    # See page 13-36
    '''SA, Select Alternate Character Set
    USE: The SA instruction selects the alternate character set (already designated by the CA instruction) for subsequent labeling. Use this instruction to shift from the currently selected standard set to the designated alternate set.
    '''
    return _cmd('SA;')

def SS():
    # See page 13-37
    '''SS, Select Standard Character Set
    USE: The SS instruction selects the standard set (already designated by the CS, Designate Standard Character Set, instruction) for subsequent labeling. Use this instruction to shift from the currently selected alternate set to the designated standard set.
    '''
    return _cmd('SS;')

def UC(*increments):
    # See page 13-38
    '''UC, User-defined Character
    USE: The UC instruction draws characters of your own design. Use this instruction to create characters or symbols not included in your plotter's character sets or to draw logos.
    '''
    if len(increments) == 0: del increments # Remove if empty, for argument check to work properly
    args = _check_args([
        [],
        ['increments'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'UC{args};')

# Part IV – Interfacing, Handshaking, Output, and Device Control
# Chapter 14: Obtaining Information from the Plotter

def GC(count_number=None):
    # See page 14-9
    '''GC, Group Count
    USE: Assigns a number known as the 'group count,' which is the number that will be output by the OG instruction. The group count is an arbitrary number that you assign at the beginning of a data block in spooling applications (typically in an RS-232-C configuration with a mainframe computer). Use this instruction in conjunction with the OG instruction to monitor the successful transfer of data blocks.
    '''
    args = _check_args([
        [],
        ['count_number'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'GC{args};')

def IM(e_mask_value=None, s_mask_value=None, p_mask_value=None):
    # See page 14-10
    '''IM, Input Mask
    USE: Controls which HP-GL errors are reported. If you are using an HP-IB interface, you can also use IM to control the conditions that cause an HP-IB service reques or a positive response to a parallel poll.
    '''
    args = _check_args([
        [],
        ['e_mask_value'],
        ['e_mask_value', 's_mask_value'],
        ['e_mask_value', 's_mask_value', 'p_mask_value'],
    ], locals())
    args = _join_args(args)
    return _cmd(f'IM{args};')

def OA():
    # See page 14-13
    '''OA, Output Actual Pen Status
    USE: Outputs the current pen location (in plotter units) and up/down position. You can use this information to position a label of figure, to determine the parameters of some desired window, or to determine the pen's current location if it has been moved using front-panel Cursor Control buttons.
    '''
    return _cmd('OA;')

def OC():
    # See page 14-14
    '''OC, Output Commanded Pen Status
    USE: Outputs the location and up/down position of the last commanded move. Use this instruction to position a label or determine the parameters of an instruction that tried to move the pen beyond the limits of some window. You can also use this instruction when you want to know the pen's location in user units. 
    '''
    return _cmd('OC;')

def OE():
    # See page 14-15
    '''OE, Output Error
    USE: Outputs a number corresponding to the type of HP-GL error (if any) received by the plotter after the most recent IN instruction, front-panel reset, or OE instruction. Use this instruction for debugging programs.
    '''
    return _cmd('OE;')

def OF():
    # See page 14-17
    '''OF, Output Factors
    USE: Outputs the number of plotter units per millimetre in each axis. This instruction lets you use the plotter with software that needs to know the size of a plotter unit.
    '''
    return _cmd('OF;')

def OG():
    # See page 14-18
    '''OG, Output Group Count
    USE: Outputs the data block number of the current group count and whether the escape function has been activated. Use this instruction at the end of a data block in spooling applications, where it is important to know the current data block number and whether the data block has been transferred.
    '''
    return _cmd('OG;')

def OI():
    # See page 14-19
    '''OI, Output Identification
    Outputs the plotter's identifying model number. This information is useful in a remote operating configuration (where several plotters are connected to the computer) to determine which plotter model is on-line, or when software needs the plotter's model number.
    '''
    return _cmd('OI;')

def OL():
    # See page 14-20
    '''OL, Output Label Length
    Output information about the label contained in the label buffer.
    '''
    return _cmd('OL;')

def OO():
    # See page 14-22
    '''OO, Output Options
    Outputs eight option parameters indicating features implemented on the plotter. Some software packages use this feature to determine which plotter capabilities exist.
    '''
    return _cmd('OO;')

def OS():
    # See page 14-23
    '''OS, Output Status
    Outputs the decimal value of the status byte. Use this instruction in debugging operations and in digitizing applications.
    '''
    return _cmd('OS;')

def OT():
    # See page 14-25
    '''OT, Output Carousel Type
    The OT instruction outputs information on the type of carousel loaded and the stalls occupied.
    '''
    return _cmd('OT;')

# Chapter 15: Device-Control Instructions

def ESC_A():
    # See page 15-7
    '''ESC.A, Output Identification
    USE: Outputs the plotter's model number and firmware revision level.
    '''
    return _cmd('\x1b.A');

def ESC_B():
    # See page 15-8
    '''ESC.B, Output Buffer Space
    USE: Outputs the plotter's currently available logical I/O buffer space.
    '''
    return _cmd('\x1b.B');

def ESC_E():
    # See page 15-8
    '''ESC.E, Output Extended Error
    USE: Outputs the error number for any I/O error related to device-control instructions and clears the error message from the front-panel display. Use this instruction when debugging a program to determine which errors have occured (if any). Additionally, if you are using the RS-232-C interface, you can use ESC.E with ESC.@ to do block I/O error checking.
    '''
    return _cmd('\x1b.E');

def ESC_J():
    # See page 15-11
    '''ESC.J, Abort Device-Control
    USE: Aborts any device-control instruction that may be partially decoded or executed. Use this instruction in an initialization sequence when you first access the plotter.
    '''
    return _cmd('\x1b.J');

def ESC_K():
    # See page 15-12
    '''ESC.K, Abort Graphics
    USE: Aborts any partially decoded HP-GL instruction and discards remaining instructions in the I/O, pen sort, bidirectional, and vector buffers. Use this instruction as part of an initialization sequence when starting a new program or to terminate plotting of HP-GL instructions in the buffer.
    '''
    return _cmd('\x1b.K');

def ESC_L():
    # See page 15-13
    '''ESC.L, Output Buffer Size When Empty
    USE: Outputs the size (in bytes) of the logical I/O buffer. The response is not transmitted by the plotter until the buffer is empty.
    '''
    return _cmd('\x1b.L');

def ESC_O():
    # See page 15-14
    '''ESC.O, Output Extended Status
    USE: Outputs the plotter's extended status. Use this instruction to obtain information about the current operating status of the plotter.
    '''
    return _cmd('\x1b.O');

def ESC_Q(n=None):
    # See page 15-17
    '''ESC.Q, Set Monitor Mode
    USE: Enables or disables either monitor mode 1 (parse) or monitor mode 2 (receive). Use this instruction as a debugging aid in program development. This instruction is valid only when you have set Monitor Mode: ON from the front panel (refer to the User's Guide for more information).
    '''
    args = _check_args([
        [],
        ['n']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.Q{args}:');

def ESC_R():
    # See page 15-19
    '''ESC.R, Reset
    USE: Resets certain I/O conditions to power-up default states. Use this instruction to establish known conditions when starting a new plot.
    '''
    return _cmd('\x1b.R');

def ESC_S(n):
    # See page 15-20
    '''ESC.S, Output Configurable Memory Size
    USE: Outputs the total memory size of user-definable RAM, or the memory space available in one of its five buffers: the physical I/O buffer, polygon buffer, downloadable character buffer, vector buffer, and pen sort buffer. Use this instruction to determine how much memory is currently allocated to each buffer or to confirm the allocation performed by GM, ESC.T, or ESC.R.
    '''
    return _cmd(f'\x1b.S{n}:');

def ESC_T(physical_io_buffer=None, polygon_buffer=None, downloadable_character_buffer=None, vector_buffer=None, pen_sort_buffer=None):
    # See page 15-21
    '''ESC.T, Allocate Configurable Memory
    USE: Allocates memory in user-definable RAM, which consists of five buffers: the physical I/O buffer, polygon buffer, downloadable character buffer, vector buffer, and pen sort buffer. Use this instruction to change the sizes of these buffers as needed.
    '''
    args = _check_args([
        [],
        ['physical_io_buffer'],
        ['physical_io_buffer', 'polygon_buffer'],
        ['physical_io_buffer', 'polygon_buffer', 'downloadable_character_buffer'],
        ['physical_io_buffer', 'polygon_buffer', 'downloadable_character_buffer', 'vector_buffer'],
        ['physical_io_buffer', 'polygon_buffer', 'downloadable_character_buffer', 'vector_buffer', 'pen_sort_buffer'],
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.T{args}:');

def ESC_U():
    # See page 15-24
    '''ESC.U, End Flush Mode
    USE: Ends flush mode. Use this instruction in spooling applications to end flush mode, thus allowing the plotter to begin parsing graphics instructions again.
    '''
    return _cmd('\x1b.U');

def ESC_Y():
    # See page 15-25
    '''ESC.Y or ESC.(, Plotter On
    USE: Enables the plotter to accept data and interpret it as graphics or device-control instructions. Use this instruction in Eavesdrop (RS-232-C interface only) to establish programmed-on operation.
    '''
    return _cmd('\x1b.Y');

def ESC_Z():
    # See page 15-25
    '''ESC.Z or ESC.), Plotter Off
    USE: Disables the plotter so that it accepts only a plotter-on instruction. Use this instruction in Eavesdrop (RS-232-C interface only) to establish programmed-off operation.
    '''
    return _cmd('\x1b.Y');

def ESC_AT(logical_io_buffer_size=None, io_conditions=None):
    # See page 15-26
    '''ESC.@, Set Plotter Configuration
    USE: For RS-232-C users, this instruction sets an effective logical I/O buffer size and controls hardwire handshake, communications protocol, monitor modes 1 and 2, and block I/O error checking.
    '''
    args = _check_args([
        [],
        ['logical_io_buffer_size'],
        ['logical_io_buffer_size', 'io_conditions']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.@{args}:');

# Chapter 16: Interfacing and Handshaking

def ESC_H(data_block_size=None, enquiry_character=None, acknowledgement_string=None):
    # See page 16-22
    '''ESC.H, Set Handshake Mode 1
    USE: Configures the plotter for enquire/acknowledge handshake when the computer requires the parameters of ESC.M and ESC.N be used during the handshaking sequence.
    '''
    args = _check_args([
        [],
        ['data_block_size'],
        ['data_block_size', 'enquiry_character'],
        ['data_block_size', 'enquiry_character', 'acknowledgement_string']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.H{args}:');

def ESC_I(xoff_threshold_level_or_data_block_size=None, omitted_or_enquiry_character=None, xon_trigger_characters_or_acknowledgement_string=None):
    # See page 16-23
    '''ESC.I, Set Handshake Mode 2
    USE: Configures the plotter for either Xon-Xoff or enquire/acknowledge handshakes when the computer does not expect the parameters of the ESC.M and ESC.N instructions to be used during the handshaking sequence. This is often true when the handshake protocol is part of the computer's operating system.
    '''
    args = _check_args([
        [],
        ['xoff_threshold_level_or_data_block_size'],
        ['xoff_threshold_level_or_data_block_size', 'omitted_or_enquiry_character'],
        ['xoff_threshold_level_or_data_block_size', 'omitted_or_enquiry_character', 'xon_trigger_characters_or_acknowledgement_string']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.I{args}:');

def ESC_M(turnaround_delay=None, output_trigger=None, echo_terminator=None, output_terminator=None, output_initiator=None):
    # See page 16-25
    '''ESC.M, Set Output Mode
    USE: Establishes parameters for the plotter's communication format. Use the instruction to establish a turnaround delay, an output trigger character, an echo terminator, and an output initiator character. Also use it to change the output terminator from its default value, ASCII decimal code 13 (carriage return).
    '''
    args = _check_args([
        [],
        ['turnaround_delay'],
        ['turnaround_delay', 'output_trigger'],
        ['turnaround_delay', 'output_trigger', 'echo_terminator'],
        ['turnaround_delay', 'output_trigger', 'echo_terminator', 'output_terminator'],
        ['turnaround_delay', 'output_trigger', 'echo_terminator', 'output_terminator', 'output_initiator'],
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.M{args}:');

def ESC_N(intercharacter_delay=None, handshake_dependent_parameter=None):
    # See page 16-28
    '''ESC.N, Set Extended Output and Handshake Mode
    USE: Establishes parameters for the plotter's communication format. Use the instruction to specify an intercharacter delay in all handshake modes and either the immediate response string for the enquire/acknowledge handshake or the Xoff trigger character(s) for the Xon-Xoff handshake.
    '''
    args = _check_args([
        [],
        ['intercharacter_delay'],
        ['intercharacter_delay', 'handshake_dependent_parameter']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.N{args}:');

def ESC_P(handshake=None):
    # See page 16-29
    '''ESC.P, Set Handshake Mode
    USE: Set one of the three standard handshakes.
    '''
    args = _check_args([
        [],
        ['handshake']
    ], locals())
    args = _join_args(args, sep=';')
    return _cmd(f'\x1b.P{args}:');



_add_lowercase()
