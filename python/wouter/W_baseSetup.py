#Wouter Gilsing 2014
try:
    import sgtk
except:
    pass
import nuke

def autoBackdrop(nodes,labeltext):

	bdX = (min([node.xpos() for node in nodes])) + -110
	bdY = (min([node.ypos() for node in nodes])) + -80
	bdW = (max([node.xpos() + node.screenWidth() for node in nodes]) - bdX) +180
	bdH = (max([node.ypos() + node.screenHeight() for node in nodes]) - bdY) + 90
   
	n = nuke.nodes.BackdropNode(xpos = bdX,bdwidth = bdW,ypos = bdY,bdheight = bdH, label = '<center>' + labeltext + '</center>', note_font_size=42)
	
	return n
    
def createBaseSetup():
    
    for i in nuke.allNodes():
        i.knob('selected').setValue(False)
        
    engine = sgtk.platform.current_engine()
    app = engine.apps["tk-nuke-writenode"]
    app_module = app.import_module("tk_nuke_writenode")
    handler = app_module.TankWriteNodeHandler(app)

    projectFormat = 'SpaceBetweenUs 2k'

    #CREATION

    removeNode = nuke.createNode('Remove', inpanel = False)
    reformatNode = nuke.createNode('Reformat', inpanel = False)

    dotNode1 = nuke.createNode('Dot', inpanel = False)
    
    aspectNode = nuke.createNode('AspectPreview', inpanel = False)
    slateNode = nuke.createNode('ShotSlate', inpanel = False)
    colorspaceNode1 =  nuke.createNode('Colorspace', inpanel = False)
    writeNode1 = handler.create_new_node('Preview Render')

    for i in nuke.selectedNodes():
        i.knob('selected').setValue(False)


    dotNode2 = nuke.createNode('Dot', inpanel = False)
    dotNode2.setInput(0, dotNode1)

    timecodeNode = nuke.createNode('AddTimeCode')
    colorspaceNode2 = nuke.createNode('Colorspace', inpanel = False)
    writeNode2 = handler.create_new_node('Final Render')

    #PROPERTIES
    aspectNode.knob('resolution').setValue('HD')
    
    removeNode.knob('operation').setValue('keep')
    removeNode.knob('channels').setValue('rgb')

    reformatNode.knob('resize').setValue('none')
    reformatNode.knob('black_outside').setValue(True)
    reformatNode.knob('format').setValue(projectFormat)

    colorspaceNode1.knob('colorspace_out').setValue('sRGB')
    colorspaceNode2.knob('colorspace_out').setValue('Cineon')

    writeNode1.knob('slateName').setValue(slateNode.name())

    timecodeNode.knob('frame').setValue(1001)
    timecodeNode.knob('useFrame').setValue(True)
    timecodeNode.knob('metafps').setValue(False)
    timecodeNode.knob('startcode').setValue('00:00:00:00')
    timecodeNode.knob('fps').setValue(25)

    #PLACEMENT

    startPos = [removeNode.xpos(),removeNode.ypos()]

    reformatNode.setXpos(startPos[0])

    dotNode1.setXpos(startPos[0])
  
    slateNode.setXpos(startPos[0])
    aspectNode.setXpos(startPos[0])
    colorspaceNode1.setXpos(startPos[0])
    writeNode1.setXpos(startPos[0])

    dotNode2.setXpos(startPos[0]+355)
    colorspaceNode2.setXpos(dotNode2.xpos())
    timecodeNode.setXpos(dotNode2.xpos())
    writeNode2.setXpos(dotNode2.xpos())

    reformatNode.setYpos(startPos[1]+45)
    
    dotNode1.setYpos(startPos[1]+45+165)
    dotNode2.setYpos(startPos[1]+45+165)
    
    timecodeNode.setYpos(startPos[1]+45+165+70+20)    
    colorspaceNode2.setYpos(startPos[1]+45+165+70+50+50-20)

    
    aspectNode.setYpos(startPos[1]+45+165+70)
    slateNode.setYpos(startPos[1]+45+165+70+50)
    colorspaceNode1.setYpos(startPos[1]+45+165+70+50+50)
    writeNode1.setYpos(startPos[1]+45+165+70+50+50+70)
    writeNode2.setYpos(startPos[1]+45+165+70+50+50+70)

    dotNode1.setXpos(dotNode1.xpos()+34)
    dotNode2.setXpos(dotNode2.xpos()+34)

    #StickyNote

    stickyNode = nuke.createNode('StickyNote', inpanel = False)

    stickyNode.knob('label').setValue('     current framerange:    \n[value root.first_frame] - [value root.last_frame]')
    stickyNode.knob('note_font_size').setValue(50)
    stickyNode.setXpos(startPos[0]-70)
    stickyNode.setYpos(startPos[1]+585)

    #BACKDROP

    jpgNodes = [dotNode1, colorspaceNode1, aspectNode, slateNode, writeNode1]
    dpxNodes = [dotNode2, colorspaceNode2, writeNode2]

    #removeNode
    #reformatNode

    backdropNode1 = autoBackdrop(jpgNodes,'JPG Preview')
    backdropNode2 = autoBackdrop(dpxNodes,'DPX Render')

menubar = nuke.menu("Nuke").addCommand("SpaceBetweenUs/Comp BaseSetup", createBaseSetup )
