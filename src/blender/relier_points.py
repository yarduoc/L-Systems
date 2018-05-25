points = 



import bpy
from numpy import *

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
    bpy.ops.mesh.primitive_uv_sphere_add(size=rayon,
                                        location=p1)
    bpy.ops.mesh.primitive_uv_sphere_add(size=rayon,
                                        location=p2)
                                        
for pt in (points) :
    draw_cylinder(pt[0],pt[1],pt[2])