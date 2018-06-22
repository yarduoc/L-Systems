points = 



import bpy
from numpy import *

bpy.ops.mesh.primitive_cylinder_add(
    radius = 1,
    depth = 1,
    location = (0,0,0)
)

bpy.ops.mesh.primitive_uv_sphere_add( size=1, location=(0,0,0))

def draw_cylinder( p1, p2, rayon):
    x1,y1,z1 = p1[0], p1[1], p1[2]
    x2,y2,z2 = p2[0], p2[1], p2[2]
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    dist = sqrt(dx**2 + dy**2 + dz**2)
    
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Cylinder'].select = True
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(dx/2 + x1, dy/2 + y1, dz/2 + z1)})
    bpy.ops.transform.resize(value=(rayon, rayon, dist))
    
    phi = arctan2(dy,dx)
    theta = arccos(dz/dist)
    bpy.context.object.rotation_euler[1] = theta
    bpy.context.object.rotation_euler[2] = phi
    
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Sphere'].select = True
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":p1})
    bpy.ops.transform.resize(value=(rayon, rayon, rayon))
    
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Sphere'].select = True
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":p2})
    bpy.ops.transform.resize(value=(rayon, rayon, rayon))
    
                                        
for pt in (points) :
    draw_cylinder(pt[0],pt[1],pt[2])