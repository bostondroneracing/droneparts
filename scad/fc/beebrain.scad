$fn = 12;

union() {
	difference() {
		cube(center = true, size = [29, 29, 0.8000000000]);
		translate(v = [12.7000000000, 12.7000000000, 0]) {
			cylinder(center = true, h = 100, r = 0.6000000000);
		}
		translate(v = [-12.7000000000, 12.7000000000, 0]) {
			cylinder(center = true, h = 100, r = 0.6000000000);
		}
		translate(v = [-12.7000000000, -12.7000000000, 0]) {
			cylinder(center = true, h = 100, r = 0.6000000000);
		}
		translate(v = [12.7000000000, -12.7000000000, 0]) {
			cylinder(center = true, h = 100, r = 0.6000000000);
		}
	}
	translate(v = [0, 0, 0.9000000000]) {
		cube(center = true, size = [21.0800000000, 21.0800000000, 1]);
	}
	translate(v = [7.6008621971, 7.6008621971, 0]) {
		rotate(a = [180, 0, -45]) {
			color(c = [0, 0, 1]) {
				translate(v = [0, -1.5000000000, 2.9000000000]) {
					cube(center = true, size = [8.2000000000, 3, 5.8000000000]);
				}
			}
		}
	}
	union() {
		translate(v = [-4.9900000000, 12.6000000000, -0.4000000000]) {
			rotate(a = [180, 0, 0]) {
				color(c = [1, 0, 0]) {
					translate(v = [0, 0, 2.8000000000]) {
						cube(center = true, size = [7.7000000000, 3.8000000000, 5.6000000000]);
					}
				}
			}
		}
		translate(v = [4.9900000000, -12.6000000000, -0.4000000000]) {
			rotate(a = [180, 0, 0]) {
				color(c = [1, 0, 0]) {
					translate(v = [0, 0, 2.8000000000]) {
						cube(center = true, size = [7.7000000000, 3.8000000000, 5.6000000000]);
					}
				}
			}
		}
		translate(v = [12.6000000000, -4.9900000000, -0.4000000000]) {
			rotate(a = [180, 0, 90]) {
				color(c = [1, 0, 0]) {
					translate(v = [0, 0, 2.8000000000]) {
						cube(center = true, size = [7.7000000000, 3.8000000000, 5.6000000000]);
					}
				}
			}
		}
		translate(v = [-12.6000000000, 4.9900000000, -0.4000000000]) {
			rotate(a = [180, 0, 90]) {
				color(c = [1, 0, 0]) {
					translate(v = [0, 0, 2.8000000000]) {
						cube(center = true, size = [7.7000000000, 3.8000000000, 5.6000000000]);
					}
				}
			}
		}
	}
	translate(v = [-6.5000000000, 6.5000000000, -0.4000000000]) {
		rotate(a = [180, 0, 45]) {
			color(c = [0, 0, 0]) {
				translate(v = [0, 0, 1.0000000000]) {
					cube(center = true, size = [1.5000000000, 3, 2]);
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *
from droneparts.fc import *
import os

SEGMENTS = 12
SCAD_ROOT = "../scad/"
SCAD_SUFFIX = ".scad"

parts = [ {'name': 'beebrain', 'category': 'fc', 'model': BeeBrain()}] 
def build():
    for part in parts:
        filename = part['name'] + SCAD_SUFFIX
        file = os.path.join(os.path.join(SCAD_ROOT, part['category']),
                            filename)
        file_header = '$fn = {};'.format(SEGMENTS)
        scad_render_to_file(part['model'].make(),  filepath = file, file_header =
                            file_header)




if __name__ == "__main__":
    build()
 
 
************************************************/
