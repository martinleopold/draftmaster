'''
one wal
'''

import draftmaster as dm
from draftmaster import *
import svg

SCALE = 10.0
DECIMALS = 0

root, paths = svg.elements('svg/wal.svg', ['path'])

vb = svg.parse_viewbox(root.attrib['viewBox'])
vb_left, vb_top, vb_width, vb_height = vb
print(vb)

def transform(p):
    # flip y
    p = p[0], vb_height - p[1]
    # center
    p = p[0] - vb_width/2, p[1] - vb_height/2
    # scale
    p = p[0] * SCALE, p[1] * SCALE
    # decimal places
    p = round(p[0], DECIMALS), round(p[1], DECIMALS)
    if (DECIMALS == 0): p = int(p[0]), int(p[1])
    return p

def plot_linestrip(ls):
    first = ls[0] 
    rest = ls[1:]
    PA( *transform(first) )
    for point in rest:
        PD( *transform(point) )
    PU()

def fill_linestrip(ls):
    first = ls[0] 
    rest = ls[1:]
    PA( *transform(first) )
    PM()
    for point in rest:
        PD( *transform(point) )
    PU()
    PM(2)
    FP()

def fill_linestrips(*linestrips):
    for i, ls in enumerate(linestrips):
        first = ls[0]
        rest = ls[1:]
        if i == 0:
            PA( *transform(first) )
            PM()
            for point in rest: PD( *transform(point) )
            PM(1)
        else:
            for point in ls: PD( *transform(point) )
            PM(1)
    PU()
    PM(2)
    FP()

def get_id_and_linestrip(p):
    return p.attrib['id'], svg.parse_linestrip_path(p.attrib['d'])

p = list(map(get_id_and_linestrip, paths))
p = dict(p)

# def plot(id): plot_linestrip(p[id])
def plot(*ids): 
    for id in ids: plot_linestrip(p[id])

# def fill(id): fill_linestrip(p[id])
def fill(*ids):
    linestrips = list(map(lambda id:p[id], ids))
    fill_linestrips(*linestrips)

print(list(p.keys()))
print()

dm._debug = True
# dm._dry = True

open()
IN()
GM(25000, 0, 0, 0, 0) # maximize polygon buffer
SP(1)
fill('outline', 'eye')
plot('outline', 'eye')
SP(0)
close()
