from nuke import *
from hiero.core import *





# Find the named preset
# import nuke
# import hiero.core

# try:
#     import hiero.core
# except ImportError:
#     print ("Fucked it upp")
#     pass


# # #from hiero.core import *

# def Export(project):
#     import hiero.core


#     print ("Running MovExporter")
#         #preset = next(preset for preset in
#     presetName = 'VFX_2016_NulExporter'+'_'+project


#     preset = next(preset for preset in
#         hiero.core.taskRegistry.localPresets() if preset.name() == presetName)

    
    

#     # get the last loaded project
    
#     myProject = projects()[-1]
#     print myProject
#     clipsBin = myProject.clipsBin()
#     sequences = clipsBin.sequences()
#     x = 0
#     for all in sequences:       
#         testitem = "BinItem('nul')"
#         print testitem
#         if str(sequences[x]) == testitem:
#             print ("Exporting file ")

#             # Create the list of items for export
#             sequence = hiero.core.projects()[0].clipsBin()[0].activeItem()
#             exportItems = [hiero.core.ItemWrapper(sequence)]

#             # Do the export
#             hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)

#             presetName2 = 'VFX_2016_NulShotExporter'+'_'+project

#             preset = next(preset for preset in
#                 hiero.core.taskRegistry.localPresets() if preset.name() == presetName2)

#             hiero.core.taskRegistry.createAndExecuteProcessor(preset, exportItems,synchronous=False)

#             pass
#         x = x+1
#         pass    
#     pass


