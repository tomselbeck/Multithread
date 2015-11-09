# Find the named preset
import hiero.core
from hiero.core import *


def MovExporter():

        #preset = next(preset for preset in
    presetName = 'VFX_2016_NulExporter' 
    preset = next(preset for preset in
        hiero.core.taskRegistry.localPresets() if preset.name() == presetName)

    #print preset
    #sequence = hiero.core.projects()[0].clipsBin()[0].activeItem()

    # get the last loaded project

    myProject = projects()[-1]
    clipsBin = myProject.clipsBin()
    sequences = clipsBin.sequences()
    x = 0
    for all in sequences:       
        testitem = "BinItem('nul')"
        print testitem
        if str(sequences[x]) == testitem:
            print ("Exporting file ")

            # Create the list of items for export
            sequence = hiero.core.projects()[0].clipsBin()[0].activeItem()
            exportItems = [hiero.core.ItemWrapper(sequence)]
            # Do the export
            hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,
            synchronous=False)
            pass
        x = x+1
        pass
    




    
    #print type(sequence)
    #print("")
    
    #sequence = "# Result: Sequence('nul')"
    #print sequence
    #exportItems = [hiero.core.ItemWrapper(sequence)]

    #hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,
    #synchronous=False)

        # Do the export
    #    hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,
    #    synchronous=True)

    pass

MovExporter()

