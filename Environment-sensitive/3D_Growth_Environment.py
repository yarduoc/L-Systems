
class Environment :
    
    physical_objects = []
    growth_modification_zones = []
    directionnal_influences = []
    
    def __init__( self):
        

    def add_physical_object( self, physical_object):
        self.physical_objects.append( physical_object)
    
    def add_growth_modifier( self, growth_modifier):
        self.growth_modification_zones.append( growth_modifier)
        
    def raycast( self, direction_vector):
        
    
    