from hiero.core import *

import sched
import time
import nuke




def Export(projectname):
    print ("Running MovExporter")
         #preset = next(preset for preset in

## Check filename exceptions 
    print projectname
    if projectname == 'Eigen':
        pathname = 'eigen'
        print "Changed projectname"
        pass
    else:
        pathname = projectname
        pass

    try:
        print "Opening file"
        projectPath = 'Z:\\Projects\\'+pathname+'\\editorial\\conform\\nukestudio\\'+projectpath.lower()+'_pipeline.hrox'
        print projectPath
        hiero.core.openProject(projectPath)    
        print "Opening Succesful"
        pass


    
    except :
        print "opening failed"
        pass




    print project(projectname.lower() +'_pipeline')
    myProject = project(projectname.lower() +'_pipeline')
    print myProject
    clipsBin = myProject.clipsBin()
    clips = clipsBin.clips()
    sequences = clipsBin.sequences()
    bins = clipsBin.bins()
    allItems = clipsBin.items()
    certainItemTypes = clipsBin.items(Bin.ItemType.kClip | Bin.ItemType.kSequence)

    print "bins: " + str(bins)

    ## Find the auto export bin
    try:
        print "Trying to do the export"



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

                presetName = 'VFX_2016_NulExporter'+'_'+ projectname
                presetName2 = 'VFX_2016_NulShotExporter'+'_'+projectname

                # Do the Sequence export 
                preset = next(preset for preset in
                    hiero.core.taskRegistry.localPresets() if preset.name() == presetName)
               # print preset
                hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)

               ## Do the shots exports ##
            

                preset = next(preset for preset in
                    hiero.core.taskRegistry.localPresets() if preset.name() == presetName2)

                hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)
        pass       
    except:
        print "Export failed"
        pass
## test

def Schedule():

    ## Run script on a shedule 
    currentTime = time.asctime()
    while currentTime[11:16] != "11:00":
        currentTime = time.asctime()
        nuke.tprint(currentTime[11:16])    
        time.sleep(1)
        pass
    
    nuke.tprint("Running exports at" + currentTime)
    
    #Export("Eigen")
    #Export("PipelineDev")
    #Export("Infinity")

    try:
        Export("Infinity")
        pass
        nuke.tprint("Export Infinity failed")
    except:
        pass
    try:
        Export("Eigen")
        pass
    except:
        nuke.tprint("Export Eigen failed")
        pass
    try:
        Export("PipelineDev")
        pass
    except:
        nuke.tprint("Export  PipelineDev failed")
        pass
    
    nuke.tprint("finished exports at" + currentTime)
    pass


Schedule()
#Export("Eigen")
#Export("PipelineDev")

