import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Turtle_3D import *
from CONFIG import *

GE = Environment()
#GE.add_physical_object(Physical_Volume("C:\\GitHub\\L-Systems\\Environment-sensitive\\ceci_nest_pas_un_cube.stl"))
GE.add_growth_modifier(GM_Parallelepiped(Euclidian_Space_Vector((0,3,0)),Euclidian_Space_Vector((1000,0,0)),Euclidian_Space_Vector((0,1000,0)),Euclidian_Space_Vector((0,0,1000)),Growth_Modifier_Volume.Halve_Length_Influence ))
t = Turtle3D(GE)
