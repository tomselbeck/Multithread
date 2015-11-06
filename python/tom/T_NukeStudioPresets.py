import os
import shutil 

print ("")
print ("")
print ("Adding custom VFX 2016 NukeStudio Presets")
# Create preset directory on users machine. 
print ("")
print ("User directory")
# Get username variable 
dest = os.getenv('USERPROFILE')
# Normalize Path 
print os.path.normpath(dest)
# Add destonation path
dest = dest + "\.nuke\TaskPresets\Processors\hiero.exporters.FnShotProcessor.ShotProcessor"  
# Check if the path already exists, otherwise, create the directory
if not os.path.exists(dest):
    os.makedirs(dest)

src = os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_AUTO_PLATE_EXPORT.xml")
print ("Copy from")
print src
print ("To")
dest = dest + "\\VFX_2016_AUTO_PLATE_EXPORT.xml"
print dest 
shutil.copyfile(src, dest)

print ("")
print ("")
print ("Succes!")

print ("")
print ("")
print ("")




