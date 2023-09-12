'''
2023-09-08
plot polygons from SVG
used to plot cover image from FH Technikum Wissensbilanz 2019/20

Added:
   * acceleration, velocity, force
   * scaling
'''

DRY = False
BOUNDS_ONLY = False
SCALE = 90 # percent

'''
int 1..4 [g's]
default: 4
'''
ACCELERATION = 1

'''
int 1..60 (cm/s)
defaults:
P (paper) ... 50
T (transparency) ... 10
R (roller ball) ... 60
V (drafting for vellum and paper), F (drafting for film) ... 30
'''
VELOCITY = 20

'''
int 1..8
defaults:
1 ... 15 grams
2 ... 24 grams; default for carousel types P (paper) and T (transparency)
3 ... 30 grams; default for carousel type V (drafting for vellum and paper) and F (drafting for film)
4 ... 36 grams
5 ... 45 grams
6 ... 51 grams; default for carousel type R (roller ball)
7 ... 57 grams
8 ... 66 grams
'''
FORCE = 3

import os as _os
import re as _re
import xml.etree.ElementTree as _ET
import math

from draftmaster import *
import draftmaster as dm


def rmns(tag):
    '''Remove namespace (eg. {http://example.com}) from tag'''
    return _re.sub(r'\{[^\}]*\}', '', tag)
    
def parse_svg(filepath_or_svgtext):
    '''Parse SVG using xml.etree.ElementTree
    Namespaces are removed from tag names.
    filepath_or_svgtext: Path to an SVG file or SVG text.
    Returns the root xml.etree.ElementTree.Element.
    '''
    if _os.path.exists(filepath_or_svgtext): # treat as file path
        root = _ET.parse(filepath_or_svgtext).getroot()
    else: # treat as svg text
        root = _ET.fromstring(filepath_or_svgtext)
    for el in root.iter():
        el.tag = rmns(el.tag)
    return root

def svg_elements(filepath_or_svgtext, tags=[]):
    '''Get flat list of elements contained in an SVG file
    filepath_or_svgtext: Path to an SVG file or SVG text.
    tags: List of tags to return. If empty (default) return all elements.
    Returns root element and list of xml.etree.ElementTree.Element.
    '''
    root = parse_svg(filepath_or_svgtext)
    els = root.iter()
    if tags: els = filter(lambda el: el.tag in tags, els)
    return root, list(els)

def parse_points(str):
    p = _re.split(',|\s+', str)
    p = list( map(float, p) ) # raw list of coordinates
    a = iter(p)
    pointlist = [ (x, y) for x, y in zip(a, a) ]
    return pointlist

def scale_points(*points, scale = SCALE):
    scale = scale / 100
    scaled = map(lambda p: ((p[0]-width/2)*scale + width/2, (p[1]-height/2)*scale + height/2), points)
    return list(scaled)

root, polys = svg_elements('svg/2021-01-28_14-15-12-496.svg', ['polygon'])
# print(root)
print(f'  polys: {len(polys)}')

viewBox = root.attrib['viewBox'].split(' ')
viewBox = tuple(map(float, viewBox))
left, top, width, height = viewBox
print(f'viewbox: {viewBox}')

open()
IN()

# Rotate plotter coordinate system: 
# In a Portrait view we have: origin center, +x right, +y up
# P1 is bottom left, P2 is top right
RO(90)
IP()

# shift p1 and p2 to the right
OP()
op = read()
shift = (39-15) * 40 / 2 # 12 mm
IP(op[0] + shift, op[1], op[2] + shift, op[3])

# SVG coordinate system: origin is top left, +x is right, +y is down
# scale isotropic; new coordinate system: center top left (y down), width/height from viewbox
# SC x_min, x_max,  y_min, y_max, type   (x_min, y_min are mapped onto p1; x_max, y_max are mapped onto p2)
SC(      0, width, height,     0,    1)

if DRY: dm._dry = True

SP(1)

if ACCELERATION > 0: AS(ACCELERATION)
if VELOCITY > 0: VS(VELOCITY)
if FORCE > 0: FS(FORCE)

# if BOUNDS_ONLY:
#     PA(0, 0)
#     EA(width, height)

i = 0
xmin = math.inf
xmax = -math.inf
ymin = math.inf
ymax = -math.inf
for poly in polys:
    points = parse_points( poly.attrib['points'] )
    points = scale_points(*points)
    i += 1
    print(f'poly {i}/{len(polys)}:   {len(points)} points')
    for p in points:
        if p[0] < xmin: xmin = p[0]
        if p[0] > xmax: xmax = p[0]
        if p[1] < ymin: ymin = p[1]
        if p[1] > ymax: ymax = p[1]
    if BOUNDS_ONLY: continue
    fp = points[0]  # first point
    PA(*fp) # move to first point
    for p in points:
        PD(*p)
    PA(*fp) # move to fist point again (to close the path)
    PU() # pen up
    # input("Press Enter to continue...")

print(f'min: {(xmin,ymin)}')
print(f'max: {(xmax,ymax)}')
if BOUNDS_ONLY:
    PA(xmin, ymin)
    EA(xmax, ymax)

SP(0)
# input("Press Enter to finish...")
close()