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
        

    def add_physical_object( self, physical_object):
        self.physical_objects.append( physical_object)
    
    def add_growth_modifier( self, growth_modifier):
        self.growth_modification_zones.append( growth_modifier)
        
    def raycast( self, direction_vector, origin):
        
        
    
    