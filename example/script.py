import os
import random
import bpy

# render as animation if yes then True
animation = False

# in which directory the render will be saved
# default in folder with .blend files
directory_render = ""

filepath = bpy.data.filepath
directory = directory_render or os.path.dirname(filepath)
name = bpy.path.display_name_from_filepath(filepath)

bpy.context.scene.render.filepath = directory + "\\render\\" + name + "//"
#bpy.data.scenes['Scene'].render.filepath = directory + "\\render\\" + name + "//"

# bpy.ops.render.opengl(animation=animation, write_still=True)

bpy.ops.render.render(animation=animation, write_still=True)

bpy.ops.wm.quit_blender()
