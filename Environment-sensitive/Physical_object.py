import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import *
from Geometry_2 import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
test = "C:\\GitHub\\L-Systems\\Environment-sensitive\\ceci_nest_pas_un_cube.stl"


class Mesh :
    
    axes   = []
    origin = Euclidian_Space_Vector((1,1,1))
    
    def __init__( self , triple):
        origin = Euclidian_Space_Vector(triple[0])
        dot1 = Euclidian_Space_Vector(triple[1])
        dot2 = Euclidian_Space_Vector(triple[2])
        self.origin = origin
        self.axes = []
        self.axes.append(dot1-origin)
        self.axes.append(dot2-origin)
    

class Triangular_Mesh (Mesh):
    
    def __init__(self, triple):
        super().__init__(triple)
    
    def is_in( self, vector):
        relative_vector = vector - self.origin
        z = Euclidian_Space_Vector.vectorial_product(self.axes[0],self.axes[1])
        vector_x = det_3D(relative_vector,self.axes[1],z)/det_3D(self.axes[0],self.axes[1],z)
        vector_y = det_3D(self.axes[0],relative_vector,z)/det_3D(self.axes[0],self.axes[1],z)
        return vector_x >= 0 and vector_y >= 0 and vector_x + vector_y <= 1



class Physical_Volume :
    
    mesh_3D = None
    list_of_meshes = []
    
    def __init__( self, stl_path):
        self.mesh_3D = mesh.Mesh.from_file(stl_path)
        for coords_array in self.mesh_3D.points :
            coords_array = coords_array.tolist()
            triple = (coords_array[:3],coords_array[3:6],coords_array[6:9])
            m = Triangular_Mesh(triple)
            self.list_of_meshes.append(m)
            

    def hit_by_raycast( self, origin, direction):
        faces_hit = []
        for triangle in self.list_of_meshes :
            intersection = resolution(triangle, Line( direction, origin))
            if intersection is not None :
                distance = (origin - intersection).get_norm()
                #To be valid, an intersection has to be in the traingle and close enough so the segment actually intersect the triangle
                if triangle.is_in(intersection) and distance <= direction.get_norm() :
                    faces_hit.append((distance, intersection))
        return faces_hit

    