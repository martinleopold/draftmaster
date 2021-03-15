'''
plot polygons from SVG
used to plot cover image from FH Technikum Wissensbilanz 2019/20
'''
import os as _os
import re as _re
import xml.etree.ElementTree as _ET

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
    pointlist = [ ( (x - width/2) * SCALE + width/2, (y - height/2) * SCALE + height/2) for x, y in zip(a, a) ]
    return pointlist

root, polys = svg_elements('svg/2021-02-01_14-53-31-633.svg', ['polygon'])
root, circs = svg_elements('svg/2021-02-01_14-53-31-633.svg', ['circle'])
# print(root)

print('polygons:', len(polys))
print('circles: ', len(circs))

viewBox = root.attrib['viewBox'].split(' ')
viewBox = tuple(map(float, viewBox))
left, top, width, height = viewBox
print(viewBox)

# dm._dry = True
SCALE = 2

open('/dev/tty.usbserial-A700CYY0')
IN()

AS(2)  # acceleration select: 1-4, default 4
FS(4)  # force select: (1-8), default for drafting 3
VS(15) # velocity select: (1-60), default for drafting 30

# Rotate plotter coordinate system: 
# In a Portrait view we have: origin center, +x right, +y up
# P1 is bottom left, P2 is top right
RO(90)
IP()
# SVG coordinate system: origin is top left, +x is right, +y is down
# scale isotropic; new coordinate system: center top left (y down), 1410 width, 1000 height
# SC x_min, x_max,  y_min, y_max, type   (x_min, y_min are mapped onto p1; x_max, y_max are mapped onto p2)
SC(      0, width, height,     0,    1)

SP(1)
i = 1
circs.reverse()
for circ in circs:
    p = ( (float(circ.attrib['cx']) - width/2) * SCALE + width/2, (float(circ.attrib['cy']) - height/2) * SCALE + height/2 )
    print(f'circle {i}/{len(circs)}')
    # print(points)
    PA(*p) # move to point
    PD()
    PU()
    i += 1
    # input("Press Enter to continue...")
SP(0)
input("Press Enter to finish...")

SP(1)
i = 1
for poly in polys:
    points = parse_points( poly.attrib['points'] )
    print(f'poly {i}/{len(polys)}:   {len(points)} points')
    # print(points)
    fp = points[0]  # first point
    PA(*fp) # move to first point
    for p in points:
        PD(*p)
    PA(*fp) # move to fist point again (to close the path)
    PU() # pen up
    i += 1
    # input("Press Enter to continue...")

SP(0)
input("Press Enter to finish...")
close()

