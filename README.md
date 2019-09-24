# blender_batch_render

Tiny script to render all yours .blend files in one click.
This script is useful if you have accumulated a lot of different projects that need to render. Now you can run this script at night and it will open files render them without disturbing your sleep;)

To begin the render you have to copy `script.py` and `render.bat` your folder with .blend files

Now just run `render.bat` as administrator.

In order to turn off the computer after rendering you need to uncomment the line by removing the word rem in render.bat

```bat
rem shutdown -s -f -t 20
```
