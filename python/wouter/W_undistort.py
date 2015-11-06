import nuke
import os
import sys

input = sys.argv[1]
input = input.split(' ')

shot = input[0]
shot = shot.upper()

mm = input[1]

sensorSize = input[2]

sequence = shot.split('_')[0]

#--------------------------------------------------------------------------------------------------------------------------------------------
#remove shit from folder
#--------------------------------------------------------------------------------------------------------------------------------------------

def removeHiddenFiles(filesList):
    newList = []
    for i in filesList:
        if i[0] == '.' or i[1] == '.':
            filesList.remove(i)
        if i[0] != '.':
            newList.append(i)
      
    return newList
#--------------------------------------------------------------------------------------------------------------------------------------------
#collect data
#--------------------------------------------------------------------------------------------------------------------------------------------

footagefilepath = 'Z:/Projects/the_space_between_us/editorial/dpx/' + sequence + '/' + shot
footageFiles = removeHiddenFiles(os.listdir(footagefilepath))
footageFiles.sort()

splittedFootageFile = footageFiles[0].split('.')
footageSeq = footagefilepath + '/' + splittedFootageFile[0] + '.%04d.' + splittedFootageFile[2]

#firstframe = int(footageFiles[0].split('.')[1])
firstframe = 1001
#lastframe = int(footageFiles[-1].split('.')[1])
lastframe = (len(footageFiles) + 1000)



undisortedPlateOutput = 'Z:/Projects/the_space_between_us/sequences/' + sequence + '/' + shot + '/Matchmove/publish/matchmove/plate'

outputVersions = removeHiddenFiles(os.listdir(undisortedPlateOutput))
version = '%03d' % (len(outputVersions)+1)

undisortedPlateOutputDir = undisortedPlateOutput + '/' + 'v' + version

#create outputfolder

if not os.path.isdir(undisortedPlateOutputDir):
    os.mkdir(undisortedPlateOutputDir)

saveNewPath = 'Z:/Projects/the_space_between_us/tmp/lensdistortion/new/' + shot + '_' + str(firstframe) + '-' + str(lastframe) + '_v' + version + '.nk'
saveDonePath = 'Z:/Projects/the_space_between_us/tmp/lensdistortion/done/' + shot + '_' + str(firstframe) + '-' + str(lastframe) + '_v' + version + '.nk'
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#NUKE
#--------------------------------------------------------------------------------------------------------------------------------------------
#ROOT

nuke.Root().knob('onScriptLoad').setValue('W_SubmitToDeadline.submit()')

#READ

readnode = nuke.createNode( 'Read', 'file {' + footageSeq + ' ' + str(firstframe) +'-'+ str(lastframe) + '}', inpanel = False)
readnode.knob('colorspace').setValue('linear')

#COLORSPACE

colorspaceNode = nuke.createNode('Log2Lin', inpanel = False)


#REFORMAT

reformatnode = nuke.createNode('Reformat')
nuke.addFormat( '2048 1080 SpaceBetweenUs 2k' )
reformatnode.knob('format').setValue('SpaceBetweenUs 2k')


#LENSDISTORTION

lensdistortion = nuke.createNode('RED_LensDistortion')
lensdistortion.knob('chooseFocal').setValue(mm)
lensdistortion.knob('direction').setValue('Undistort')
lensdistortion.knob('sensor').setValue(sensorSize)

#WRITE

writenode = nuke.createNode('Write')
writenode.knob('colorspace').setValue('sRGB')
writenode.knob('file_type').setValue('jpeg')
writenode.knob('_jpeg_quality').setValue(1)
writenode.knob('file').setValue(undisortedPlateOutputDir + '/' + shot + '_undistorted_v' + version + '.%04d.jpg')
#writenode.knob('afterRender').setValue('import shutil\nshutil.move("'+saveNewPath+'", "'+saveDonePath+ '")')

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
