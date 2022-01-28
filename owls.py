'''
two owls with partially filled polygons, two color fills
colors:
1: black
2: blue
3: yellow
'''

import draftmaster as dm
from draftmaster import *
import svg

SCALE = 2.2
DECIMALS = 0

root, paths = svg.elements('svg/owlsA.svg', ['path'])

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

open('/dev/tty.usbserial-A700CYY0')
IN()
GM(25520)
# blue fills
SP(2) 
fill('body-big', 'big-eye-L', 'big-eye-R', 'beak-big')
fill('small-eye-L', 'small-pupil-L')
# yellow fills
SP(3) 
fill('small-body', 'small-eye-L', 'small-eye-R', 'small-beak')
fill('small-foot-L', 'small-foot-R')
fill('small-beak')
# black fills
SP(1)
fill('big-pupil-L', 'big-pupil-R')
fill('small-pupil-L', 'small-pupil-R')
# black outlines
plot('body-big', 'big-foot-L', 'big-foot-R')
plot('big-pupil-L', 'big-pupil-R')
plot('big-eye-L', 'big-eye-R', 'beak-big')
plot('small-body', 'small-foot-L-lower-part', 'small-foot-R-lower-part')
plot('small-pupil-L', 'small-pupil-R')
plot('small-eye-L', 'small-eye-R', 'small-beak')
plot('branch-1', 'branch-2', 'branch-3', 'branch-4', 'branch-5-addition', 'branch-6')
# some outlines again
plot('body-big', 'big-foot-L', 'big-foot-R')
plot('big-eye-L', 'big-eye-R', 'beak-big')
plot('small-body')
plot('branch-1', 'branch-2', 'branch-3', 'branch-4', 'branch-5-addition', 'branch-6')
SP(0)
close()



## OUTLINE ONLY
# open('/dev/tty.usbserial-A700CYY0')
# IN()
# SP(1)
# plot('beak-big')
# plot('big-eye-L')
# plot('big-pupil-L')
# plot('big-eye-R')
# plot('big-pupil-R')
# plot('big-foot-L')
# plot('big-foot-R')
# plot('small-body')
# plot('small-beak')
# plot('small-eye-L')
# plot('small-pupil-L')
# plot('small-eye-R')
# plot('small-pupil-R')
# plot('small-foot-L-lower-part')
# plot('small-foot-R-lower-part')
# plot('branch-1')
# plot('branch-2')
# plot('branch-3')
# plot('branch-4')
# plot('branch-5-addition')
# plot('branch-6')
# SP(0)
# close()



## BLACK
# open('/dev/tty.usbserial-A700CYY0')
# IN()
# GM(25520)
# SP(1)
# fill('body-big', 'big-eye-L', 'big-eye-R', 'beak-big')
# fill('big-pupil-L', 'big-pupil-R')
# plot('big-pupil-L', 'big-pupil-R')
# #missing big eye outlines + beak
# plot('body-big', 'big-foot-L', 'big-foot-R')
# fill('small-body', 'small-eye-L', 'small-eye-R', 'small-beak')
# fill('small-foot-L', 'small-foot-R')
# plot('small-body', 'small-foot-L-lower-part', 'small-foot-L-lower-part')
# fill('small-eye-L', 'small-pupil-L')
# fill('small-beak')
# fill('small-pupil-L', 'small-pupil-R')
# plot('small-pupil-L', 'small-pupil-R')
# plot('small-eye-L', 'small-eye-R', 'small-beak')
# plot('branch-1', 'branch-2', 'branch-3', 'branch-4', 'branch-5-addition', 'branch-6')
# SP(0)
# close()
