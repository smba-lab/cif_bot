# -*- coding: utf-8 -*-
"""
bpy_video.py - to render rotation animation based on 'output_file.xyz' in 
blender scene - scenus.blend and saved as 'anim.mp4'

"""
import bpy
import math
import io_mesh_atomic.xyz_import as imprts
import os

flpth = "output_file.xyz"

# load blender scene
bpy.ops.wm.open_mainfile(filepath=f"{os.getcwd()}/scenus.blend")
imprts.import_xyz("0", 32, 32, 1, '2', 1, True, True, False, False, flpth)


def animate_rotation(obj_name):
    """
    Animate the rotation of an object.
    
    Parameters:
    - obj_name: The name of the object to be animated.
    """
     
    # Select the object to rotate
    obj = bpy.context.scene.objects[obj_name] 
    
    # Set the number of keyframes
    num_keyframes = 3
    
    # Set the rotation angle
    rotation_angle = 2 * math.pi  # 360 degrees in radians
    
    # Insert keyframes with easing
    for i in range(num_keyframes):
        frame = i * 60     # Set the frame number as per your requirement
        bpy.context.scene.frame_set(frame)
        obj.rotation_euler = (0, 0, rotation_angle * (i + 1))
         
        # Set easing for smoother movement
        obj.keyframe_insert(data_path="rotation_euler", index=-1, frame=frame)
        fcurve = obj.animation_data.action.fcurves.find('rotation_euler', index=-1)
        keyframe_points = fcurve.keyframe_points
        for point in keyframe_points:
            point.interpolation = 'BEZIER'
            point.handle_left_type = 'FREE'
            point.handle_right_type = 'FREE'
            

def get_mesh_names_in_collection(collection):
    """
    Get the names of all mesh objects in the specified collection and its nested collections.
    
    Parameters:
    - collection: The collection for which to retrieve mesh names.
    """
    mesh_names = []
    for obj in collection.objects:
        if obj.type == 'MESH':
            mesh_names.append(obj.name)
    for sub_collection in collection.children:
        mesh_names.extend(get_mesh_names_in_collection(sub_collection))
    return mesh_names


# Specify the name of the collection
collection_name = "output_file.xyz"

# Get the collection by name
collection = bpy.data.collections.get(collection_name)

if collection is not None:
    # Get the names of all mesh objects in the collection and its nested collections
    mesh_names = get_mesh_names_in_collection(collection)
    print(mesh_names)
    
else:
    print("Collection named '{}' not found".format(collection_name))
    
for i in mesh_names:
    animate_rotation(i)

# Set the start and end frames for the animation
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 120


# Set the output file format to FFmpeg video
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.filepath = f'{os.getcwd()}/anim.mp4'

# Render the animation
bpy.ops.render.render(animation=True)