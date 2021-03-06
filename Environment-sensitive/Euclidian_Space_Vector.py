
## Euclidian_Space_Vector Object

""" 
Allows the user to manipulate more easily vectors in a 3-Dimension Euclidian Space
"""

from numpy import array
from numpy import matrix
from numpy import nditer
from numpy import radians
from numpy import cross
from numpy import cos
from numpy import sin
from numpy import identity
from math  import sqrt

class Euclidian_Space_Vector :
    
    """ 
    Euclidian_Space_Vector( coordinates = (0,0,0))
    
    Returns a vector from an iterable of size at least 3. 
    Euclidian_Space_Vectors are mathematical 3D vectors with usual operators
    implemented.
    
    Parameters
    ----------
    coordinates : numeral iterable
        The three first elements of this iterable are considered as the
        coordinates of the vector
    
    """
    
    coordinates = matrix([[]])  # column vector representing coordinates
    limit_precision = 10**-15   # limit precision of coordinates (for printing)
    
    ## Construction of vectors
    
    def __init__( self, coordinates = (0,0,0)):
        self.coordinates = matrix([[coordinates[k]] for k in range(3)])
    
    def get_copy(self):
        coordinates_list = self.coordinates.transpose().tolist()[0]
        return Euclidian_Space_Vector(coordinates_list)
        
    def get_homothetic_vector( self, value):
        new_vector = self.get_copy()
        new_vector.homothety( value)
        return new_vector
    
    
    ## Setting coordinates in a specific coordinates system
    
    def set_coordinates_cartesian( self, coordinates):
        if len(coordinates) != 3 :
            print("Parameter error, coordinates don't match dimension")
        self.coordinates = matrix([[coordinates[k]] for k in range(3)])
        
    ## Operations on vector
    
    def translate( self, vector):
        self.coordinates = self.coordinates + vector.coordinates
    
    def homothety( self, value):
        self.coordinates = self.coordinates * value
    
    def rotate( self, angle, axis=0):
        if axis == Euclidian_Space_Vector.X :
            rotation_X = Euclidian_Space_Vector.__get_X_rotation_matrix_3D(angle)
            self.coordinates = rotation_X * self.coordinates
        elif axis == Euclidian_Space_Vector.Y :
            rotation_Y = Euclidian_Space_Vector.__get_Y_rotation_matrix_3D(angle)
            self.coordinates = rotation_Y * self.coordinates
        elif axis == Euclidian_Space_Vector.Z :
            rotation_Z = Euclidian_Space_Vector.__get_Z_rotation_matrix_3D(angle)
            self.coordinates = rotation_Z * self.coordinates
        else :
            print( "Error, Invalid Axis Value")
        self.__matrix_simplification()
        
    def rotate_around_U( self, angle, U):
        rotation_U = Euclidian_Space_Vector.__get_U_rotation_matrix_3D( angle, U)
        self.coordinates = rotation_U * self.coordinates
        
    def normalise( self):
        self = self.homothety(1/self.get_norm())
    
    ## Informations on vector
    
    def get_norm( self):
        sum = 0
        for k in nditer(self.coordinates):
            sum += k**2
        return sqrt(sum)
    
    def get_tuple_representation( self):
        return tuple(self.coordinates.transpose().tolist()[0])
        
    ## Usual Functions on Vectors
    
    def canonical_scalar_product( v1, v2):
        sum = 0
        for k in range(len(v1.coordinates)):
            sum += v1.coordinates[k,0]*v2.coordinates[k,0]
        return sum
    
    def vectorial_product( v1, v2):
        matrix_product = cross(v1.coordinates.transpose(),v2.coordinates.transpose())
        return Euclidian_Space_Vector(matrix_product.tolist()[0])
        
    
    ## Internal Sub-Methods for rotations
    
    def __get_X_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]])
        
    def __get_Y_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]])
        
    def __get_Z_rotation_matrix_3D( theta):
        theta = radians(theta)
        return matrix([[cos(theta),-sin(theta),0],[sin(theta),cos(theta),0],[0,0,1]])
        
    def __get_U_rotation_matrix_3D( theta, U):
        theta = radians(theta)
        normalised_u = U.get_copy()
        normalised_u.normalise()
        P = normalised_u.coordinates*normalised_u.coordinates.transpose()
        x,y,z = [float(k) for k in nditer(normalised_u.coordinates)]
        Q = matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
        return P +  cos(theta)*(identity(3)-P) + sin(theta)*Q 
    
    def __matrix_simplification( self):
        # simplifies coordinates matrixes when values are near to 0
        matrix = self.coordinates
        for k in range(matrix.shape[0]):
            for l in range(matrix.shape[1]):
                if abs(matrix[k,l])<self.limit_precision:
                    matrix[k,l]=0.
    
    def set_precision_limit( self, limit):
        self.limit_precision = limit
    
    ## Overloaded operators
    
    def __add__( self, v2):
        vector = self.get_copy()
        vector.translate(v2)
        return vector
    
    def __sub__( self, v2):
        vector = self.get_copy()
        vector.translate(v2.get_homothetic_vector(-1))
        return vector
    
    def __mul__( self, arg):
        if type(arg) == int or type(arg) == float :
            return self.get_homothetic_vector(arg)
        elif type(arg) == Euclidian_Space_Vector :
            return Euclidian_Space_Vector.canonical_scalar_product(self,arg)
            
    def __rmul__(self, arg) :
        return  Euclidian_Space_Vector.__mul__(self, arg)
    
    def __neg__(self):
        return self.get_homothetic_vector(-1)
        
    def __getitem__( self, index):
        return int(self.coordinates[index])
    
    def __repr__(self):
        representation = "("
        for k in nditer(self.coordinates):
            representation += str( k)+","
        representation = representation[:-1] + ")" 
        return representation