import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import *

class Growth_Modifier_Volume :
    
    influence = None
    
    def __init__( self, influence = None):
        if influence is not None :
            self.influence = influence
        else :
            self.influence = Growth_Modifier_Volume.Default_Influence
    
    
    def Default_Influence( vector):
        return vector
    def Double_Length_Influence( vector):
        return vector.homotethy(2)
    def Halve_Length_Influence( vector):
        return vector.homotethy(1/2)
    
    

class GM_Sphere (Growth_Modifier_Volume):
    
    center = Euclidian_Space_Vector((0,0,0))
    radius = 1
    
    def __init__( self, center_vector, radius, influence):
        super().__init__(influence)
        self.center = center_vector
        self.radius = radius
    
    def is_in( self, vector):
        return (self.center - vector).get_norm() < self.radius


class GM_Parallelepiped (Growth_Modifier_Volume):
    
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
        valid_x = (new_vector * self.x) < (self.x.get_norm())**2
        valid_y = (new_vector * self.y) < (self.y.get_norm())**2
        valid_z = (new_vector * self.z) < (self.z.get_norm())**2
        return valid_x and valid_y and valid_z
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        