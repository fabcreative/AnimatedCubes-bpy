
import bpy

import random

from math import sin, tau



# clear meshes in the scene

for obj in bpy.data.objects:

    if obj.type == 'MESH':

        bpy.data.objects.remove(obj)



# animation variables

total_frames = 150

theta = 0.0



# define a one hundred frame timeline

bpy.context.scene.frame_end = total_frames

bpy.context.scene.frame_start = 0

def random_color():
    r, g, b = [random.random() for i in range(3)]

    return r, g, b, 1



for x in range(30):

    # generate a grid of cones
    

    for y in range(30):
        

        cone = bpy.ops.mesh.primitive_cube_add()

        cone = bpy.context.object
        
        cone.color = random_color()
        
        # Create a material
        mat = bpy.data.materials.new("Blue")

        # Activate its nodes
        mat.use_nodes = True

        # Get the principled BSDF (created by default)
        principled = mat.node_tree.nodes['Principled BSDF']

        # Assign the color
        principled.inputs['Base Color'].default_value = random_color()

        # Assign the material to the object
        cone.data.materials.append(mat)

        cone.name = 'Cone-{}-{}'.format(x, y)

        cone.location[0] = x * 2

        cone.location[1] = y * 2
    

        for frame in range(0, total_frames):

            bpy.context.scene.frame_set(frame)

            cone.location.z = sin(theta + x) * 2 - 1

            cone.keyframe_insert(data_path='location')

            scale = sin(theta + y)

            cone.scale = (scale, scale, scale)

            cone.keyframe_insert(data_path='scale')

            theta += tau / total_frames
ff