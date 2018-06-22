## Geometry Classes and Functions

""" 
Defines classes and functions to be used as geometry tools (for the raycast or the
triangularisation of a Physical_Volume mesh
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from numpy import concatenate
from numpy.linalg import det
from Euclidian_Space_Vector import Euclidian_Space_Vector

## Classes

class Mesh :
    
    """ 
    Mesh( triple)
    
    Returns a plane mesh. This class is not made to be instanciated,
    but rather to serve as a base to create custom finite surfaces
    
    Parameters
    ----------
    triple : numeral iterable iterable
        The three first elements of each of the three first elements of this iterable
        are considered as the coordinates of the three points describing the plane
   
    """
    
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
    
    """ 
    Triangular_Mesh( triple)
    
    Returns a triangular mesh. This mesh geometry is used in Physical_Volumes to
    represent the triangularisation of the mesh
    
    Parameters
    ----------
    triple : numeral iterable iterable
        The three first elements of each of the three first elements of this iterable
        are considered as the coordinates of the three points describing the triangle
        
    """
    
    def __init__(self, triple):
        super().__init__(triple)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(axes[0],axes[1])
        vector_x = det_3D(relative_vector,axes[1],z)/det_3D(axes[0],axes[1],z)
        vector_y = det_3D(axes[0],relative_vector,z)/det_3D(axes[0],axes[1],z)
        return vector_x > 0 and vector_y > 0 and vector_x + vector_y < 1

class Square_Mesh (Mesh):
    
    """ 
    Square_Mesh( triple)
    
    Returns a square mesh. 
    
    Parameters
    ----------
    triple : numeral iterable iterable
        The three first elements of each of the three first elements of this iterable
        are considered as the coordinates of the three points describing the square
        (the fourth point is computable given those three)
        
    """
    
    def __init__(self,triple):
        super().__init__(triple)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(axes[0],axes[1])
        vector_x = det_3D(relative_vector,axes[1],z)/det_3D(axes[0],axes[1],z)
        vector_y = det_3D(axes[0],relative_vector,z)/det_3D(axes[0],axes[1],z)
        return vector_x > 0 and vector_y > 0 and vector_x <1 and vector_y < 1
    
class Line:
    
    """ 
    Line( direction, origin)
    
    Returns a line representing object. 
    
    Parameters
    ----------
    direction : numeral iterable
        The three first elements of this iterable represent the coordinates of 
        the directional vector of the line
    origin : numeral iterable
        The three first elements of this iterable represent the coordinates of 
        the origin point of the line
        
    """
    
    direction = Euclidian_Space_Vector((1,0,0))
    origin    = Euclidian_Space_Vector((0,0,0))
    def __init__(self , direction , origin):
        self.direction = direction
        self.origin = origin


## Functions

def det_3D(v1,v2,v3,precision = 3):
    matrix = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),v3.coordinates.copy()),1)
    return round(linalg.det(matrix),precision)









def resolution(mesh, line):
    v1,v2,v3 = mesh.axes[0],mesh.axes[1],line.direction*(-1)
    matrix_system = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),v3.coordinates.copy()),1)
    p1,p2 = mesh.origin, line.origin
    matrix_column = (p2-p1).coordinates.copy()
    if det_3D(v1,v2,v3) == 0:
        None
    else:
        A = linalg.solve(matrix_system,matrix_column)
        M = matrix((0,0,0)).T
        matrix_mesh = concatenate((v1.coordinates.copy(),v2.coordinates.copy(),M),1)
        solution_vector = dot(matrix_mesh,A)+p1.coordinates.copy()
        return Euclidian_Space_Vector((solution_vector.T).tolist()[0])