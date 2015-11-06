import nuke
import ast
import os

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

import W_openDocs

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

NodesToolbar = nuke.toolbar("Nodes")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROJECT SETTINGS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

nuke.knobDefault("Root.format", "HD")  
nuke.knobDefault("Root.fps", "25.0")  


nuke.knobDefault("Root.first_frame","1001")
nuke.knobDefault("Root.last_frame","1100")

nuke.knobDefault("WriteTank.colorspace","linear")
nuke.knobDefault("Write.colorspace","linear")

import W_read

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# KNOBDEFAULTS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

nuke.knobDefault("TimeOffset.label","[expr [frame] - [value time_offset]]")
nuke.knobDefault("PostageStamp.hide_input","true")
nuke.knobDefault("Read.cacheLocal","always")
nuke.knobDefault("Roto.cliptype","no clip")
nuke.knobDefault("RotoPaint.cliptype","no clip")
nuke.knobDefault("Camera.frame_rate","25")
nuke.knobDefault("ScanlineRender.MB_channel","none")
nuke.knobDefault("Radial.area","0 0 1920 1080")
nuke.knobDefault("AppendClip.firstFrame","1001")

NodesToolbar.addCommand("Color/Math/Multiply", "nuke.createNode('Multiply').knob('value').setRange(0,1)", icon="ColorMult.png")
NodesToolbar.addCommand("Time/FrameHold", "nuke.createNode('FrameHold')['first_frame'].setValue( nuke.frame() )", icon='FrameHold.png')

NodesToolbar.addCommand("Draw/Text", "nuke.createNode('Text')", icon='Text.png')
NodesToolbar.addCommand("Draw/TextNew", "nuke.createNode('Text2')", icon='Text.png')

nuke.knobDefault("LD_3DE4_Radial_Standard_Degree_4.label","[expr 10 * [value this.tde4_focal_length_cm]]mm")

try:
    nuke.knobDefault("S_LensFlare.combine","Add")
except Exception:
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#MOCHA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

import send_to_mocha

mochaToolbar = NodesToolbar.addMenu("Mocha", icon='mocha.png')
mochaToolbar.addCommand( 'Send ReadNode to mocha', 'send_to_mocha.send_to_mocha()', icon='mocha.png')

import cornerPinToTracker    
mochaToolbar.addCommand('cornerPinToTracker', 'cornerPinToTracker.cornerPinToTracker()', icon='CornerPin.png')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# NEAT VIDEO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

neatVideoMenu = NodesToolbar.findItem("Neat Video")
neatVideoMenu.clearMenu()
NodesToolbar.removeItem("Neat Video")

neatVideoToolbar = NodesToolbar.addMenu("NeatVideo",icon="iron.png")
neatVideoToolbar.addCommand("Reduce Noise", "nuke.createNode('OFXcom.absoft.neatvideo_v2')", icon="denoise.png")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIZMOS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

gizmoToolbar = NodesToolbar.addMenu("Gizmos",icon="NukePedia.png")


gizmoToolbar.addCommand("W_Duplicator", "nuke.createNode('W_Duplicator')", icon="W_Duplicator.png")
gizmoToolbar.addCommand("W_Perspectinator", "nuke.createNode('W_Perspectinator')", icon="W_Perspectinator.png")
gizmoToolbar.addCommand("W_FirstScreening", "nuke.createNode('W_FirstScreening')", icon="W_FirstScreening.png")
gizmoToolbar.addCommand("W_Suppressor", "nuke.createNode('W_Suppressor')", icon="Color.png")

gizmoToolbar.addCommand("DespillMadness", "nuke.createNode('DespillMadness')", icon="NukePedia.png")
gizmoToolbar.addCommand("EdgeExtend", "nuke.createNode('EdgeExtend')", icon="FilterErode.png")
gizmoToolbar.addCommand("ImagePlane", "nuke.createNode('ImagePlane')", icon="planar_tracker.png")
gizmoToolbar.addCommand("nTransform", "nuke.createNode('nTransform')", icon="2D.png")
gizmoToolbar.addCommand("TrackingConverter", "nuke.createNode('TrackingConverter')", icon="CameraTracker.png")
gizmoToolbar.addCommand("mmColorTarget", "nuke.createNode('mmColorTarget')", icon='mmColorTarget.png')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# CUSTOM PYTHONSCRIPTS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

	#NukeMenu 
import W_colorize
import W_mirrorTree
import W_align
	
	#NodesMenu
import W_smartMerge

	#AnimationMenu
import W_deleteKeys
nuke.menu('Animation').addCommand('Set to current frame','nuke.thisKnob().setValue(nuke.frame())')

	#SnapMenu
import animatedSnap3D

	#Slate
import W_slate
import W_shotgunWrite

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# SHORTCUT EDITOR
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#DEADLINE
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

import DeadlineNukeClient
menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("&Thinkbox")
tbmenu.addCommand("Submit Nuke To Deadline", DeadlineNukeClient.main, "")

if nuke.menu('Nuke').items()[0].name() == 'Shotgun' :
    try:
        nuke.menu("Nuke").removeItem("Shotgun")
    except Exception:
        pass
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#SPACE BETWEEN US
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
NUKE.KNOBdEAFAULTS('roto.aspectpreview', 'nuke.createNode())
menubar = nuke.menu("Nuke")
spacemenu = menubar.addMenu("SpaceBetweenUs")
spacemenu.addCommand("Slate/AssetSlate", "nuke.createNode('AssetSlate')")
spacemenu.addCommand("Slate/ShotSlate", "nuke.createNode('ShotSlate')")
import W_importSkydome
spacemenu.addCommand("AspectPreview", "nuke.createNode('AspectPreview')")
import W_lutPreview
import W_reformatCG
spacemenu.addCommand("RedDragon Grain", "nuke.createNode('RedDragonGrain')")
spacemenu.addCommand("RedDragon LensDistortion", "nuke.createNode('RedDragonLensDistortion')")
spacemenu.addCommand("Shotgun WriteGeo", "nuke.createNode('ShotgunWriteGeo')")


import W_speedTree
import W_baseSetup
import W_ShotgunWriteGeo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Remove temp menu that is constructed in init.py
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

tmpMenu = NodesToolbar.findItem("tmp")
tmpMenu.clearMenu()
NodesToolbar.removeItem("tmp")
