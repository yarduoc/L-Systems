#import bpy

##
from numpy import *
from math import exp


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
        
    def rotate_around_U( self, angle, U):
        self.coordinates = Euclidian_Space_Vector.__get_U_rotation_matrix_3D( angle, U)*self.coordinates
    
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
    def __get_U_rotation_matrix_3D( theta, U):
        theta = radians(theta)
        normalised_u = Euclidian_Space_Vector.get_copy_vector( U)
        normalised_u.normalise()
        P = normalised_u.coordinates*normalised_u.coordinates.transpose()
        x,y,z = [int(k) for k in nditer(normalised_u.coordinates)]
        Q = matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
        return P +  cos(theta)*(identity(3)-P) + sin(theta)*Q 
        
    
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
        
        
        
class Cartesian_Axes :
    
    X_axis = Euclidian_Space_Vector(3)
    Y_axis = Euclidian_Space_Vector(3)
    Z_axis = Euclidian_Space_Vector(3)
    
    def __init__( self):
        self.X_axis = Euclidian_Space_Vector.get_vector((1,0,0))
        self.Y_axis = Euclidian_Space_Vector.get_vector((0,1,0))
        self.Z_axis = Euclidian_Space_Vector.get_vector((0,0,1))
    
    # Rotation Method
        
    def rotate_around_U( self, angle, U):
        self.X_axis.rotate_around_U( angle, U)
        self.Y_axis.rotate_around_U( angle, U)
        self.Z_axis.rotate_around_U( angle, U)
        
        
    # Absolute Methods
    
    def get_default_axes( tuple):
        X_vect = Euclidian_Space_Vector.get_vector(tuple)
        Y_vect = 0
        x,y,z = tuple
        if x==0 :
            Y_vect = Euclidian_Space_Vector.get_vector((1,0,0))
        elif z==0 :
            Y_vect = Euclidian_Space_Vector.get_vector((0,1,0))
        elif z==0 :
            Y_vect = Euclidian_Space_Vector.get_vector((0,0,1))
        else :
            Y_vect = Euclidian_Space_Vector.get_vector((x,y,-(x**2+y**2)/z))
        x2,y2,z2 = [int(k) for k in nditer(cross(X_vect.coordinates.transpose(),Y_vect.coordinates.transpose()))]
        Z_vect = Euclidian_Space_Vector.get_vector((x2,y2,z2))
        new_axes = Cartesian_Axes()
        new_axes.X_axis = X_vect
        new_axes.Y_axis = Y_vect
        new_axes.Z_axis = Z_vect
        return new_axes
    
    def get_copy_axes( axes):
        new_axes = Cartesian_Axes()
        new_axes.X_axis = Euclidian_Space_Vector.get_copy_vector(axes.X_axis)
        new_axes.Y_axis = Euclidian_Space_Vector.get_copy_vector(axes.Y_axis)
        new_axes.Z_axis = Euclidian_Space_Vector.get_copy_vector(axes.Z_axis)
        return new_axes
    
    # Representation Method
    
    def __repr__(self):
        representation = ""
        representation += "ux : " + str(self.X_axis) + "\n"
        representation += "uy : " + str(self.Y_axis) + "\n"
        representation += "uz : " + str(self.Z_axis) + "\n"
        return representation
        
    
    
    

class turtle3D :
    
    stored_lines        = []  
    is_down             = True      
    line_thickness      = 1
    __current_position    = Euclidian_Space_Vector(3)
    __current_orientation = Cartesian_Axes()
        
    def __init__( self, coords = (0,0,0), orientation = (1,0,0)):
        self.stored_points = []
        self.__current_position = Euclidian_Space_Vector.get_vector(coords)
        self.__current_orientation = Cartesian_Axes.get_default_axes(orientation)
    
    # Turtle execution methods 
    
    def forward( self, length=1):
        current_position_copy = Euclidian_Space_Vector.get_copy_vector( self.__current_position)
        self.__current_position.translate( self.__current_orientation.X_axis.get_homothetic_vector( length))
        if self.is_down:
            self.stored_lines.append((current_position_copy.to_tuple(),self.__current_position.to_tuple(),self.line_thickness))
            
    def backward( self, length=1):
        self.forward(-length)
    
    def rotate_absolute_X( self, angle):
        self.__current_orientation.rotate_around_U(angle,Euclidian_Space_Vector.get_vector((1,0,0)))
        
    def rotate_absolute_Y( self, angle):
        self.__current_orientation.rotate_around_U(angle,Euclidian_Space_Vector.get_vector((0,1,0)))
        
    def rotate_absolute_Z( self, angle):
        self.__current_orientation.rotate_around_U(angle,Euclidian_Space_Vector.get_vector((0,0,1)))
        
    def rotate_relative_X( self, angle):
        self.__current_orientation.rotate_around_U(angle,self.__current_orientation.X_axis)
        
    def rotate_relative_Y( self, angle):
        self.__current_orientation.rotate_around_U(angle,self.__current_orientation.Y_axis)
        
    def rotate_relative_Z( self, angle):
        self.__current_orientation.rotate_around_U(angle,self.__current_orientation.Z_axis)
    
    def goto( self, coordinates):
        if self.is_down :
            stored_lines.append((self.__current_position.to_tuple(),Euclidian_Space_Vector.get_vector(coordinates).to_tuple(),self.line_thickness))
        self.set_position( coordinates)
    
    def pen_up( self):
        self.is_down = false
    def pen_down( self):
        self.is_down = true
    
    # Methods setting parameters
    
    def set_position( self, coordinates_vector):
        self.__current_position = coordinates_vector
    def set_orientation( self, orientation_axes):
        self.__current_orientation = orientation_axes
    def set_tuple_position( self, coordinates):
        self.__current_position = Euclidian_Space_Vector.get_vector(coordinates)
    def set_tuple_orientation( self, axes):
        self.__current_orientation = Cartesian_Axes.get_default_axes(axes)
    def set_thickness(self, value):
        self.line_thickness = value
        
    # Getters that returns copies of attributes
    
    def get_position( self):
        return Euclidian_Space_Vector.get_copy_vector( self.__current_position)
        
    def get_orientation( self):
        return Cartesian_Axes.get_copy_axes( self.__current_orientation)
        
    # Blender
    
    
       
    def draw_cylinder( p1, p2, rayon):
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
        bpy.ops.mesh.primitive_uv_sphere_add(size=rayon,
                                            location=p1)
        bpy.ops.mesh.primitive_uv_sphere_add(size=rayon,
                                            location=p2)
        
    def get_data_size( data_list):
        (xmin,ymin,zmin) = data_list[0][0]
        (xmax,ymax,zmax) = data_list[0][0]
        for data in data_list:
            ((x1,y1,z1),(x2,y2,z2),size) =  data
            xmin = min( xmin, min( x1, x2))
            xmax = max( xmax, max( x1, x2))
            ymin = min( ymin, min( y1, y2))
            ymax = max( ymax, max( y1, y2))
            zmin = min( zmin, min( z1, z2))
            zmax = max( zmax, max( z1, z2))
        return max( abs( xmax-xmin), abs( ymax-ymin), abs( zmax-zmin))
    
    def resize_data( data_list, dimension):
        coefficient = dimension / turtle3D.get_data_size( data_list)
        for k in range ( len( data_list)) :
            ((x1,y1,z1),(x2,y2,z2), size) =  data_list[k]
            x1 *= coefficient
            x2 *= coefficient
            y1 *= coefficient
            y2 *= coefficient
            z1 *= coefficient
            z2 *= coefficient
            size *= coefficient
            data_list[k] = [(x1,y1,z1),(x2,y2,z2), size]
        return data_list
    
    
    def blender_print ( self, dimension):
        data_list = turtle3D.resize_data( self.stored_lines, dimension)
        for data in data_list:
            (p1,p2,size) = data
            turtle3D.draw_cylinder(p1,p2,size)
        
t = turtle3D()



##Morphisme

class Morphisme:
    regle = None
    alphabet = None
    def __init__(self,regle,alphabet):
        self.regle = regle
        self.alphabet = alphabet
        
    def skip_dyck(self,mot,indice):
        compteur_dyck = -1
        for k in range(indice-1,-1,-1):
            if compteur_dyck == 0:
                return k+1
            if mot[k][0] == "[" or mot[k][0] == "]":
                compteur_dyck += (-1)**(mot[k][0] == "]")
        return "Impossible"
    
    def indice_predec(self, mot, indice):
        if indice == 0:
            return "Impossible"
        if mot[indice - 1][0] in self.alphabet:
            return indice - 1
        elif mot[indice - 1][0] == "]":
            j = self.skip_dyck(mot,indice - 1)
            if j == "impossible" :
                return "impossible"
            return self.indice_predec(mot, j)
        else:
            return self.indice_predec(mot, indice - 1)
            
            
    def est_predecesseur(self, mot,indice, motif):
        if motif == "" :
            return True
        
        nouvel_indice = self.indice_predec(mot,indice)
        
        if nouvel_indice == "Impossible" :
            return False
        if mot[nouvel_indice] != motif[-1] :
            return False
        return self.est_predecesseur(mot,nouvel_indice, motif[:-1:])
        
    def succ(self,mot,k,motif):
        pass
        
    def appliquer(self,mot):
        
        sortie = []
        for k in range(len(mot)):
            
            m = self.regle(k,mot,self.alphabet)
            sortie += m

        return sortie

##L_systeme

class L_systeme :

    alphabet = []
    morphism = None
    graine = None
    langage = []
    
    def __init__(self,morphism,graine,alphabet):
        self.morphism = morphism
        self.alphabet = alphabet
        self.graine = graine
        self.langage.append(graine)
        
    def appartiens_a_alphabet(self,caractere):
        return caractere in self.langage
    
    def etendre_langage(self):
        mot = self.langage[-1]
        
        self.langage.append(self.morphism.appliquer(mot))
        
    def renvoyer_mot(self, n):
        
        if len(self.langage) > n :
            
            return self.langage[n]
            
        self.etendre_langage()
        return self.renvoyer_mot(n)
    

## Interpretation_geometrique
    
class Interpretation_geometrique:
    
    regle_affichage = None
    L_system = None
    
    def __init__(self , regle_affichage , L_system):
        self.regle_affichage = regle_affichage
        self.L_system = L_system
    
    
    def tracer(self,n):
        
        
        mot = self.L_system.renvoyer_mot(n)
        self.regle_affichage(mot)

##regle


def regle(indice,mot,alphabet):
    lettre = mot[indice]
    if lettre[0] == "A":
        if lettre[1] < m-1:
            return [["A",lettre[1]+1]]
        if lettre[1] == m-1:
            return [["["],["+",60],["F",1,1],["B",0],["]"],["F",1,0],["/",180],["A",0]]
    if lettre[0] == "B":
        if lettre[1] < n-1:
            return [["B",lettre[1]+1]]
        if lettre[1] == n-1:
            return [["F",1,1],["B",0]]
    if lettre[0] == "S":
        if lettre[1] < u+v:
            return [["S",lettre[1]+1]]
        if lettre[1] == u+v:
            return []
    if lettre[0] == "F":
        l,o = lettre[1],lettre[2]
        if o == 0 and M.est_predecesseur(mot,indice,[["S",u-1]]):
            return [["#"],["F",l,o],["!"],["S",0]]
        if o == 1 and M.est_predecesseur(mot,indice,[["S",v-1]]):
            return [["#"],["F",l,o],["!"],["S",0]]
    if lettre[0] == "B":
        L = [["S",i] for i in range(7)]
        for pred in L:
            if M.est_predecesseur(mot,indice,pred):
                return []
    return [lettre]

##

def affichage(mot):
    pos = []
    for k in mot:
        if k[0] == "F":
            t.forward(k[1])
        elif k[0] =="[":
            pos.append((t.get_position(),t.get_orientation()))
        elif k[0] =="]":
            x=pos.pop()
            t.set_position(x[0])
            t.set_orientation(x[1])
        
        elif k[0] == "+":
            t.rotate_relative_Z(k[1])
        
        elif k[0] == "-":
            t.rotate_relative_Z(-k[1]) 
        
        elif k[0] == "/":
            t.rotate_relative_X(k[1])
        elif k[0] == "!":
            t.set_thickness(t.line_thickness*0.8)
        elif k[0] == "#":
            t.set_thickness(t.line_thickness*1.2)
##
M = Morphisme(regle,["A","B","F","S"])
L = L_systeme(M,[["S",0],["F",1,0],["A",0]],["A","B","F","S"])
A = Interpretation_geometrique(affichage,L)
m,n,u,v = 3,4,4,2
L.renvoyer_mot(0)
t = turtle3D()
A.tracer(10)