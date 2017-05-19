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
