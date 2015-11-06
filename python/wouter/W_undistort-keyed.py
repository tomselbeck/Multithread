import nuke
import os
import sys

shot = sys.argv[1]

seq = shot.split('_')[0]

#--------------------------------------------------------------------------------------------------------------------------------------------
#remove shit from folder
#--------------------------------------------------------------------------------------------------------------------------------------------

def removeHiddenFiles(filesList):
    for i in filesList:
        if i[0] == '.':
            filesList.remove(i)
      
    return filesList
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#collect data
#--------------------------------------------------------------------------------------------------------------------------------------------

mmdir = "Z:/Projects/the_space_between_us/sequences/" + seq  + "/" + shot + "/Matchmove/publish/matchmove/plate/"
readpath = mmdir + "v001/" + shot + '_undistorted_v001.%04d.jpg'
writedir = mmdir + "v002"

footageFiles = removeHiddenFiles(os.listdir(mmdir + '/v001'))
footageFiles.sort()

firstframe = int(footageFiles[0].split('.')[1])
lastframe = int(footageFiles[-1].split('.')[1])


saveNewPath = 'Z:/Projects/the_space_between_us/tmp/lensdistortion/new/' + shot + '_' + str(firstframe) + '-' + str(lastframe) + '_v002.nk'
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#NUKE
#--------------------------------------------------------------------------------------------------------------------------------------------
#ROOT

nuke.Root().knob('onScriptLoad').setValue('W_SubmitToDeadline.submit()')



try:
    os.mkdir(writedir)
except:
    pass

writepath = writedir + '/' + shot + '_undistorted-premultiplied_v002.%04d.png'


footageRead = nuke.createNode('Read')
keyerNode = nuke.createNode('Keyer')
exprNode =  nuke.createNode('Expression')

premultNode = nuke.createNode('Premult')
textNode = nuke.createNode('Text')
writeNode = nuke.createNode('Write')

footageRead.knob('file').setValue(readpath)
footageRead.knob('colorspace').setValue('sRGB')

footageRead.knob('first').setValue(firstframe)
footageRead.knob('last').setValue(lastframe)
footageRead.knob('origfirst').setValue(firstframe)
footageRead.knob('origlast').setValue(lastframe)

keyerNode.knob('operation').setValue('greenscreen')
keyerNode.knob('range').setValue([.9, 1, 1, 1])

exprNode.knob('expr1').setValue('g > (r+b)/2? (r+b)/2 : g')

textNode.knob('message').setValue('[frame]')
textNode.knob('xjustify').setValue('right')
textNode.knob('yjustify').setValue('bottom')

textNode.knob('box').setValue([40, 40, 2048-40, 1080-40])
writeNode.knob('file_type').setValue('png')
writeNode.knob('colorspace').setValue('sRGB')
writeNode.knob('channels').setValue('rgba')
writeNode.knob('file').setValue(writepath)


#PROJECT

nuke.Root().knob('first_frame').setValue(firstframe)
nuke.Root().knob('last_frame').setValue(lastframe)

#SAVE

nuke.scriptSave(saveNewPath)

#RENDER

#nuke.execute(writenode.name(), start=firstframe, end=lastframe, incr=1)

#QUIT NUKE

nuke.scriptExit()

#--------------------------------------------------------------------------------------------------------------------------------------------
