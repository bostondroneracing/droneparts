from solid import *
from solid.utils import *
from .frame import *
from .hardware import *

BEEBRAIN_W = 29
BEEBRAIN_H = BEEBRAIN_W 
BEEBRAIN_PCB_THICKNESS = 0.8


class FC(object):
    def __init__(self):
        pass

class MicroUSB(object):
    x = 8.2
    y = 3
    z = 5.8
    def  make(self):
        return translate([0, -self.y/2.0, self.z/2.0])(cube([self.x, self.y,
                                                             self.z], center=True))
class PicoFemaleConnector(object):
    x = 7.7
    y = 3.8 
    z = 5.6
    def make(self):
        return translate([0, 0, self.z/2.0])(cube([self.x, self.y, self.z], center=True))

class BindButton(object):
    x = 1.5
    y = 3
    z = 2
    def make(self):
        return translate([0, 0, self.z/2.0])(cube([self.x, self.y, self.z], center=True))

class BeeBrain(FC):
    def __init__(self):
        super(FC, self).__init__()

    def make(self):
        pcb = cube([BEEBRAIN_W, BEEBRAIN_H, BEEBRAIN_PCB_THICKNESS],
                   center=True)
        
        pcb = inductrix_hole_punch(pcb)

        component_w = component_h = INDUCTRIX_HOLE_TO_HOLE_D - (SCREW_HEAD_R*2.0)
        top_component_h = 1
        top_components = translate([0, 0, top_component_h/2.0 +
                                    BEEBRAIN_PCB_THICKNESS/2.0]) (
                                        cube([component_w, component_h,top_component_h], center=True) 
                                    )

        micro_usb = MicroUSB()
        usb_padding = 4
        usb_x =  BEEBRAIN_W/2.0 - usb_padding - math.cos(math.radians(45)) * micro_usb.x/2.0
        usb_y =  BEEBRAIN_H/2.0 - usb_padding - math.sin(math.radians(45)) * micro_usb.x/2.0
        usb = translate([usb_x, usb_y, 0])(
            rotate([180, 0, -45])(  
                color(Blue)(micro_usb.make())
            )
        )

        header_offset_x = 5.66
        header = PicoFemaleConnector()
        header_offset_z = -BEEBRAIN_PCB_THICKNESS/2.0
        headers = union()(
            #bottom left
            translate([-BEEBRAIN_W/2.0 + header.x/2.0 + header_offset_x,
                      BEEBRAIN_H/2.0 - header.y/2.0,
                      header_offset_z])(
                          rotate([180, 0, 0])(
                              color(Red)(header.make())
                          )
                      ),

            #top right
            translate([BEEBRAIN_W/2.0 - header.x/2.0 - header_offset_x,
                      -BEEBRAIN_H/2.0 + header.y/2.0,
                      header_offset_z])(
                          rotate([180, 0, 0])(
                              color(Red)(header.make())
                          )
                      ),
            translate([BEEBRAIN_W/2.0 - header.y/2.0,
                      -BEEBRAIN_H/2.0 + header.x/2.0 + header_offset_x,
                      header_offset_z])(
                          rotate([180, 0, 90])(
                              color(Red)(header.make())
                          )
                      ),
            translate([-BEEBRAIN_W/2.0 + header.y/2.0,
                      BEEBRAIN_H/2.0 - header.x/2.0 -  header_offset_x,
                      header_offset_z])(
                          rotate([180, 0, 90])(
                              color(Red)(header.make())
                          )
                      )
        )

        #8.3 from hole
        bind_button = BindButton()
        button_x = button_y = BEEBRAIN_W/2.0 - 8 
        button = translate([-button_x, button_y, header_offset_z])(
            rotate([180, 0, 45])(color(Black)(bind_button.make()))
        )
        return union()(
            pcb,
            top_components,
            usb,
            headers,
            button
        )
