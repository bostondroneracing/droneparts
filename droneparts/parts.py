from solid import *
from solid.utils import *

#min outside radius needed around the mounting hole 

INDUCTRIX_FC_MOUNTING_HOLE_OR=4.32/2.0
INDUCTRIX_FC_MOUNTING_HOLE_R = 1.2/2.0
INDUCTRIX_HOLE_TO_HOLE_D=25
INDUCTRIX_HOLE_TO_HOLE_W = INDUCTRIX_HOLE_TO_HOLE_H = math.hypot(INDUCTRIX_HOLE_TO_HOLE_D, INDUCTRIX_HOLE_TO_HOLE_D)


CRAZYPONY_LENS_BARREL_R = (7.06/2.0)
CRAZYPONY_LENS_BARREL_H =1.5 
CRAZYPONY_LENS_R = 5.0
CRAZYPONY_LENS_H = 3.42 
CRAZYPONY_CAMERA_PCB_W =  14.6
CRAZYPONY_CAMERA_PCB_H = 12.09
CRAZYPONY_CAMERA_PCB_THICKNESS = 5.4 #0.88

DIPOLE_ANTENNA_L = 27
DIPOLE_ANTENNA_R = (5.23/2.0)

def inductrix_fc_hole_puncher(part, thickness=100):
    return part - translate([0, INDUCTRIX_HOLE_TO_HOLE_H/2.0, -1]) (
            cylinder(h = thickness + 2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
        ) - translate([-INDUCTRIX_HOLE_TO_HOLE_W/2.0, 0, -1]) (
            cylinder(h = thickness+2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
        ) - translate([INDUCTRIX_HOLE_TO_HOLE_W/2.0, 0, -1]) (
            cylinder(h = thickness+2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
        ) 
    
#    translate([0, INDUCTRIX_HOLE_TO_HOLE_H/2.0, -1]) (
#            cylinder(h = thickness + 2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
#        ) - translate([-INDUCTRIX_HOLE_TO_HOLE_W/2.0, 0, -1]) (
#            cylinder(h = thickness+2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
#        ) - translate([INDUCTRIX_HOLE_TO_HOLE_W/2.0, 0, -1]) (
#            cylinder(h = thickness+2, r= INDUCTRIX_FC_MOUNTING_HOLE_R)
#        ) 

#TODO define antenna 
def crazypony_camera_tx(antenna_length, antenna_radius, pcb_width, pcb_height, pcb_thickness): 
    tx = union()(
        translate([0, 0, 0]) (
            cube([pcb_width, pcb_height, pcb_thickness ], True)
        ),
        translate([-pcb_width/2 + antenna_radius, pcb_height/2, 0])(
            rotate([-90, 0, 0]) (
                cylinder(h=antenna_length, r=antenna_radius)
            )
        )
    )
    return tx


def crazypony_camera():
    lens_barrel_height = CRAZYPONY_LENS_BARREL_H
    lens_barrel_radius = CRAZYPONY_LENS_BARREL_R
    lens_height = CRAZYPONY_LENS_H
    lens_radius = CRAZYPONY_LENS_R
    pcb_width = CRAZYPONY_CAMERA_PCB_W
    pcb_depth = CRAZYPONY_CAMERA_PCB_H

    pcb_thickness =CRAZYPONY_CAMERA_PCB_THICKNESS# 0.88
    camera = union()(
        translate([0, 0, pcb_thickness/2.0])(
            cube([pcb_width, pcb_depth, pcb_thickness ], True)
        ),
        translate([0, 0, pcb_thickness])(
            cylinder(h=lens_barrel_height, r=lens_barrel_radius)
        ),
        translate([0, 0, lens_barrel_height + pcb_thickness])(
            cylinder(h=lens_height, r=lens_radius)
        )
    )
    return camera
