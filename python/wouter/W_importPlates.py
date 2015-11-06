import os
import nuke

def removeHiddenFiles(filesList):
    newList = []
    for i in filesList:
        if i[0] != '.':
            newList.append(i)
    return newList
			
def autoBackdropAdjusted(type):

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
    
    backdropNode = nuke.nodes.BackdropNode( xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, label = type, note_font_size = 30 )
    
    backdropNode.knob('tile_color').setValue(3432912127)

def getFrameRange(curScript):

	plateDir = 'Z:/Projects/the_space_between_us/editorial/dpx/' + curScript.split('/')[4]  + '/' + curScript.split('/')[5]
					
	allFiles = os.listdir(plateDir)
			
	allFiles = removeHiddenFiles(allFiles)
	
	allFiles.sort()
	
	#firstFrame = int( allFiles[0].split('.')[1])
	firstFrame = 1001
	lastFrame =  int( allFiles[-1].split('.')[1])
	
	framerange = [firstFrame , lastFrame]
	
	return framerange         

def getLatest(curFolder):
	allVersions = os.listdir(curFolder)
	allVersions = removeHiddenFiles(allVersions)
	latestVersion = allVersions[0]
	for i in allVersions:
		if int(i[-3:]) > latestVersion[-3:]:
			latestVersion = i
	return latestVersion
	
def createRead(curScript, type):

		sequence = curScript.split('/')[4]
		shot = curScript.split('/')[5]
		curShot = 'Z:/Projects/the_space_between_us/sequences/' + sequence + '/' + shot
		
		if type == 'camera':
			curFolder = curShot + '/Matchmove/publish/matchmove/cam' 
			print curFolder
			latestVersion = os.listdir(curFolder)
			latestVersion.reverse()
			print latestVersion
			file = curFolder + '/' + latestVersion[0]
			print file
			tileColor = 8388607		
		if type == 'plate':
			file = 'Z:/Projects/the_space_between_us/editorial/dpx/' + sequence  + '/' + shot + '/' + shot + '.%04d.dpx'
			tileColor = 3717375	    
		if type == 'prep':
			curFolder = curShot + '/Prep/publish/elements/comp/img-final'
			latestVersion = getLatest(curFolder)
			file = curFolder + '/' + latestVersion + '/' + shot + '_Prep.%04d.dpx'
			tileColor = 4286513407L
		if type == 'denoise':
			curFolder = curShot + '/Prep/publish/elements/comp/img-intermediate'
			latestVersion = getLatest(curFolder)
			file = curFolder + '/' + latestVersion + '/' + shot +  '_Prep_' + latestVersion + '.%04d.dpx'
			tileColor = 4294967295L
		if type == 'undistorted':
			file = curShot + '/Matchmove/publish/matchmove/plate/v001/' + shot + '_undistorted_v001.%04d.jpg'
			tileColor = 4278255615L
		if type == 'matte':
			curFolder = curShot + '/Prep/publish/elements/comp/img-mattes'
			latestVersion = os.listdir(curFolder)
			latestVersion.sort()           
			if len(latestVersion) > 1 : 
			    latestVersion = latestVersion[-1]
			else:
			    latestVersion = latestVersion[0]
			file = curFolder + '/' + latestVersion + '/' + shot +  '_Prep_' + latestVersion + '.%04d.jpg'
			tileColor = 255
			
		if type != 'camera':
			readNode = nuke.createNode('Read')
			readNode.knob('file').setValue(file)
			 
			frameRange = getFrameRange(curScript)
			
			readNode.knob('first').setValue(frameRange[0])
			readNode.knob('origfirst').setValue(frameRange[0])
			readNode.knob('last').setValue(frameRange[1])
			readNode.knob('origlast').setValue(frameRange[1])
			readNode.knob('format').setValue('SpaceBetweenUs 2k')
			readNode.knob('colorspace').setValue('linear')
			readNode.knob('label').setValue(type.upper())
			readNode.knob('tile_color').setValue(tileColor)
			autoBackdropAdjusted(type)
            
		else:
			readNode = nuke.createNode('Camera2')
			readNode.knob('tile_color').setValue(tileColor)            
			filename = file.split('/')[-1].split('_')
			readNode.knob('label').setValue(filename[0] + '_' + filename[1] + '\n' + filename[-1].split('.')[0])
			readNode.knob('read_from_file').setValue(True)
			readNode.knob('file').setValue(file)
            
		if type == 'matte':
			readNode.knob('colorspace').setValue('sRGB')
        
		
	
def createColorpace():
    if nuke.selectedNode().knob('file').value()[-3:] == 'jpg':
        expressionNode = nuke.createNode('Expression')
        expressionNode.knob('expr0').setValue('r > 0.5 ? 1 : 0')
        expressionNode.knob('expr1').setValue('g > 0.5 ? 1 : 0')
        expressionNode.knob('expr2').setValue('b > 0.5 ? 1 : 0')
        expressionNode.knob('expr3').setValue('clamp(r + g + b) > 0.5 ? 1 : 0')
    else:
        colorspace = 'Cineon'
        colorspaceNode = nuke.createNode('Colorspace')
        colorspaceNode.knob('colorspace_in').setValue(colorspace)
        colorspaceNode.knob('colorspace_out').setValue('RGB')
		
def plateImport(type):

	curScript = nuke.Root().name()
	
	if curScript == '':
		nuke.message('"Keep it saved" \n          - Gandalf the Grey')
	else:
		try:
			createRead(curScript, type)
			if type != 'camera':
				createColorpace()
		except:
			nuke.message('"Publishes to rule them all, but nowhere to find them,\nunable to bring them all and in your nukescript pipe them"')
			
def importPlate():
	plateImport('plate')
	
def importPrep():
	plateImport('prep')
	
def importDenoise():
	plateImport('denoise')
	
def importUndistorted():
	plateImport('undistorted')
	
def importMatte():
	plateImport('matte')
	
def importCamera():
	plateImport('camera')

def bokehImage():
    readNode = nuke.createNode('Read')
    readNode.knob('file').setValue("Z:/Projects/the_space_between_us/reference/stock/bokeh/bokeh.jpg")
    readNode.knob('colorspace').setValue('sRGB')
    readNode.knob('tile_color').setValue(3430960895L)
    
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Plate", importPlate )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Prepped Plate", importPrep )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Denoised Prepped Plate", importDenoise )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Undistorted Plate", importUndistorted )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Matte", importMatte )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Camera", importCamera )
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Import/import Bokeh", bokehImage )
nuke.toolbar("Nodes").addCommand("Gizmos/Bokeh", bokehImage )