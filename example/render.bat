
rem utf-8 
chcp 65001 

for %%i in (*.blend) do (
   echo write the name of the next file
   echo %%i
   rem path to your blender
   "C:\Program Files\Blender Foundation\Blender\blender.exe" %%i -P script.py 
)

rem echo off 
rem shutdown -s -f -t 20 

echo successfully
pause 