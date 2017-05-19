from solid import *
from solid.utils import *

SCREW_HEAD_R=4.32/2.0
SCREW_R = 1.2/2.0
SCREW_L = 4.48
SCREW_THREAD_L = 4

def screw():
    return union()(
        cylinder(h=SCREW_THREAD_L, r = SCREW_R),
        translate([0, 0, SCREW_THREAD_L])(
            cylinder(h=SCREW_L - SCREW_THREAD_L, r = SCREW_HEAD_R)
        )
    )
