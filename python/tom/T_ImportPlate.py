import os
import nuke
from PySide import QtGui



def importPlate(plateType):

    ## Switch for different plate types 
    if plateType =="source":
        plateType = ""
        plateDesc = "Source"
        pass
    elif plateType == "undistorted":
        plateType = "undistorted"
        plateDesc = "Camera undistorted"
        pass
    elif plateType == "clean":
        plateType = "clean"
        plateDesc = "Cleanplate"
        pass
    elif plateType == "matte":
        plateType = "matte"
        plateDesc = "Matte"
        pass
    else:
        plateType =""
        plateDesc = "Unknown"
        pass


    scriptPath =  os.path.abspath(nuke.value("root.name"))
    ## Check if last two letters of the scripthpath end with a .nk extension
    if scriptPath != 'C:\Program Files\Nuke9.0v5':
        print "Found a saved script"
        print scriptPath

        ## Check of 

        ## Try to import the plate 
        
        ## Get the path creation variablse
        splitPath = scriptPath.split('\\')
      
        projectName = splitPath[2]
        sequenceName = splitPath[4]
        shotName = splitPath[5]
        ## Get the colorspace
        colorSpace = getColorSpace(projectName)
         ## Get the format size 
        format = getFormat(projectName)
        ## construct the plate path ##
        print plateType
        platePath = 'Z:\\Projects\\'+projectName+'\\editorial\\plates\\'+plateType+'\\'+sequenceName+'\\'+shotName+'\\'
        ## Get the in out 
        plateInOut = getPlateLength(platePath)
        ## Get the file extension
        ext = getExt(platePath)




        print projectName
        print sequenceName
        print shotName
        print colorSpace
        print format
        print platePath
        print plateInOut
        print ext
        
        ## Create the ReadNode##
        createReadNode(colorSpace,platePath,plateInOut,sequenceName,shotName,ext,format,plateDesc)
        try:
            
            print "Big succes!"
            nuke.tprint("Plate imported, veel plezier met Roto ;) ")
            pass
        except:
            print "Creating node failed"
            pass
        ## Celebrate! 
        







    else: ## Print a warning to the user, that he has to save the script
        print"Script has not been saved,please save script first"
        ## Send a pop up message
        msgBox = QtGui.QMessageBox() 
        msgBox.setText("This isn't going to work, please save your script first.") 
        msgBox.exec_()
    pass


## Function, takes the projectname, returns the projects colorspace 
def getColorSpace(project):


    project = project.lower()
    ## Default colorspace 
    colorSpace = "linear"
    
    if project == "infinity":
        colorSpace = "AlexaLogC"
        pass
    elif project == "mechanic":
        colorSpace = "AlexaLogC"
        pass
    elif project == "trouble":
        colorSpace = "AlexaLogC"
        pass
    elif project == "darkmachine":
        colorSpace = "AlexaLogC"
        pass
    elif project == "eigen":
        colorSpace = "AlexaLogC"
        pass
    elif project == "eigen":
        colorSpace = "AlexaLogC"
        pass    
    elif project == "Kropsdam":
        colorSpace = "AlexaLogC"
        pass
    else:
        print "Project colorspace is unknown,sorry"
        nuke.tprint("Project colorspace is unknown,sorry")
        pass
    return(colorSpace)
    pass 
 ## Function, takes the platePath, returns the length of the plate 
def getPlateLength(platePath):

    inOutFrame=[0,0]
    inOut =[0,0]
    try:
        ## Count the number of frames in the directory, check the max and min (in/out)
        inOutFrame[0] = min(os.listdir(platePath))
        inOutFrame[1] = max(os.listdir(platePath))

        ## Convert the string framenumbers into int 
        inOut[0] = int(inOutFrame[0].split('.')[1])
        inOut[1] = int(inOutFrame[1].split('.')[1])
        
        pass
    except:
        print "Counting failed"
        pass
    return inOut
    pass

## Test ther script 

def createReadNode(colorSpace,platePath,plateInOut,sequenceName,shotName,ext,format,plateDesc):
    
    ## Construct the final readpath
    readPath = os.path.normpath(platePath+shotName+'.####'+ext)
    ## Change fucking slashes 
    readPath = readPath.replace('\\','/')
    print readPath
    readNode = nuke.createNode('Read')
    readNode.knob('file').setValue(readPath)
    readNode.knob('first').setValue(plateInOut[0])
    readNode.knob('origfirst').setValue(plateInOut[0])
    readNode.knob('last').setValue(plateInOut[1])
    readNode.knob('origlast').setValue(plateInOut[1])
    readNode.knob('format').setValue(format)
    readNode.knob('colorspace').setValue(colorSpace)
    readNode.knob('label').setValue('Sequence: '+sequenceName+' Shot:'+shotName)
    readNode.knob('tile_color').setValue(150)
    
    selNodes = nuke.selectedNodes()
        
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
      
    left, top, right, bottom = (-30, -60, 30, 85)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)
    
    backdropNode = nuke.nodes.BackdropNode( xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, label = plateDesc, note_font_size = 30 )
    
    backdropNode.knob('tile_color').setValue(3432912127)

    pass

def getExt(platePath):

    ext = ".dpx"
    try:
        ## Look at extension of the first frame of the sequence)
        ext = '.'+min(os.listdir(platePath)).split('.')[2]
        pass
    except:
        print "Extension detection failed"
        ext = ".dpx"
    return ext
    pass

def getFormat(project):
    project = project.lower()
    ## Default colorspace 
    format = "HD_1080"
    
    if project == "infinity":
        format = "HD_1080"
        pass
    elif project == "mechanic":
        format = "HD_1080"
        pass
    elif project == "trouble":
        format= "HD_1080"
        pass
    elif project == "darkmachine":
        format = "HD_1080"
        pass
    elif project == "eigen":
        format= "HD_1080"
        pass
    elif project == "eigen":
        format = "HD_1080"
        pass    
    elif project == "Kropsdam":
        format = "HD_1080"
        pass
    else:
        print "Project format is unknown,sorry"
        nuke.tprint("Project format is unknown,sorry")
        pass
    return(format)
    pass


nuke.Tprint("VFX 2016,PlateExporter")