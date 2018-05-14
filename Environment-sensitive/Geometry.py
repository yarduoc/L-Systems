##Import

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import *
from numpy import concatenate
from numpy.linalg import det

##Plane

def det_3D(v1,v2,v3,precision = 3):
    matrix = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),v3.coordinates.copy()),1)
    return round(det(matrix),precision)

    
class Triangular_Mesh:
    
    axes   = []
    origin = Euclidian_Space_Vector((1,1,1))
    
    def __init__( self , triple):
        origin = Euclidian_Space_Vector(triple[0])
        dot1 = Euclidian_Space_Vector(triple[1])
        dot2 = Euclidian_Space_Vector(triple[2])
        self.origin = origin
        self.axes.append(dot1-origin)
        self.axes.append(dot2-origin)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(axes[0],axes[1])
        vector_x = det_3D(relative_vector,axes[1],z)/det_3D(axes[0],axes[1],z)
        vector_y = det_3D(axes[0],relative_vector,z)/det_3D(axes[0],axes[1],z)
        return vector_x > 0 and vector_y > 0 and vector_x + vector_y < 1
        


##Line

class Line:
    direction = Euclidian_Space_Vector((1,0,0))
    origin    = Euclidian_Space_Vector((0,0,0))
    def __init__(self , direction , origin):
        self.direction = direction
        self.origin = origin


##Fonction de Résolution


def resolution( mesh, line):
    if det_3D( mesh.axes[0], mesh.axes[1], line.direction) == 0 :
        return "Pas de point d'intersection unique"
    
    
    
    system = column_stack((plane.axes[0].coordinates.copy(),plane.axes[1].coordinates.copy(),line.direction.coordinates.copy()))
    origin = plane.origin.coordinates.copy() + line.origin.coordinates.copy()
    if linalg.det( system) != 0:
        A = linalg.solve( system , origin)
        plane_system = column_stack((plane.axes[0].coordinates.copy(),plane.axes[1].coordinates.copy(), matrix([[0],[0],[0]])))
        sol = dot(plane_system,A) - plane.origin.coordinates
        return Euclidian_Space_Vector( sol.transpose().tolist()[0])
    else:
        return "Pas de solution"

def in_segment( line, point):
    return (point-line.origin).get_norm() < line.direction.get_norm()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

