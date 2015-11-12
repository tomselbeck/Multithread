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
user = dest
# Normalize Path 
print os.path.normpath(dest)
# Add destonation path
dest = dest + "\.nuke\TaskPresets\Processors\hiero.exporters.FnShotProcessor.ShotProcessor"  
# Check if the path already exists, otherwise, create the directory
if not os.path.exists(dest):
    os.makedirs(dest)
src = []
dest2 =[]




src.append (os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_AUTO_PLATE_EXPORT.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_NulShotExporter_Eigen.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_NulShotExporter_Mechnanic.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_NulShotExporter_DarkMachine.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_NulShotExporter_Infinity.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnShotProcessor.ShotProcessor\\VFX_2016_NulShotExporter_Trouble.xml"))


src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnTimelineProcessor.TimelineProcessor\\VFX_2016_NulExporter_Eigen.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnTimelineProcessor.TimelineProcessor\\VFX_2016_NulExporter_Mechanic.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnTimelineProcessor.TimelineProcessor\\VFX_2016_NulExporter_DarkMachine.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnTimelineProcessor.TimelineProcessor\\VFX_2016_NulExporter_Infinity.xml"))
src.append ( os.path.abspath("Z:\\pipeline\\nuke\\TaskPresets\\Processors\\hiero.exporters.FnTimelineProcessor.TimelineProcessor\\VFX_2016_NulExporter_Trouble.xml"))

print ("Copy from")
print src
print ("To")

dest2.append ( dest + "\\VFX_2016_AUTO_PLATE_EXPORT.xml")
dest2.append ( dest + "\\VFX_2016_NulShotExporter_Eigen.xml")
dest2.append ( dest + "\\VFX_2016_NulShotExporter_Mechnanic.xml")
dest2.append ( dest + "\\VFX_2016_NulShotExporter_DarkMachine.xml")
dest2.append ( dest + "\\VFX_2016_NulShotExporter_Infinity.xml")
dest2.append ( dest + "\\VFX_2016_NulShotExporter_Trouble.xml")


dest2.append ( dest + "\\VFX_2016_NulExporter_Eigen.xml")
dest2.append ( dest + "\\VFX_2016_NulExporter_Mechnanic.xml")
dest2.append ( dest + "\\VFX_2016_NulExporter_DarkMachine.xml")
dest2.append ( dest + "\\VFX_2016_NulExporter_Infinity.xml")
dest2.append ( dest + "\\VFX_2016_NultExporter_Trouble.xml")
print dest2


for x in src:
	for y in dest2:
		shutil.copyfile(x,y)
		print "Copying export sjizzle from" + x + "to"+ y
		pass
	pass













print ("")
print ("")
print ("It's Amazing, nothing crashed, Succes!")

print ("")
print ("")
print ("")

print user + ", Have a good day :) " 



