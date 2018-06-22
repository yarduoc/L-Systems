## Physical_Volume Object

""" 
Defines a physical volume in a 3D space using a stl mesh. Includes a raycast
function on these physical volumes meshes.
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import Euclidian_Space_Vector
from Geometry import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

class Physical_Volume :
    
    """ 
    Physical_Volume( stl_path)
    
    Returns a Physical_Volume from a stl file. Physical volumes can be interpreted
    as solid volumes of the environment. Includes a raycast function.
    
    Parameters
    ----------
    stl_path : string
        This string is the local path to the .stl file you want to use as a model
        for your physical volume.
        
    """
    
    mesh_3D = None
    list_of_meshes = []
    
    def __init__( self, stl_path):
        self.mesh_3D = mesh.Mesh.from_file(stl_path)
        for coords_array in self.mesh_3D.points :
            coords_array = coords_array.tolist()
            triple = (coords_array[:3],coords_array[3:6],coords_array[6:9])
            m = Triangular_Mesh(triple)
            self.list_of_meshes.append(m)
        
    ## Raycast function

    def hit_by_raycast( self, origin, direction):
        faces_hit = []
        for triangle in self.list_of_meshes :
            intersection = resolution(triangle, Line( direction, origin))
            if intersection is not None :
                distance = (origin - intersection).get_norm()
                #To be valid, an intersection has to be in the traingle and close
                #enough so the segment actually intersects the triangle
                if triangle.is_in(intersection) and distance <= direction.get_norm():
                    faces_hit.append((distance, intersection))
        return faces_hit

    