import os
import nuke

def importSkydome():
    
    path = "Z:\\Projects\\the_space_between_us\\assets\\Matte-Painting\\Sky\\MP\\publish\\nuke"

    allFiles = os.listdir(path)
    newsetFile = sorted(allFiles)[-1]
    filePath = path + "\\" + newsetFile

    nuke.scriptSource(filePath)
    
menubar = nuke.menu("Nuke").addCommand("SpaceBetweenUs/Sequence/GE040/Sky Setup", importSkydome )