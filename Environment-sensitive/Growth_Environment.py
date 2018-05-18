import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Physical_object import *
from Growth_Modifier import *
from Geometry_2 import *

class Environment :
    
    physical_objects = []
    growth_modification_zones = []
    directionnal_influences = []
    
    def __init__( self):
        pass
        

    def add_physical_object( self, physical_object):
        self.physical_objects.append( physical_object)
    
    def add_growth_modifier( self, growth_modifier):
        self.growth_modification_zones.append( growth_modifier)
        
    def raycast( self, direction_vector, origin):
        growth_effects = []
        for modifier in self.growth_modification_zones :
            if modifier.is_in(origin + direction_vector):
                growth_effects.append(modifier)
        physical_collisions = []
        for physical_object in self.physical_objects :
            physical_collisions += physical_object.hit_by_raycast( origin, direction_vector)
        return growth_effects,physical_collision
        
            
                
            
        
        
    
    