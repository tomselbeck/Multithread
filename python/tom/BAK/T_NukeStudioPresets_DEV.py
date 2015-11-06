import os
import shutil 


# Create preset directory on users machine. 

# Get username variable 
dest = os.getenv('USERPROFILE')
print dest
# Normalize Path 
print os.path.normpath(dest)
# Add destonation path
dest = dest + "\.nuke\TaskPresets\Processors\hiero.exporters.FnShotProcessor.ShotProcessor"  
print dest 
# Check if the path already exists, otherwise, create the directory
if not os.path.exists(dest):
    os.makedirs(dest)

src = os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_AUTO_PLATE_EXPORT.xml")
print src

dest = dest + "\\VFX_2016_AUTO_PLATE_EXPORT.xml"
print dest 
shutil.copyfile(src, dest)




