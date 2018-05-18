import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Turtle_3D import *
from CONFIG import *

GE = Environment()
GE.add_physical_object(Physical_Volume("C:\\GitHub\\L-Systems\\Environment-sensitive\\ceci_nest_pas_un_cube.stl"))
t = Turtle3D(GE)
