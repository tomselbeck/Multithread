#Wouter Gilsing 2014

import nuke
import os
import getpass
import time

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE UPDATE SLATE FUNCTION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
	

def updateSlate(slateNodeName):
	if not slateNodeName:
		return
	else:
		curArtist = getpass.getuser()

		curDate = time.strftime("%a") + ' ' + time.strftime("%d")  + ' ' + time.strftime("%b")  + ' ' + time.strftime("%Y") 
		curTime = time.strftime("%H") + ':' +   time.strftime("%M") 
		curScene = nuke.root().knob('name').value()
       
		slateNode = nuke.toNode(slateNodeName)
        
        manArtist = slateNode.knob('manArtist').value()
        if manArtist != '':
            slateNode.knob('artist').setValue(manArtist.lower())
        else:
            slateNode.knob('artist').setValue(curArtist)
            
        slateNode.knob('date').setValue(curDate)
        slateNode.knob('time').setValue(curTime)
        
        if nuke.toNode(slateNodeName).Class() == 'ShotSlate':
            curScene = curScene.replace('Z:/Projects/the_space_between_us/sequences/','')
            slateNode.knob('scene').setValue(curScene)
            
            curTask = curScene.split('/')[-4].lower()
            manTask = slateNode.knob('manTask').value()
            if manTask != '':
                slateNode.knob('task').setValue(manTask.lower())
            else:
                slateNode.knob('task').setValue(curTask)
       
        if nuke.toNode(slateNodeName).Class() == 'AssetSlate':
        
            sceneName = curScene.split('/')[-1][:-3].replace('.','_').split('_')

            curAssetName = sceneName[0]
            curTask = sceneName[-2]
            curVersion = sceneName[-1]
            
            slateNode.knob('asset').setValue(curAssetName)
                    
            manTask = slateNode.knob('manTask').value()
            if manTask != '':
                slateNode.knob('task').setValue(manTask.lower())
            else:
                slateNode.knob('task').setValue(curTask)
            
            slateNode.knob('version').setValue(curVersion)

def selectSlate():
    SlateList = ['AssetSlate','ShotSlate']
    if len(nuke.thisParent().selectedNodes()) == 0:
        nuke.message('Select the Slatenode')
    elif len(nuke.thisParent().selectedNodes()) > 1:
        nuke.message('Multiple nodes selected. Select only the Slatenode')
    elif nuke.thisParent().selectedNode().Class() not in SlateList:
        nuke.message('Selected node is a ' + nuke.thisParent().selectedNode().Class() +  '. Select a SlateNode')
    else:
        nuke.thisNode().knob('slateName').setValue( nuke.thisParent().selectedNode().name() )


#---------------------------------------------------------------------------------------------------------------------------------
#COREHOURS
#---------------------------------------------------------------------------------------------------------------------------------
        
def selectRead():
    if len(nuke.thisParent().selectedNodes()) == 0:
        nuke.message('Select the ReadNode you want to use')
    elif len(nuke.thisParent().selectedNodes()) > 1:
        nuke.message('Multiple nodes selected. Select only one ReadNode')
    elif nuke.thisParent().selectedNode().Class() != 'Read':
        nuke.message('Selected node is a ' + nuke.thisParent().selectedNode().Class() +  '. Select a ReadNode')
    else:
        nuke.thisNode().knob('readName').setValue( nuke.thisParent().selectedNode().name() )
        
def createDict():
    readNodeName = nuke.thisNode().knob('readName').value()
    if readNodeName == '':
        nuke.thisNode().knob('coreHoursText').setValue('')
        return

    readNode = nuke.toNode(readNodeName)
    filepath = readNode.knob('file').value().replace('publish','work').replace('elements','images')
    logPath = filepath.split('/cg/')[0] + '/cg/log/' +  filepath.split('/cg/')[1].split('/')[0]
     
    output = {}
     
    for logFile in os.listdir(logPath):
     
        with open(logPath+"/"+logFile, 'r') as f:
            for line in f:  
                if "bucket workers of size" in line:
                    cores =  int(line.split()[4])
                     
                if "Arnold shutdown" in line:
                    renderTime = line.split()[0]
         
        f.closed
        frame = logFile.split(".")[1]    
        hour, min, sec = renderTime.split(":")
        
        coreHours = (float(hour)+(float(min)/60)+(float(sec)/3600))*cores
        output[frame] =  "%.2f Core Hours on %i cores  (%s)" %( coreHours, cores ,renderTime)

    nuke.thisNode().knob('coreHoursDict').setValue(str(output))
    nuke.thisNode().knob('coreHoursText').setValue("[python {ast.literal_eval(nuke.thisNode().knob('coreHoursDict').value())[str(nuke.frame())]}]")