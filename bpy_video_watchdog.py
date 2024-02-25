"""
Watchdog to control whether the animation file exists or not.

"""

import os
import time

file_path = 'animation.mp4' 

while True:
    if os.path.exists(file_path):
        time.sleep(5)

    else:
        os.system('python bpy_video.py')
        os.rename('anim.mp4', 'animation.mp4')