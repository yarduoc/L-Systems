##Import

from numpy import *
from numpy import concatenate
from numpy.linalg import det

##Plan

def det_3D(v1,v2,v3,precision = 3):
    matrix = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),v3.coordinates.copy()),1)
    return round(linalg.det(matrix),precision)

class Mesh :
    
    axes   = []
    origin = Euclidian_Space_Vector((1,1,1))
    
    def __init__( self , triple):
        origin = Euclidian_Space_Vector(triple[0])
        dot1 = Euclidian_Space_Vector(triple[1])
        dot2 = Euclidian_Space_Vector(triple[2])
        self.origin = origin
        self.axes.append(dot1-origin)
        self.axes.append(dot2-origin)
    

class Triangular_Mesh (Mesh):
    
    def __init__(self, triple):
        super().__init__(triple)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(axes[0],axes[1])
        vector_x = det_3D(relative_vector,axes[1],z)/det_3D(axes[0],axes[1],z)
        vector_y = det_3D(axes[0],relative_vector,z)/det_3D(axes[0],axes[1],z)
        return vector_x > 0 and vector_y > 0 and vector_x + vector_y < 1

class Square_Mesh (Mesh):
    
    def __init__(self,triple):
        super().__init__(triple)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(axes[0],axes[1])
        vector_x = det_3D(relative_vector,axes[1],z)/det_3D(axes[0],axes[1],z)
        vector_y = det_3D(axes[0],relative_vector,z)/det_3D(axes[0],axes[1],z)
        return vector_x > 0 and vector_y > 0 and vector_x <1 and vector_y < 1


##Droite

    
class Line:
    direction = Euclidian_Space_Vector((1,0,0))
    origin    = Euclidian_Space_Vector((0,0,0))
    def __init__(self , direction , origin):
        self.direction = direction
        self.origin = origin


##

def resolution(mesh, line):
    v1,v2,v3 = mesh.axes[0],mesh.axes[1],line.direction*(-1)
    matrix_system = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),v3.coordinates.copy()),1)
    p1,p2 = mesh.origin, line.origin
    matrix_column = (p2-p1).coordinates.copy()
    if det_3D(v1,v2,v3) == 0:
        "Pas d'intersection"
    else:
        A = linalg.solve(matrix_system,matrix_column)
        M = matrix((0,0,0)).T
        matrix_mesh = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),M),1)
        return dot(matrix_mesh,A)+p1.coordinates.copy()
