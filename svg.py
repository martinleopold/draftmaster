'''
plot polygons from SVG
used to plot cover image from FH Technikum Wissensbilanz 2019/20
'''
import os as _os
import re as _re
import xml.etree.ElementTree as _ET

def rmns(tag):
    '''Remove namespace (eg. {http://example.com}) from tag'''
    return _re.sub(r'\{[^\}]*\}', '', tag)
    
def parse(filepath_or_svgtext):
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

def elements(filepath_or_svgtext, tags=[]):
    '''Get flat list of elements contained in an SVG file
    filepath_or_svgtext: Path to an SVG file or SVG text.
    tags: List of tags to return. If empty (default) return all elements.
    Returns root element and list of xml.etree.ElementTree.Element.
    '''
    root = parse(filepath_or_svgtext)
    els = root.iter()
    if tags: els = filter(lambda el: el.tag in tags, els)
    return root, list(els)

def parse_linestrip_path(d):
    '''parse pathdata for a linestrip
    i.e. one M followed by L commands and an optional final Z i.e. ML+Z?
    returns: tuple of x,y coordiantes
    '''
    d = d.strip()
    close = d.endswith('Z')
    d = _re.sub(r'[MLZ]', ' ', d).strip()
    d = d.split(' ')
    d = list( map(lambda x: tuple(map(float, x.split(','))), d) )
    if close: d.append(d[0])
    return d

def parse_viewbox(s):
    viewBox = s.split(' ')
    viewBox = tuple(map(float, viewBox))
    return viewBox

'''
def parse_points(str):
    p = _re.split(',|\s+', str)
    p = list( map(float, p) ) # raw list of coordinates
    a = iter(p)
    pointlist = [ ( (x - width/2) * SCALE + width/2, (y - height/2) * SCALE + height/2) for x, y in zip(a, a) ]
    return pointlist
'''

'''
root, polys = svg_elements('svg/2021-02-01_14-53-31-633.svg', ['polygon'])
root, circs = svg_elements('svg/2021-02-01_14-53-31-633.svg', ['circle'])
# print(root)

print('polygons:', len(polys))
print('circles: ', len(circs))

viewBox = root.attrib['viewBox'].split(' ')
viewBox = tuple(map(float, viewBox))
left, top, width, height = viewBox
print(viewBox)
'''