'''Show info (don't print anything)'''
'''
Notes: 
Longer Axis is always X.
Landscape: P1 bottom-left, P2 top-right, non-printable border at the bottom
Portrait:  P1 top-left, P2 bottom-right, non-printable border at the bottom
Paper loading:
  A4: landscape
  A3: portrait
  A2: landscape
'''
from draftmaster import *
import draftmaster as dm

def to_mm(x, factors=(40,40)):
    return tuple( val/factors[i % len(factors)] for i, val in enumerate(x) )

# detect paper size
def find_paper(x):
    x = sorted(x)
    papers = {
        'A6': (105, 148),
        'A5': (148, 210),
        'A4': (210, 297),
        'A3': (291, 420),
        'A2': (420, 594),
        'A1': (594, 841),
        'A0': (841, 1189)
    }
    for p in papers.items():
        if x[0] <= p[1][0] and x[1] <= p[1][1]: return p
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
wh = ( clip[2] - clip[0], clip[3] - clip[1] )
detected_size = find_paper(wh)
print(f'      paper size (DIN): {detected_size[0]} {detected_size[1]} mm')
print(f'         carousel type: {dm._carousel_types[ot[0]]}')

print(f'    carousel map (1-8): {carousel_map(ot[1])}')

close()
