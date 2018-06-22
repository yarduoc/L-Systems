## Growth_Modifier_Volume Objects

""" 
Defines volumes in a 3D space, associated with a function on Euclidian_Space_Vectors.
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import *

## Abstract Volume

class Growth_Modifier_Volume :
    
    """ 
    Growth_Modifier_Volume( influence)
    
    Returns a Growth_Modifier_Volume. This class is not made to be instanciated,
    but rather to serve as a base to create custom influence volumes 
    
    Parameters
    ----------
    influence : Eucilidian_Space_Vector -> Eucilidian_Space_Vector function
        This function represents the influence this volume will have on vectors
        
    """
    
    influence = None
    
    def __init__( self, influence = None):
        if influence is not None :
            self.influence = influence
        else :
            self.influence = Growth_Modifier_Volume.Default_Influence
    
    def is_in( self):
        pass
    
    ## Default influence
    
    def Default_Influence( vector):
        return vector
        
    def Double_Length_Influence( vector):
        copy = vector.get_copy()
        copy.homothety(2)
        return copy
        
    def Halve_Length_Influence( vector):
        copy = vector.get_copy()
        copy.homothety(1/2)
        return copy
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
## Real Volumes inheriting from Growth_Modifier_Volumes

class GM_Sphere (Growth_Modifier_Volume):
    
    """ 
    GM_Sphere( center_vector, radius, influence)
    
    Returns a GM_Sphere. GM_Sphere represent a volumic influence bounded inside
    a sphere.
    
    Parameters
    ----------
    center_vector : Euclidian_Space_Vector
        This vector determines where the center of the influence sphere will be
    radius : float or int
        This value determines the radius of the influence sphere
    influence : Eucilidian_Space_Vector -> Eucilidian_Space_Vector function
        This function represents the influence this volume will have on vectors
    
    """
    
    center = Euclidian_Space_Vector((0,0,0))
    radius = 1
    
    def __init__( self, center_vector, radius, influence):
        super().__init__(influence)
        self.center = center_vector
        self.radius = radius
    
    def is_in( self, vector):
        return (self.center - vector).get_norm() < self.radius





class GM_Parallelepiped (Growth_Modifier_Volume):
    
    """ 
    GM_Parallelepiped( origin_vector, x_vect, y_vect, z_vect, influence)
    
    Returns a GM_Parallelepiped. GM_Sphere represent a volumic influence bounded
    inside a parallelepiped
    
    Parameters
    ----------
    origin_vector : Euclidian_Space_Vector
        This vector determines where the origin corner of the parallelepiped will
        be located
    x_vect : Euclidian_Space_Vector
        This vector represents the first edge of the parallelepiped connected to the
        origin point    
    y_vect : Euclidian_Space_Vector
        This vector represents the second edge of the parallelepiped connected to the
        origin point
    z_vect : Euclidian_Space_Vector
        This vector represents the third edge of the parallelepiped connected to the
        origin point
    influence : Eucilidian_Space_Vector -> Eucilidian_Space_Vector function
        This function represents the influence this volume will have on vectors
    
    """
    
    origin = Euclidian_Space_Vector((0,0,0))
    x = Euclidian_Space_Vector((1,0,0))
    y = Euclidian_Space_Vector((0,1,0))
    z = Euclidian_Space_Vector((0,0,1))
    
    def __init__( self, origin_vector, x_vect, y_vect, z_vect, influence):
        super().__init__(influence)
        self.origin = origin_vector
        self.x = x_vect
        self.y = y_vect
        self.z = z_vect
    
    def is_in( self, vector):
        new_vector = vector - self.origin
        valid_x = 0 <= (new_vector * self.x) <= (self.x.get_norm())**2
        valid_y = 0 <= (new_vector * self.y) <= (self.y.get_norm())**2
        valid_z = 0 <= (new_vector * self.z) <= (self.z.get_norm())**2
        return valid_x and valid_y and valid_z
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        