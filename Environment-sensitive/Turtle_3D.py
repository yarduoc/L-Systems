## Turtle3D Object

""" 
Allows the user to ave a turtle structure in a 3D space. Lines and position where
to draw can be exported into blender to have a 3D modelisation of the turtle output
"""

import os
os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
from Euclidian_Space_Vector import Euclidian_Space_Vector
from Cartesian_Axes import Cartesian_Axes
from Growth_Environment import Environment

class Turtle3D :
    
    """ 
    Turtle3D( environment, coords = (0,0,0), orientation = (1,0,0))
    
    Returns a Turtle object. Turtles can be given multiples instructions, and
    take into account their environment modifiers to create the 3D positions of
    the instructions sequence.
    
    Parameters
    ----------
    environment : Environment object
        This environment represents the environment and obstacles the turtle may
        encounter during the execution of the user instructions
    coords : numeral iterable
        The three first elements of this iterable represent the coordinates of 
        the vector representing the initial position of the turtle
    orientation : numeral_iterable
        The three first elements of this iterable represent the coordinates of 
        the direction vector of the turtle (its forward direction)
    
    """
    
    stored_lines        = []  
    is_down             = True      
    line_thickness      = 1
    __current_position    = Euclidian_Space_Vector()
    __current_orientation = Cartesian_Axes()
    environment = None
        
    def __init__( self, environment, coords = (0,0,0), orientation = (1,0,0)):
        self.stored_points = []
        self.__current_position = Euclidian_Space_Vector(coords)
        self.__current_orientation = Cartesian_Axes.get_default_axes(orientation)
        self.environment = environment
    
    ## Turtle execution methods 
    
    def forward( self, length=1):
        raydir = length*self.__current_orientation.X_axis
        environment_action = self.environment.raycast(raydir,self.__current_position)
        if len(environment_action[1]) > 0:
            return "Erreur_collision"
        origin_dir = self.__current_orientation.X_axis.get_homothetic_vector(length)
        direction = origin_dir.get_copy()
        for modifier in environment_action[0]:
            direction = modifier.influence(direction)
        current_position_copy = self.__current_position.get_copy()
        self.__current_position += direction
        if self.is_down:
            origin = current_position_copy.get_tuple_representation()
            position = self.__current_position.get_tuple_representation()
            self.stored_lines.append(( origin, position, self.line_thickness))
            
    def backward( self, length=1):
        self.forward(-length)
    
    def rotate_absolute_X( self, angle):
        axis = Euclidian_Space_Vector((1,0,0))
        self.__current_orientation.rotate_around_U( angle, axis)
        
    def rotate_absolute_Y( self, angle):
        axis = Euclidian_Space_Vector((0,1,0))
        self.__current_orientation.rotate_around_U( angle, axis)
        
    def rotate_absolute_Z( self, angle):
        axis = Euclidian_Space_Vector((0,0,1))
        self.__current_orientation.rotate_around_U( angle, axis)
        
    def rotate_relative_X( self, angle):
        axis = self.__current_orientation.X_axis
        self.__current_orientation.rotate_around_U( angle, axis)
        
    def rotate_relative_Y( self, angle):
        axis = self.__current_orientation.Y_axis
        self.__current_orientation.rotate_around_U( angle, axis)
        
    def rotate_relative_Z( self, angle):
        axis = self.__current_orientation.Z_axis
        self.__current_orientation.rotate_around_U( angle, axis)
    
    def goto( self, coordinates):
        if self.is_down :
            origin = self.__current_position.get_tuple_representation()
            self.stored_lines.append(( origin, coordinates, self.line_thickness))
        self.set_position( coordinates)
    
    def pen_up( self):
        self.is_down = false
    def pen_down( self):
        self.is_down = true
    
    ## Methods setting parameters
    
    def set_position( self, coordinates_vector):
        self.__current_position = coordinates_vector
        
    def set_orientation( self, orientation_axes):
        self.__current_orientation = orientation_axes
        
    def set_tuple_position( self, coordinates):
        self.__current_position = Euclidian_Space_Vector(coordinates)
        
    def set_tuple_orientation( self, axes):
        self.__current_orientation = Cartesian_Axes.get_default_axes(axes)
        
    def set_thickness(self, value):
        self.line_thickness = value
        
    ## Getters that returns copies of attributes
    
    def get_position( self):
        return Euclidian_Space_Vector.get_copy( self.__current_position)
        
    def get_orientation( self):
        return Cartesian_Axes.copy( self.__current_orientation)
        
        
        
        
        
    ## Blender output functions
    
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
        
        bpy.ops.mesh.primitive_uv_sphere_add( size=rayon, location=p1)
        bpy.ops.mesh.primitive_uv_sphere_add( size=rayon, location=p2)
        
    
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