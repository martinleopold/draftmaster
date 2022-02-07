'''Show info (don't print anything)'''

from draftmaster import *
import draftmaster as dm

def to_mm(x, factors=(40,40)):
    return tuple( val/factors[i % len(factors)] for i, val in enumerate(x) )

def to_bits(num, len=16):
    b = '{:0' + str(len) + 'b}'
    b = b.format(num)
    b = b[::-1] # reverse string
    b = tuple(map(int, b))
    return b

# detect paper size from printable area (length, width)
def detect_paper(d):
    TOLERANCE = 0.02
    d = (d[0] + 30, d[1] + 30) # add non-printable margins (15mm)
    d = sorted(d) # so d[0] is the shorter side
    papers = { # all given in portrait orientation
        'A6':    (105, 148),
        'A5':    (148, 210),
        'A4':    (210, 297),
        '24x34': (240, 340),
        'A3':    (297, 420),
        'A2':    (420, 594),
        '50x70': (500, 700),
        'A1':    (594, 841),
        'A0':    (841, 1189)
    }
    for p in papers.items():
        allowed_x = ( p[1][0] * (1-TOLERANCE), p[1][0] * (1+TOLERANCE) )
        allowed_y = ( p[1][1] * (1-TOLERANCE), p[1][1] * (1+TOLERANCE) )
        if d[0] >= allowed_x[0] and d[0] <= allowed_x[1] and d[1] + 24 >= allowed_y[0] and d[1] + 24 <= allowed_y[1]:
            return (p[0], p[1], 'portrait')
        if d[0] + 24 >= allowed_x[0] and d[0] + 24 <= allowed_x[1] and d[1] >= allowed_y[0] and d[1] <= allowed_y[1]:
            return (p[0], p[1], 'landscape')
        if d[0] <= allowed_x[1] and d[1] <= allowed_y[1]:
            return (p[0], p[1], 'unknown')
    return None

def carousel_map(map):
    b = f'{map:08b}'
    b = b[::-1] # reverse string
    # return { i+1:status for i, status in enumerate(b) }
    return b[:4] + ' ' + b[4:]

def status(bits):
    bits = f'{bits:08b}'
    bits = bits[::-1] # reverse string
    bits = tuple(map(int, bits))
    out = ''
    for i, b in enumerate(bits):
        if b: out += dm._status_bits[i] + '. '
    out = out.strip()
    return out

def state(bits):
    if not bits[4] and not bits[5]: return 'Ready'
    elif bits[4] and not bits[5]: return 'View'
    elif not bits[4] and bits[5]: return 'Not ready (Paper not loaded)'
    return ''

open()

ESC_A()
esc_a = read()
print(f'       plotter id (ESC.A): {esc_a[0]}, firmware rev. {esc_a[1]}')

ESC_B()
esc_b = read()
print(f' i/o buffer space (ESC.B): {esc_b}')
print()

# ESC_E()
# esc_e = read()
# print(f'        i/o error (ESC.E): {esc_e}')

ESC_O()
esc_o = read()
print(f'           status (ESC.O): {esc_o}')
esc_o = to_bits(esc_o)
print(f'                    State: {state(esc_o)}')
print(f'             Paper marked: {"Yes (Not clean)" if esc_o[1] else "No (Clean)"}')
print(f'               Cover open: {"Yes (open)" if esc_o[6] else "No (Lowered)"}')
print(f'         Using roll paper: {"Yes" if esc_o[0] else "No (Single Sheet)"}')
print(f'         I/O buffer empty: {"Yes (Ready for data)" if esc_o[3] else "No (Not empty)"}')
print(f'           Paper advanced: {"Yes" if esc_o[2] else "No"}')
print(f'     Function Key pressed: {"Yes" if esc_o[9] else "No"}')
print(f'        Servo malfunction: {"Yes" if esc_o[10] else "No"}')
print(f'                  Emulate: {"ON" if esc_o[7] else "OFF"}')
print(f'                   Expand: {"ON" if esc_o[8] else "OFF"}')
print(f'              Invert plot: {"OFF" if esc_o[11] else "ON"}')
print()

ESC_S(0)
esc_s0 = read()
ESC_S(1)
esc_s1 = read()
ESC_S(2)
esc_s2 = read()
ESC_S(3)
esc_s3 = read()
ESC_S(4)
esc_s4 = read()
ESC_S(5)
esc_s5 = read()
ESC_S(6)
esc_s6 = read()
print(f'           memory (ESC.S):')
print(f'         (0) total buffer: {esc_s0}')
print(f'           (1) i/o buffer: {esc_s1}')
print(f'       (2) polygon buffer: {esc_s2}')
print(f'     (3) character buffer: {esc_s3}')
print(f'      (4) reserved buffer: {esc_s4}')
print(f'        (5) vector buffer: {esc_s5}')
print(f'      (6) pen sort buffer: {esc_s6}')
print()

if esc_o[5]: # Not ready
    close(wait=False)
    exit()

if esc_o[6]: print('Close cover to continue...')

if esc_o[4]: print('Exit view mode to continue...')

IN()

OI()
oi = read()
print(f'       plotter id (OI): {oi}')
print()

OH() # output hard clip limits
oh = read()
print(f' hard clip limits (OH): {oh}')

OW() # output window
ow = read()
print(f'           window (OW): {ow}')

OP() # output P1 and P2
op = read()
print(f'        p1 and p2 (OP): {op}')
print()

OA() # output actual pen status
oa = read()
print(f'actual pen status (OA): {oa}')

OT() # output carousel type
ot = read()
print(f'    carousel type (OT): {ot}')

# output factors (plotter units per mm); always (40,40)
OF()
of = read()
print(f'          factors (OF): {of}')

OO() # output options
oo = read()
print(f'          options (OO): {oo}')

OS() # output status
os = read()
print(f'           status (OS): {os}')
print()


clip = to_mm(oh, of) # hard clip limits in mm
wh = ( clip[2] - clip[0], clip[3] - clip[1])
detected_size = detect_paper(wh)
print(f'        printable area: {round(wh[1])} × {round(wh[0])} mm')
print(f' paper size (detected): {detected_size[0]}, {detected_size[1][0]} × {detected_size[1][1]} mm, {detected_size[2]}')
print(f'                 media: {dm._paper_check_bit[oo[0]]}')
print(f'         carousel type: {dm._carousel_types[ot[0]]}')
print(f'    carousel map (1-8): {carousel_map(ot[1])}')
print(f'                   pen: {"down" if oa[2] else "up"}, {to_mm(oa[:2], of)} mm')
print(f'                status: {status(os)}' )

close()
