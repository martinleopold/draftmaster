# platonic solid coordinates (unfinished #TODO)

from math import sqrt

# Tetrahedron (4)
# https://en.wikipedia.org/wiki/Tetrahedron#Coordinates_for_a_regular_tetrahedron
# Expressed symmetrically as 4 points on the unit sphere, centroid at the origin, with lower face level, the vertices are
tetra = [ 
    (  sqrt(8/9),          0, -1/3 ), # v1
    ( -sqrt(2/9),  sqrt(2/3), -1/3 ), # v2
    ( -sqrt(2/9), -sqrt(2/3), -1/3 ), # v3
    (          0,          0,    1 )  # v4
]

# Hexahedron (6, Cube)
# Cube inscribed in unit sphere, centroid at origin (x+..right, y+..up, z+..towards viewer)
sh = sqrt(1/2)
hexa = [
    (  sh,  sh,  sh ), # top, right, front
    (  sh,  sh, -sh ), # top, right, back
    ( -sh,  sh, -sh ), # top, left,  back
    ( -sh,  sh,  sh ), # top, left,  front
    (  sh, -sh,  sh ), # bottom, right, front
    (  sh, -sh, -sh ), # bottom, right, back
    ( -sh, -sh, -sh ), # bottom, left,  back
    ( -sh, -sh,  sh )  # bottom, left,  front
]

# Octahedron (8)
# https://en.wikipedia.org/wiki/Octahedron#Cartesian_coordinates
# ...placed with its center at the origin and its vertices on the coordinate axes
octa = [
    ( 1,  0,  0), # base, right
    (-1,  0,  0), # base, left
    ( 0,  1,  0), # top
    ( 0, -1,  0), # bottom
    ( 0,  0,  1), # base, front
    ( 0,  0, -1)  # base, back
]

# Dodecahedron (12)
# https://en.wikipedia.org/wiki/Regular_dodecahedron#Cartesian_coordinates
phi = ( 1 + sqrt(5) ) / 2
dodeca = [
    ( 1,  1,  1),
    ( 1,  1, -1),
    ( 1, -1,  1),
    ( 1, -1, -1),
    (-1,  1,  1),
    (-1,  1, -1),
    (-1, -1,  1),
    (-1, -1, -1),
    
    (0,  phi,  1/phi),
    (0,  phi, -1/phi),
    (0, -phi,  1/phi),
    (0, -phi, -1/phi),
    
    ( 1/phi, 0,  phi),
    ( 1/phi, 0, -phi),
    (-1/phi, 0,  phi),
    (-1/phi, 0, -phi),
    
    ( phi,  1/phi, 0),
    ( phi, -1/phi, 0),
    (-phi,  1/phi, 0),
    (-phi, -1/phi, 0),
]

# Icosahedron (20)
# https://en.wikipedia.org/wiki/Regular_icosahedron#Cartesian_coordinates
icosa = [
    (0,  1,  phi), ( phi, 0,  1), (1,   phi,   0),
    (0,  1, -phi), (-phi, 0,  1), (1,  -phi,   0),
    
    (0, -1,  phi), ( phi, 0, -1), ( 0,   -1, phi),
    (0, -1, -phi), (-phi, 0, -1), (-1, -phi,   0),
]
