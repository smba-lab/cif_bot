# -*- coding: utf-8 -*-
"""
bpy_renderer to render crystal structure on a blender scene - scenus.blend
and save as png file

"""

import bpy
import io_mesh_atomic.xyz_import as imprts
import argparse
import os

# psraer to run module with options
parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument("--opt1", type=str, default=1)
args = parser.parse_args()

# get paser options - filename
flpth = args.opt1

#render image
bpy.ops.wm.open_mainfile(filepath=f"{os.getcwd()}\scenus.blend")
imprts.import_xyz("0", 32, 32, 1, '2', 1, True, True, False, False, flpth)
bpy.context.scene.render.filepath = f"{os.getcwd()}\{flpth}.png"
bpy.ops.render.render(write_still=True)