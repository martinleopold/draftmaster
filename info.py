'''Show info (don't print anything)'''

from draftmaster import *
import draftmaster as dm

def to_mm(x, factors=(40,40)):
    return tuple( val/factors[i % len(factors)] for i, val in enumerate(x) )

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
        print(p[0], allowed_x, allowed_y)
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

open('/dev/tty.usbserial-A700CYY0')
IN()

OI()
oi = read()
print(f'       plotter id (OI): {oi}')
print()

OF() # output factors (plotter units per mm)
of = read()

OH() # output hard clip limits
oh = read()
print(f' hard clip limits (OH): {oh} {to_mm(oh, of)} mm')

OW() # output window
ow = read()
print(f'           window (OW): {ow} {to_mm(ow, of)} mm')

OP() # output P1 and P2
op = read()
print(f'        p1 and p2 (OP): {op} {to_mm(op, of)} mm')
print()

OA() # output actual pen status
oa = read()
print(f'actual pen status (OA): {oa} {to_mm(oa[:2], of)} mm, pen {"down" if oa[2] else "up"}')

OT() # output carousel type
ot = read()
print(f'    carousel type (OT): {ot}')

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
print(f'         carousel type: {dm._carousel_types[ot[0]]}')
print(f'    carousel map (1-8): {carousel_map(ot[1])}')

close()
