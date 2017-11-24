## Turtle 3D by Yarduoc
import bpy

from numpy import *

class Euclidian_Space_Vector :
    
    """ Allow the user to manipulate a vector in a 3-dimensional Euclidian Space """
    
    dimension = None            #int between in [1,2,3]
    coordinates = []            #float list of coordinates
    
    # Default access indexes for the 3 first coordinates
    X = 0
    Y = 1
    Z = 2
    
    def __init__( self, dimension):
        self.dimension = dimension
        coordinates = matrix([[0] for _ in range(self.dimension)])
    
    
    # Setting coordinates in a specific coordinates system
    
    def set_coordinates_cartesian( self, coordinates):
        if len(coordinates) != self.dimension :
            print("Parameter error, coordinates don't match dimension")
        self.coordinates = matrix([[coordinates[k]] for k in range(self.dimension)])
        
        
    def set_coordinates_spherical( self, coordinates): #WIP
        pass
    def set_coordinates_cylindrical( self, coordinates): #WIP
        pass
        
    # Operations on vector
    
    def translate( self, vector):
        self.coordinates = self.coordinates + vector.coordinates
    
    def homothety( self, value):
        self.coordinates = self.coordinates * value
    
    def rotate( self, angle, axis=0):
        if self.dimension == 2:
            self.coordinates = Euclidian_Space_Vector.__get_rotation_matrix_2D(angle)*self.coordinates
        elif axis == Euclidian_Space_Vector.X :
            self.coordinates = Euclidian_Space_Vector.__get_X_rotation_matrix_3D(angle)*self.coordinates
        elif axis == Euclidian_Space_Vector.Y :
            self.coordinates = Euclidian_Space_Vector.__get_Y_rotation_matrix_3D(angle)*self.coordinates
        elif axis == Euclidian_Space_Vector.Z :
            self.coordinates = Euclidian_Space_Vector.__get_Z_rotation_matrix_3D(angle)*self.coordinates
        else :
            print( "Error, Invalid Axis Value")
        Euclidian_Space_Vector.__matrix_simplification(self)
    
    def test(self):
        print (Euclidian_Space_Vector.__get_rotation_matrix_2D(90))
        
    def normalise( self):
        self = self.homothety(1/self.get_norm())
    
    # Informations on vector
    
    def get_norm( self):
        sum = 0
        for k in nditer(self.coordinates):
            sum += k**2
        return sqrt(sum)
        
    def get_homothetic_vector( self, value):
        new_vector = Euclidian_Space_Vector.get_copy_vector( self)
        new_vector.homothety( value)
        return new_vector
    
    def to_tuple( self):
        return tuple(self.coordinates.transpose().tolist()[0])
        
    # External Methods
    
    def get_vector( coordinates):
        dimension = len( coordinates)
        vector = Euclidian_Space_Vector(dimension)
        vector.set_coordinates_cartesian(coordinates)
        return vector
    
    def get_copy_vector( vector):
        return Euclidian_Space_Vector.get_vector(vector.coordinates.transpose().tolist()[0])
    
    # Internal Sub-Methods
    
    def __get_rotation_matrix_2D( theta):
        theta = radians(theta)
        return matrix([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
        
    def __get_X_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]])
    def __get_Y_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]])
    def __get_Z_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[cos(theta),-sin(theta),0],[sin(theta),cos(theta),0],[0,0,1]])
    
    def __matrix_simplification( vector):
        # simplifies coordinates matrixes when values are near to 0
        matrix = vector.coordinates
        for k in range(matrix.shape[0]):
            for l in range(matrix.shape[1]):
                if abs(matrix[k,l])<10**(-15):
                    matrix[k,l]=0.
    
    def __repr__(self):
        representation = "("
        for k in nditer(self.coordinates):
            representation += str( k)+","
        representation = representation[:-1] + ")"
        return representation
    

class turtle3D :
    
    stored_lines        = []  
    is_down             = True      
    line_thickness      = 1
    current_position    = Euclidian_Space_Vector(3)
    current_orientation = Euclidian_Space_Vector(3)
    
        
    def __init__( self, coords = (0,0,0), orientation = (1,0,0)):
        self.stored_points = []
        self.current_position = Euclidian_Space_Vector.get_vector(coords)
        self.current_orientation = Euclidian_Space_Vector.get_vector(orientation)
        self.current_orientation.normalise()
    
    # Turtle execution methods 
    
    def forward( self, length=1):
        current_position_copy = Euclidian_Space_Vector.get_copy_vector( self.current_position)
        self.current_position.translate( self.current_orientation.get_homothetic_vector( length))
        if self.is_down:
            self.stored_lines.append((current_position_copy.to_tuple(),self.current_position.to_tuple(),self.line_thickness))
            
    def backward( self, length=1):
        self.forward(-length)
    
    def rotate_X(self, angle):
        self.current_orientation.rotate(angle,Euclidian_Space_Vector.X)
        
    def rotate_Y(self, angle):
        self.current_orientation.rotate(angle,Euclidian_Space_Vector.Y)
        
    def rotate_Z(self, angle):
        self.current_orientation.rotate(angle,Euclidian_Space_Vector.Z)
    
    def goto( self, coordinates):
        if self.is_down :
            stored_lines.append((self.current_position.to_tuple(),Euclidian_Space_Vector.get_vector(coordinates).to_tuple(),self.line_thickness))
        self.set_position( coordinates)
    
    # Methods setting parameters
    
    def set_position( self, coordinates):
        self.current_position = Euclidian_Space_Vector.get_vector(coordinates)
    def set_orientation( self, orientation):
        self.current_orientation = Euclidian_Space_Vector.get_vector(orientation)
    def set_thickness(self, value):
        self.line_thickness = value
    
    # Blender
    
    def cylindre_entre_points( p1, p2, rayon):
    
    
        x1,y1,z1 = p1[0], p1[1], p1[2]
        x2,y2,z2 = p2[0], p2[1], p2[2]
    
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
    
        dist = sqrt(dx**2 + dy**2 + dz**2)
    
        bpy.ops.mesh.primitive_cylinder_add(
            radius = rayon,
            depth = dist,
            location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)
        )
    
        phi = arctan2(dy,dx)
        theta = arccos(dz/dist)
    
        bpy.context.object.rotation_euler[1] = theta
        bpy.context.object.rotation_euler[2] = phi
    
    def taille ( liaisons):
    
    
        [xmin,ymin,zmin] = liaisons[0][0]
        [xmax,ymax,zmax] = liaisons[0][0]
        
        for liaison in liaisons:
            
            [(x1,y1,z1),(x2,y2,z2),rayon] =  liaison
            
            xmin = min(xmin, min(x1,x2))
            xmax = max(xmax, max(x1,x2))
            ymin = min(ymin, min(y1,y2))
            ymax = max(ymax, max(y1,y2))
            zmin = min(zmin, min(z1,z2))
            zmax = max(zmax, max(z1,z2))
            

        return max (abs(xmax-xmin), abs(ymax - ymin), abs(zmax-zmin))
    
    def redimensionner(liaisons, dim):
        
        coef = dim / (self.taille(liaisons))
        
        for k in range (len(liaisons)) :
            
            [(x1,y1,z1),(x2,y2,z2),rayon] =  liaisons[k]
        
            x1 *= coef
            x2 *= coef
            y1 *= coef
            y2 *= coef
            z1 *= coef
            z2 *= coef
            rayon *= coef
            
            liaisons[k] = [(x1,y1,z1),(x2,y2,z2),rayon]
            
        return liaisons
    
    def blender_print ( self ,dimension):
        
        liaisons = self.redimensionner (self.stored_lines , dimension)
        
        for liaison in liaisons:
            
            [p1,p2,rayon] =  liaison
            
            self.cylindre_entre_points(p1,p2,rayon)
        
        
T = turtle3D()

T.set_orientation((0,0,1))

for _ in range (4) :
    
    T.forward(5)

    T.rotate_Y (90)

T.blender_print(5)
