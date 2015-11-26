from hiero.core import *

projectName = "PipelineDev"

print ("Running MovExporter")
     #preset = next(preset for preset in






myProject = project("PipelineDev")
clipsBin = myProject.clipsBin()
clips = clipsBin.clips()
sequences = clipsBin.sequences()
bins = clipsBin.bins()
allItems = clipsBin.items()
certainItemTypes = clipsBin.items(Bin.ItemType.kClip | Bin.ItemType.kSequence)

print "bins: " + str(bins)

## Find the auto export bin

for item in bins:
    #print str(item).find('autoExport')
    if str(item).find('autoExport') > 0:
#        print item.items()
        print item[0].activeItem()
        # Export all timelines in the folder autoExport
        #for timeline in item.items():
#            print "Found it bitch"
#            print timeline
#            
#            print sequence
        exportItems = [hiero.core.ItemWrapper(item[0].activeItem())]

        presetName = 'VFX_2016_NulExporter'+'_'+ projectName
        presetName2 = 'VFX_2016_NulShotExporter'+'_'+projectName

        # Do the Sequence export 
        preset = next(preset for preset in
            hiero.core.taskRegistry.localPresets() if preset.name() == presetName)
       # print preset
        hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)

       ## Do the shots exports ##
    

        preset = next(preset for preset in
            hiero.core.taskRegistry.localPresets() if preset.name() == presetName2)

        hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)
#        





