import nuke

def updatePreviewPaths(node):

    curNode = node
    writeGeoNode = nuke.toNode(curNode.name() +'.WriteGeo1')

    filePath = nuke.root().knob('name').value()

    if filePath == '':
        curNode.knob('outputcontext').setValue('Please save your script')
        curNode.knob('outputlocalpath').setValue('Please save your script')
        curNode.knob('outputfilename').setValue('Please save your script')   
        
    else:
        workDir =  filePath.split('/nuke/')[0]
        outputType = curNode.knob('output').value()
    
        stepDir = workDir.split('/')[-2] + '/' + workDir.split('/')[-1]
        localPath = stepDir + '/matchmove/' +  outputType
        context = workDir.replace(('/' + stepDir),'')
    
        sceneName = filePath.split('/')[-5]
        version = filePath.split('/')[-1].split('.')[1]  
        
        fileName = sceneName + '_' + outputType + '_' + version + '.abc'
        completeOutputPath = context + '/' + localPath + '/' + fileName
    
        curNode.knob('outputcontext').setValue(context)
        curNode.knob('outputlocalpath').setValue(localPath)
        curNode.knob('outputfilename').setValue(fileName)    
    
        writeGeoNode.knob('file').setValue(completeOutputPath)

def updatePathsOnKnobChange():
    if nuke.thisKnob().name() == 'output':
        updatePreviewPaths(nuke.thisNode())

def updatePathsOnScriptSave():
    for i in nuke.allNodes():
        if i.Class() == 'ShotgunWriteGeo':
            updatePreviewPaths(i)
            
def updatePathsOnCreation():
    nuke.addKnobChanged(updatePathsOnKnobChange, nodeClass='ShotgunWriteGeo')
    nuke.addOnScriptSave(updatePathsOnScriptSave)
    updatePreviewPaths(nuke.thisNode())
            
nuke.addOnCreate(updatePathsOnCreation, nodeClass='ShotgunWriteGeo')
