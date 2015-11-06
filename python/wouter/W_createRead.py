aovdir = r'C:\Users\w.gilsing\Desktop\New folder (2)\CGImporter\img_cgi\test_02\v01\beauty'

import os 

allFiles = os.listdir(aovdir)

firstFrame = int( allFiles[0].split('.')[1])
lastFrame =  int( allFiles[-1].split('.')[1])

filename =  allFiles[0].split('.')

#CREATE READ

readNode = nuke.createNode('Read')
readNode.knob('file').setValue((aovdir + '\\' + filename[0]+'.%04d.'+ filename[2]).replace(os.path.sep,'/'))


readNode.knob('first').setValue(firstFrame)
readNode.knob('origfirst').setValue(firstFrame)
readNode.knob('last').setValue(lastFrame)
readNode.knob('origlast').setValue(lastFrame)


#SET READ TO CORRECT FORMAT

shotWidth = str(readNode.metadata()['input/width'])
shotHeight = str(readNode.metadata()['input/height'])

formatName = 'CG Render - ' + filename[0].split('_')[1]

formatList = []

for i in nuke.formats():
    formatList.append(i.name())

if  formatName not in formatList:
    nuke.addFormat( shotWidth + ' ' + shotHeight + ' ' + formatName )
    
readNode.knob('format').setValue(formatName)