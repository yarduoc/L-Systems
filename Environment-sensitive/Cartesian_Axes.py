import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import *

class Cartesian_Axes :
    
    X_axis = Euclidian_Space_Vector()
    Y_axis = Euclidian_Space_Vector()
    Z_axis = Euclidian_Space_Vector()
    
    def __init__( self):
        self.X_axis = Euclidian_Space_Vector((1,0,0))
        self.Y_axis = Euclidian_Space_Vector((0,1,0))
        self.Z_axis = Euclidian_Space_Vector((0,0,1))
    
    # Rotation Method
        
    def rotate_around_U( self, angle, U):
        self.X_axis.rotate_around_U( angle, U)
        self.Y_axis.rotate_around_U( angle, U)
        self.Z_axis.rotate_around_U( angle, U)
    
    def copy( self):
        new_axes = Cartesian_Axes()
        new_axes.X_axis = Euclidian_Space_Vector.get_copy(self.X_axis)
        new_axes.Y_axis = Euclidian_Space_Vector.get_copy(self.Y_axis)
        new_axes.Z_axis = Euclidian_Space_Vector.get_copy(self.Z_axis)
        return new_axes
        
        
    # Absolute Methods
    
    def get_default_axes( vector):
        X_vect = Euclidian_Space_Vector(vector)
        x,y,z = vector
        if x==0 :
            Y_vect = Euclidian_Space_Vector((1,0,0))
        elif z==0 :
            Y_vect = Euclidian_Space_Vector((0,1,0))
        elif z==0 :
            Y_vect = Euclidian_Space_Vector((0,0,1))
        else :
            Y_vect = Euclidian_Space_Vector((x,y,-(x**2+y**2)/z))
        x2,y2,z2 = [int(k) for k in nditer(cross(X_vect.coordinates.transpose(),Y_vect.coordinates.transpose()))]
        Z_vect = Euclidian_Space_Vector((x2,y2,z2))
        new_axes = Cartesian_Axes()
        new_axes.X_axis = X_vect
        new_axes.Y_axis = Y_vect
        new_axes.Z_axis = Z_vect
        return new_axes
    
    # Representation Method
    
    def __repr__(self):
        representation = ""
        representation += "ux : " + str(self.X_axis) + "\n"
        representation += "uy : " + str(self.Y_axis) + "\n"
        representation += "uz : " + str(self.Z_axis) + "\n"
        return representation