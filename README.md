# blender_batch_render
## [readme на русском](README_RUS.md)

Tiny script to render all yours .blend files in one click.
This script is useful if you have accumulated a lot of different projects that need to render. Now you can run this script at night and it will open files render them without disturbing your sleep;) **only for windows** 

### Usage
To begin the render you have to copy `script.py` and `render.bat` your folder with .blend files

Now just run `render.bat` as administrator.
![alt text](simple_img/examlpe.gif)

### Settings
In order to turn off the computer after rendering you need to uncomment the line by removing the word `rem` in render.bat

```bat
shutdown -s -f -t 20
```
You can render the in background (often used for UI-less rendering) by adding the `-b` flag

```bat
 "C:\Program Files\Blender Foundation\Blender\blender.exe" %%i -P script.py -b
```
![alt text](simple_img/example2.gif)

#### Warning
* If you have blender installed in a different folder, change the path in `render.bat`
* opengl and eevee no support render the in background

### support 
Windows 
Blender 2.8x 
