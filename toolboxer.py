# -*- coding: utf-8 -*-
"""
Toolboxer - asset of function:
- get cif information
- CIF to xyz file 
- Render image by xyz file
- Generate infos by Gigachat 
- check garbage from last session and delete it
"""

import re
from ase.io import read, write
import os

# get cif info
def cif_info():
    file_path = 'received_file.cif'  # Replace with the actual path to your file

    # Read the entire file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Define the pattern for the regular expression
    pattern = r'_publ_section_title(.*?);(.*?)_'

    # Find all matches in the file content
    matches = re.findall(pattern, file_content, re.DOTALL)

    text_info =''
    
    # If publ_section title absence
    if len(matches) == 0:
        pattern = r'_chemical_name_common.*'
        matches = re.findall(pattern, file_content)
        pattern = r'_chemical_name_common\s*'
        replacement = ''
        new_string = re.sub(pattern, replacement, matches[0])
        text_info += new_string

    for match in matches:
        text_info += match[1].strip()[:-3]  # Print the fragment after "_publ_section_title" between two symbols ";"
       
        # Remove line breaks
        text_info = text_info.replace('\n', ' ')
    
    return text_info

# CIF to xyz
def cif_to_xyz(flnm):
    
    # Read the CIF file using ASE
    atoms = read(flnm)
    
    # Write the atoms to the output XYZ file using ASE
    write("output_file.xyz", atoms, format='xyz')


# Render image by XYZ
def render_xyz():
    os.system('python bpy_renderer.py --opt1 "output_file.xyz"')

# Generate infos
def get_infos():
    os.system('python gigachat.py"')

# check garbage from last session and delete it
def session_cleaner():
    
    if os.path.exists('info.txt'):
        os.remove('info.txt')
    
    if os.path.exists('animation.mp4'):
        os.remove('animation.mp4')
