
## Cartesian Axes Object

"""
Allows the user to manipulate a three axis system in a 3D euclidian space
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import Euclidian_Space_Vector

class Cartesian_Axes :
    
    """ 
    Cartesian_Axes( X = (1,0,0), Y = (0,1,0), Z = (0,0,1))
    
    Returns an axis system from three iterables of size at least 3. 
    Cartesian_Axes have some usual transformations on axes system such as
    translations and rotations.
    
    Parameters
    ----------
    X : numeral iterable
        The three first elements of this iterable are considered as the
        coordinates of the first vector of the base
    Y : numeral iterable
        The three first elements of this iterable are considered as the
        coordinates of the second vector of the base
    Z : numeral iterable
        The three first elements of this iterable are considered as the
        coordinates of the last vector of the base
    """
    
    X_axis = Euclidian_Space_Vector()
    Y_axis = Euclidian_Space_Vector()
    Z_axis = Euclidian_Space_Vector()
    
    def __init__( self, X = (1,0,0), Y = (0,1,0), Z = (0,0,1)):
        self.X_axis = Euclidian_Space_Vector(X)
        self.Y_axis = Euclidian_Space_Vector(Y)
        self.Z_axis = Euclidian_Space_Vector(Z)
    
    ## Rotation Methods
        
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
        
        
        
        
        
        
        
        
        
        
    ## Absolute Methods
    
    def get_default_axes( vector):
        """ This method returns an orthonormal axes system from a direction vector"""
        X_vect = Euclidian_Space_Vector(vector)
        x,y,z = vector
        if x==0 :
            Y_vect = Euclidian_Space_Vector((1,0,0))
        elif y==0 :
            Y_vect = Euclidian_Space_Vector((0,1,0))
        elif z==0 :
            Y_vect = Euclidian_Space_Vector((0,0,1))
        else :
            Y_vect = Euclidian_Space_Vector((x,y,-(x**2+y**2)/z))
        Z_matrix = cross(X_vect.coordinates.transpose(),Y_vect.coordinates.transpose())
        Z_vect = Euclidian_Space_Vector([int(k) for k in nditer( Z_matrix)])
        new_axes = Cartesian_Axes(X_vect,Y_vect_Z_vect)
        return new_axes
    
    ## Representation Method
    
    def __repr__(self):
        representation = ""
        representation += "ux : " + str(self.X_axis) + "\n"
        representation += "uy : " + str(self.Y_axis) + "\n"
        representation += "uz : " + str(self.Z_axis) + "\n"
        return representation