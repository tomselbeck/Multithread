	
import os
import nuke

def removeHiddenFiles(filesList):
    for i in filesList:
        if i[0] == '.':
            filesList.remove(i)

def importPlate():
    try:
        curScript = nuke.Root().name()
        plateDir = curScript[:59] + 'Matchmove/publish/matchmove/plate'
         
        import os
         
        allDirs = os.listdir(plateDir)
        removeHiddenFiles(allDirs)

        lastVersion = plateDir + '/v001'

        allFiles = os.listdir(lastVersion)
        
        removeHiddenFiles(allFiles)

        allFiles.sort()
        
        firstFrame = int( allFiles[0].split('.')[1])
        lastFrame =  int( allFiles[-1].split('.')[1])
         
        filename =  allFiles[0].split('.')
         
        #CREATE READ
         
        readNode = nuke.createNode('Read')
        readNode.knob('file').setValue((lastVersion + '\\' + filename[0]+'.%04d.jpg').replace(os.path.sep,'/'))
         
         
        readNode.knob('first').setValue(firstFrame)
        readNode.knob('origfirst').setValue(firstFrame)
        readNode.knob('last').setValue(lastFrame)
        readNode.knob('origlast').setValue(lastFrame)
        
        readNode.knob('tile_color').setValue(4278255615L)
          
        readNode.knob('format').setValue('SpaceBetweenUs 2k')
        readNode.knob('colorspace').setValue('sRGB')
        readNode.knob('label').setValue('UNDISTORTED')
    except:
        nuke.message('Woops... Something went wrong.\nDid you save your script?')
        
nuke.menu("Nuke").addCommand("SpaceBetweenUs/RED/Undistorted Plate", importPlate )