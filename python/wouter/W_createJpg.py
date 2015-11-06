import nuke
import sys
import os

shot = sys.argv[1]

seq = shot.split('_')[0]


def removeHiddenFiles(filesList):
    for i in filesList:
        if i[0] == '.':
            filesList.remove(i)
            

dest = 'Z:\\Projects\\the_space_between_us\\editorial\\jpg\\' + seq + '\\' + shot

try:    
    os.mkdir(dest)
except:
    pass
readNode = nuke.createNode('Read')
reformatNode = nuke.createNode('Reformat')
colorspaceNode = nuke.createNode('Colorspace')

for i in nuke.allNodes():
    i.knob('selected').setValue(False)
    
logoRead = nuke.createNode('Read')
textnode = nuke.createNode('Text')
textnode2 = nuke.createNode('Text')  
textnode3 = nuke.createNode('Text')
colorspaceNode2 = nuke.createNode('Colorspace')

for i in nuke.allNodes():
    i.knob('selected').setValue(False)

colorspaceNode2.knob('selected').setValue(True)
colorspaceNode.knob('selected').setValue(True)


mergeNode = nuke.createNode('Merge2')
writeNode = nuke.createNode('Write')

plateDir = 'Z:/Projects/the_space_between_us/editorial/dpx/' + seq  + '/' + shot
                
allFiles = os.listdir(plateDir)
        
removeHiddenFiles(allFiles)

allFiles.sort()

firstFrame = int( allFiles[0].split('.')[1])
lastFrame =  int( allFiles[-1].split('.')[1])

nuke.Root().knob('first_frame').setValue(firstFrame)
nuke.Root().knob('last_frame').setValue(lastFrame)

filename =  allFiles[0].split('.')

reformatNode.knob('format').setValue('HD')
colorspaceNode.knob('colorspace_in').setValue('RGB')
colorspaceNode.knob('colorspace_out').setValue('sRGB')

colorspaceNode2.knob('colorspace_in').setValue('RGB')
colorspaceNode2.knob('colorspace_out').setValue('sRGB')

readNode.knob('file').setValue((plateDir + '\\' + filename[0] + '.%04d.dpx').replace(os.path.sep,'/'))       
readNode.knob('first').setValue(firstFrame)
readNode.knob('origfirst').setValue(firstFrame)
readNode.knob('last').setValue(lastFrame)
readNode.knob('origlast').setValue(lastFrame)
   
logoRead.knob('file').setValue(('Z:\\Projects\\the_space_between_us\\dev\\nuke\\icons\\slate_overlay.png').replace(os.path.sep,'/'))
    
textnode.knob('size').setValue(24)
textnode.knob('xjustify').setValue('right')
textnode.knob('message').setValue('[format %04i [frame]]')
textnode.knob('box').setValue([0,0,1880,115])
textnode.knob('color').setValue(0.7)

textnode2.knob('size').setValue(24)
textnode2.knob('message').setValue(shot)
textnode2.knob('box').setValue([40,981,2080,1015])
textnode2.knob('color').setValue(0.7)

textnode3.knob('size').setValue(24)
textnode3.knob('xjustify').setValue('right')
textnode3.knob('message').setValue('[ date %a ] [ date %d ] [ date %b ] [ date %Y ]\n[ date %H ]:[ date %M ]')
textnode3.knob('box').setValue([0,0,1920,1080])
textnode3.knob('translate').setValue([-40,470])
textnode3.knob('color').setValue(0.7)

writeNode.knob('file').setValue(dest.replace(os.path.sep,'/') + '/' + shot + '_v000.%04d.jpg')
writeNode.knob('file_type').setValue('jpeg')
writeNode.knob('_jpeg_quality').setValue(1)
writeNode.knob('colorspace').setValue('linear')    
    
nuke.scriptSave('Z:/Projects/the_space_between_us/tmp/techcheckjpg/nukescripts/' + shot + '_' + str(firstFrame) + '-' + str(lastFrame) + '.nk')

nuke.scriptExit()
    