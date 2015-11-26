print "Debug:Running Menu.py"




#----------------------------------------------------------------------------------------------------------------------
# VFX 2016 custom menubar
#----------------------------------------------------------------------------------------------------------------------
 
menubar = nuke.menu("Nuke")
## Add Menu Bar
bar2016 = menubar.addMenu("vfx 2016 :)")
## Custom scripts ##
import T_twtswitch
import T_ImportPlate

bar2016.addCommand("TimeWillTell/Switch_to_server", "T_twtswitch.server()")
bar2016.addCommand("TimeWillTell/Switch_to_local", "T_twtswitch.local()")

## Plate importer 
bar2016.addCommand("PipelineTools/Import plate/Import Source", "T_ImportPlate.importPlate('source')")
bar2016.addCommand("PipelineTools/Import plate/Import Undistorted", "T_ImportPlate.importPlate('undistorted')")
bar2016.addCommand("PipelineTools/Import plate/Import Matte", "T_ImportPlate.importPlate('matte')")
bar2016.addCommand("PipelineTools/Import plate/Import Clean", "T_ImportPlate.importPlate('clean')")
#import T_NulversieCreator
bar2016.addCommand("PipelineTools/Import NulversieExporter", "import T_NulversieCreator")
bar2016.addCommand("PipelineTools/Import export timer", "import T_MovExporter")
bar2016.addCommand("PipelineTools/Start export timer", "T_MovExporter.Schedule")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: PipelineDev", "T_NulversieCreator.PipelineDev()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: Eigen", "T_NulversieCreator.Eigen()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: DarkMachine", "T_NulversieCreator.DarkMachine()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: Kropsdam", "T_NulversieCreator.Kropsdam()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: Infinity", "T_NulversieCreator.Infinity()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: Trouble", "T_NulversieCreator.Trouble()")
bar2016.addCommand("PipelineTools/Update Nulversie/Project: Mechanic", "T_NulversieCreator.Mechanic()")





## Custom Gizmos







## Custom Stuff
#bar2016.addCommand("Custom/ShotSlate", "nuke.createNode('T_ShotSlate')")

#----------------------------------------------------------------------------------------------------------------------
# VFX 2016 custom menu
#----------------------------------------------------------------------------------------------------------------------








#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIZMOS toolbar nukepedia
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
NodesToolbar = nuke.toolbar("Nodes")

gizmoToolbar = NodesToolbar.addMenu("Gizmos",icon="NukePedia.png")

gizmoToolbar.addCommand("DespillMadness", "nuke.createNode('DespillMadness')", icon="NukePedia.png")
gizmoToolbar.addCommand("EdgeExtend", "nuke.createNode('EdgeExtend')", icon="FilterErode.png")
gizmoToolbar.addCommand("tracker2Camera", "nuke.createNode('tracker2Camera')", icon="CameraTracker.png")

gizmoToolbar.addCommand("ImagePlane", "nuke.createNode('ImagePlane')", icon="planar_tracker.png")
gizmoToolbar.addCommand("nTransform", "nuke.createNode('nTransform')", icon="2D.png")
gizmoToolbar.addCommand("TrackingConverter", "nuke.createNode('TrackingConverter')", icon="CameraTracker.png")
gizmoToolbar.addCommand("mmColorTarget", "nuke.createNode('mmColorTarget')", icon='mmColorTarget.png')

gizmoToolbar.addCommand("bm_Lightwrap", "nuke.createNode('bm_Lightwrap')", icon='bm_lightwrap.png')
gizmoToolbar.addCommand("bm_OpticalGlow", "nuke.createNode('bm_OpticalGlow')", icon='opticalglow')
gizmoToolbar.addCommand("Colour_Smear", "nuke.createNode('Colour_Smear')", icon='smear.png')
gizmoToolbar.addCommand("Breakdown_Tool", "nuke.createNode('Breakdown_Tool')", icon='breakdown.jpg')
gizmoToolbar.addCommand("Chromatic_Abberration", "nuke.createNode('Chromatic_Aberration')", icon='chromab.jpg')



gizmoToolbar.addCommand("BokehBlur", "nuke.createNode('BokehBlur')", icon='bokehblur.jpg')
gizmoToolbar.addCommand("Caustics_jb", "nuke.createNode('Caustics_jb')", icon='caustics.jpg')
gizmoToolbar.addCommand("Heat_Distort", "nuke.createNode('Heat_Distort')", icon='heat_distort.png')
gizmoToolbar.addCommand("RealHeatDistortion", "nuke.createNode('RealHeatDistortion')", icon='heat_distort.png')
gizmoToolbar.addCommand("RealChromaticAberration", "nuke.createNode('RealChromaticAberration')", icon='chromab.png')

gizmoToolbar.addCommand("TX_Fog", "nuke.createNode('TX_Fog')", icon='fog.png')
gizmoToolbar.addCommand("VectorExtendEdge", "nuke.createNode('VectorExtendEdge')", icon='EdgeExtend.png')
gizmoToolbar.addCommand("RealCamShake", "nuke.createNode('RealCamShake')", icon="shake.png")
gizmoToolbar.addCommand("ExpressionWaveGenerator", "nuke.createNode('ExpressionWaveGenerator')", icon='chromab.png')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIZMOS toolbar Pixomondo
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

NodesToolbar = nuke.toolbar("Nodes")
pixToolbar = NodesToolbar.addMenu("Pixo",icon="pixomondo.png")

pixToolbar.addCommand("P_Matte", "nuke.createNode('P_Matte')", icon="")
pixToolbar.addCommand("P_Noise3D", "nuke.createNode('P_Noise3D')", icon="")
pixToolbar.addCommand("P_Ramp", "nuke.createNode('P_Ramp')", icon="")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIZMOS toolbar Luma tools
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

NodesToolbar = nuke.toolbar("Nodes")
lumaToolbar = NodesToolbar.addMenu("luma",icon="luma.png")

lumaToolbar.addCommand("L_AlphaClean", "nuke.createNode('L_AlphaClean')", icon="")
lumaToolbar.addCommand("L_AspectMask", "nuke.createNode('L_AspectMask')", icon="")
lumaToolbar.addCommand("L_BlurHue", "nuke.createNode('L_BlurHue')", icon="")
lumaToolbar.addCommand("L_CameraBlur", "nuke.createNode('L_CameraBlur')", icon="")
lumaToolbar.addCommand("L_ChannelSolo", "nuke.createNode('L_ChannelSolo')", icon="")
lumaToolbar.addCommand("L_CropBBox", "nuke.createNode('L_CropBBox')", icon="")
lumaToolbar.addCommand("L_Despill", "nuke.createNode('L_Despill')", icon="")
lumaToolbar.addCommand("L_ExponBLur", "nuke.createNode('L_ExponBlur')", icon="")
lumaToolbar.addCommand("L_Fuse", "nuke.createNode('L_Fuse')", icon="")
lumaToolbar.addCommand("L_Grain", "nuke.createNode('L_Grain')", icon="")
lumaToolbar.addCommand("L_Icolor", "nuke.createNode('L_Icolor')", icon="")
lumaToolbar.addCommand("L_Ramp", "nuke.createNode('L_Ramp')", icon="")
lumaToolbar.addCommand("L_SpotRemover", "nuke.createNode('L_SpotRemover')", icon="")
lumaToolbar.addCommand("L_SwitchMatte", "nuke.createNode('L_SwitchMatte')", icon="")







#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIZMOS toolbar Pixelfudger
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



import pixelfudger


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deadline 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


import DeadlineNukeClient
menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("&Thinkbox")
tbmenu.addCommand("Submit Nuke To Deadline", DeadlineNukeClient.main, "")
#This is done to only add the Frame Server in Nuke Studio.
#Try-except is for older versions of Nuke.
try:
    if nuke.env[ 'studio' ]:
        import DeadlineNukeFrameServerClient
        tbmenu.addCommand("Reserve Frame Server Slaves",
            DeadlineNukeFrameServerClient.main, "")
except:
    pass



