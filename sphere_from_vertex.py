# Script to convert a vertex to a uv sphere

import bpy 
from bpy import context
import bmesh
import mathutils


shape_mesh_v = bpy.context.active_object #set as active object
bm = bmesh.new() #Create new mesh
bm.from_mesh(shape_mesh_v.data) #get data from shape_mesh_v 

src = [v for v in bm.verts] 

for v in src:
    loc = mathutils.Matrix.Translation(v.co) #Define location
    mat = mathutils.Matrix.Identity(3) #create new empty matrix
    mat = loc * mat.to_4x4() #Convert to a 4 by 4 matrix
    bmesh.ops.create_uvsphere(bm, u_segments=10, v_segments=10, diameter=1, matrix=mat) #Draw a sphere

bm.to_mesh(shape_mesh_v.data)
bm.free()
    
