import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Turtle_3D import *
from CONFIG import *

force = 0.5

def wind(vecteur):
    v = vecteur.get_copy()
    n = v.get_norm()
    v2 = v + Euclidian_Space_Vector((force,0,0))
    v2.normalise()
    v2 *= n
    return v2

GE = Environment()
#GE.add_physical_object(Physical_Volume("C:\\GitHub\\L-Systems\\Environment-sensitive\\ceci_nest_pas_un_cube.stl"))
GE.add_growth_modifier(GM_Parallelepiped(Euclidian_Space_Vector((-200,-200,15)),Euclidian_Space_Vector((400,0,0)),Euclidian_Space_Vector((0,400,0)),Euclidian_Space_Vector((0,0,400)),wind ))
t = Turtle3D(GE)
