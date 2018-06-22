## Environment Object

""" 
Allows the turtle3D object to have environmental parameters impacting its evolution
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Physical_object import Physical_Volume
from Growth_Modifier import *
from Geometry import *

class Environment :
    
    """ 
    Environment()
    
    Returns an Environment object
    Environment objects are used to keep environmental objects and influences and
    process raycasts and belonging tests to return a turtle the effects modifying
    its instructions.
    
    Parameters
    ----------
    None
    
    """
    
    physical_objects = []
    growth_modification_zones = []
    
    def __init__( self):
        pass

    ## Methods adding influences to the Environment
    
    def add_physical_object( self, physical_object):
        self.physical_objects.append( physical_object)
    
    def add_growth_modifier( self, growth_modifier):
        self.growth_modification_zones.append( growth_modifier)
    
    ## Raycast and Belonging tests
    
    def raycast( self, direction, origin):
        growth_effects = []
        for modifier in self.growth_modification_zones :
            if modifier.is_in(origin + direction):
                growth_effects.append(modifier)
        physical_collisions = []
        for physical_object in self.physical_objects :
            physical_collisions += physical_object.hit_by_raycast( origin, direction)
        return growth_effects,physical_collisions
        
            
                
            
        
        
    
    