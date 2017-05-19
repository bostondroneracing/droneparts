from solid import *
from solid.utils import *
from .hardware import *

""" Distance adjacent holes """
INDUCTRIX_HOLE_TO_HOLE_D = 25.4
INDUCTRIX_HOLE_TO_HOLE_W = INDUCTRIX_HOLE_TO_HOLE_H = math.hypot(INDUCTRIX_HOLE_TO_HOLE_D, INDUCTRIX_HOLE_TO_HOLE_D)
INDUCTRIX_FC_MOUNTING_HOLE_R = SCREW_R

def inductrix_hole_punch(part):
    """
    Add mounting holes to part. Part must be centered
    """
    thickness = 100
    hole = cylinder(h = thickness, r = INDUCTRIX_FC_MOUNTING_HOLE_R,
                    center=True)
    x = INDUCTRIX_HOLE_TO_HOLE_D/2.0
    y = INDUCTRIX_HOLE_TO_HOLE_D/2.0
    return difference()(
        part,
        translate([x, y, 0])(hole),
        translate([-x, y, 0])(hole),
        translate([-x, -y, 0])(hole),
        translate([x, -y, 0])(hole),
    ) 

