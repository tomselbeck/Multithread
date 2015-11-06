import os
import nuke

def removeHiddenFiles(filesList):
    for i in filesList:
        if i[0] == '.':
            filesList.remove(i)
            
def autoBackdropAdjusted():

    selNodes = nuke.selectedNodes()
    
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
      
    left, top, right, bottom = (-30, -120, 30, 85)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)
    
    backdropNode = nuke.nodes.BackdropNode( xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, label = 'plate', note_font_size = 50 )
    
    backdropNode.knob('tile_color').setValue(3432912127L)

    
def importSourcePlate():

    try:

        curScript = nuke.Root().name()

        plateDir = 'Z:/Projects/the_space_between_us/editorial/dpx/' + curScript.split('/')[4]  + '/' + curScript.split('/')[5]
                        
        allFiles = os.listdir(plateDir)
                
        removeHiddenFiles(allFiles)
        
        allFiles.sort()
        
        firstFrame = int( allFiles[0].split('.')[1])
        lastFrame =  int( allFiles[-1].split('.')[1])
         
        filename =  allFiles[0].split('.')
         
        #CREATE READ
         
        readNode = nuke.createNode('Read')
        
        colorspaceNode = nuke.createNode('Colorspace')
        colorspaceNode.knob('colorspace_in').setValue('Cineon')
        
        readNode.knob('file').setValue((plateDir + '\\' + filename[0] + '.%04d.dpx').replace(os.path.sep,'/'))
        readNode.knob('tile_color').setValue(3717375)          
        readNode.knob('first').setValue(firstFrame)
        readNode.knob('origfirst').setValue(firstFrame)
        readNode.knob('last').setValue(lastFrame)
        readNode.knob('origlast').setValue(lastFrame)
          
        readNode.knob('format').setValue('SpaceBetweenUs 2k')
        readNode.knob('label').setValue('PLATE')
        
        
        readNode.knob('selected').setValue(True)
        colorspaceNode.knob('selected').setValue(True)

        autoBackdropAdjusted()
        
        colorspaceNode.setYpos(colorspaceNode.ypos()+55)
        
    except:
    
        nuke.message('Woops... Something went wrong.\nDid you save your script?')
        
nuke.menu("Nuke").addCommand("SpaceBetweenUs/import Plate", importSourcePlate )