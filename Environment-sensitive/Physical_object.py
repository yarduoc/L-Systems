
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
test = "C:\\GitHub\\L-Systems\\Environment-sensitive\\ceci_nest_pas_un_cube.stl"

class Physical_Volume :
    
    mesh_3D = None
    list_of_meshes = []
    
    def __init__( self, stl_path):
        self.mesh_3D = mesh.Mesh.from_file(stl_path)
        for coords_array in self.mesh_3D.points :
            triple = (coords_array[:2],coords_array[3:5],coords_array[6:8])
            self.list_of_meshes.append(Triangular_Mesh(triple))

    def hit_by_raycast( origin, direction):
        faces_hit = []
        for triangle in self.list_of_meshes :
            intersection = resolution(triangle, Line( direction, origin))
            if intersection is not None :
                distance = (origin - intersection).get_norm()
                #To be valid, an intersection has to be in the traingle and close enough so the segment actually intersect the triangle
                if triangle.is_in(intersection) and distance < direction.get_norm() :
                    faces_hit.append((distance, intersection))
        return faces_hit

    