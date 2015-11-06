import nuke
import os
import random

beautyTemplate = ['beauty']
passesTemplate = ['direct_diffuse','indirect_diffuse','reflection', 'refraction', 'emission', 'direct_specular', 'direct_specular_2', 'indirect_specular', 'indirect_specular_2', 'shallow_scatter', 'mid_scatter', 'deep_scatter', 'primary_specular', 'secondary_specular', 'sheen', 'specular', 'sss', 'mesh_light_beauty', 'single_scatter', 'direct_backlight', 'indirect_backlight']
utilityTemplate = ['Z', 'N', 'P', 'motionvector', 'opacity']

passesReads = []
utilityReads = []
mattesReads = []

nodesToConnectTo = []

allNodesinTree = []


colors = [8519679, 122093567, 2530047, 1930751]

tilecolor = 8519679


def clearSelection():
    nuke.selectAll()
    nuke.invertSelection()


def autoBackdropAdjusted(label):

    selNodes = nuke.selectedNodes()
    
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
      
    left, top, right, bottom = (-10, -80, 10, 35)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)
    
    backdropNode = nuke.nodes.BackdropNode( xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, label = label, note_font_size = 50 )
    
    backdropNode.knob('tile_color').setValue(tilecolor)
    
    allNodesinTree.append(backdropNode)
    
def sortList(list):

    sortedList = []

    if list == passesReads:
        templateList = passesTemplate
    else:
        templateList = utilityTemplate
    
    templist = []
    
    for i in list:
        templist.append(i.knob('label').value())

    for i in templateList:

        for a in list:
    
            if a.knob('label').value() == i:
                
                sortedList.append(a)

    return sortedList
    

def createSetupPasses(curRead):
    global allNodesinTree
    global nodesToConnectTo
    
    clearSelection()
    
    #CREATION SETUP

    curRead.knob('selected').setValue(True)
    
    reformatNode = nuke.createNode('Reformat', inpanel=False)
    reformatNode.knob('format').setValue('SpaceBetweenUs 2k')
    reformatNode.knob('pbb').setValue(True)
    
    copyNode = nuke.createNode('Copy',  inpanel=False)
    dotNode1 = nuke.createNode('Dot',  inpanel=False)
    unpremultNode = nuke.createNode('Unpremult',   inpanel=False)
    gradeNode = nuke.createNode('Grade',   inpanel=False)
    premultNode = nuke.createNode('Premult',   inpanel=False)
    dotNode2 = nuke.createNode('Dot',  inpanel=False)
            
    clearSelection()
            
    subtractMergeNode = nuke.createNode('Merge2', 'operation from output rgb', False)
    subtractMergeNode.knob('disable').setValue(True)
    subtractMergeNode.setInput(1,dotNode1)
    subtractMergeNode.setInput(0,nodesToConnectTo[1])
            
    addMergeNode = nuke.createNode('Merge2', 'operation plus output rgb', False)
    addMergeNode.knob('disable').setValue(True)
    addMergeNode.setInput(1,dotNode2)
    addMergeNode.setInput(0,subtractMergeNode)
            
    clearSelection()
    
    dotNode0 = nuke.createNode('Dot',  inpanel=False)
    copyNode.setInput(1,dotNode0)
    copyNode.setInput(0,reformatNode)
    dotNode0.setInput(0,nodesToConnectTo[0])
    
    #POSITIONING
    
    posXOffset = 0
    posYOffset = 30
    
    curReadPosX = reformatNode.xpos() + posXOffset 
    curReadPosY = reformatNode.ypos() + posYOffset - 87

    copyNode.setXpos(curReadPosX)
    dotNode1.setXpos(curReadPosX+34)
    unpremultNode.setXpos(curReadPosX)
    gradeNode.setXpos(curReadPosX)
    premultNode.setXpos(curReadPosX)
    dotNode2.setXpos(curReadPosX+34)
    
    subtractMergeNode.setXpos(curReadPosX + 130)
    addMergeNode.setXpos(curReadPosX + 130)

    dotNode0.setXpos(curReadPosX - 130)

    copyNode.setYpos(curReadPosY + 98)
    dotNode0.setYpos(curReadPosY + 108)
    dotNode1.setYpos(curReadPosY + 136)
    subtractMergeNode.setYpos(curReadPosY + 132)
    unpremultNode.setYpos(curReadPosY + 162)
    gradeNode.setYpos(curReadPosY + 192)
    premultNode.setYpos(curReadPosY + 222)
    dotNode2.setYpos(curReadPosY + 256)  
    addMergeNode.setYpos(curReadPosY + 251)  
    
    #LABELING
    
    clearSelection()

    allNodes = [curRead, copyNode, dotNode0, dotNode1, subtractMergeNode, unpremultNode, gradeNode, premultNode, dotNode2, addMergeNode, reformatNode]
    for i in allNodes:
        i.knob('selected').setValue(True)

    autoBackdropAdjusted(curRead.knob('label').value())
    clearSelection()
    
    
    nodesToConnectTo = [dotNode0, addMergeNode]
    
    allNodesinTree = allNodesinTree + allNodes
    

def buildNodeTree():

    global passesReads
    global utilityReads
    global mattesReads
    
    global nodesToConnectTo
    global allNodesinTree
    
    global tilecolor
    
    tilecolor = random.choice(colors)
    beautyReads = ''
    
    for i in nuke.selectedNodes():
        if i.Class() != "Read":
            i.knob('selected').setValue(False)
       
    
        
    selection = nuke.selectedNodes()
        
    for i in selection:

        fileName = i.knob('file').value().split('/')[-1]
        aovName = fileName.split('.')[0].split('_v')[1]
        aovName = aovName.replace(aovName[:3],'')
        if aovName[0] == '_':
            aovName = aovName[1:]
        aovName = aovName.split('_%')[0]
        i.knob('label').setValue(aovName)

        if aovName in beautyTemplate:
             beautyReads = i
        elif aovName in passesTemplate:
            passesReads.append(i)
        elif aovName in utilityTemplate:
            utilityReads.append(i)
        else:
            mattesReads.append(i)

    if  selection == []:
        nuke.message('Selection is empty')
        return
    elif beautyReads == '': 
        nuke.message('One does not simply build a tree without a Beauty')
        return


            
    passesReads = sortList(passesReads)
    utilityReads = sortList(utilityReads)

    allNodesinTree = allNodesinTree + utilityReads + mattesReads

    #------------------------------------------------------------------------------
    #BEAUTY NODE
    #------------------------------------------------------------------------------

    beautyPosition = [beautyReads.xpos(), beautyReads.ypos()]
    nodesToConnectTo = []

    clearSelection()

    #CREATION

    beautyReads.knob('selected').setValue(True)
    reformatNode0 = nuke.createNode('Reformat', inpanel=False)
    dotNode0 = nuke.createNode('Dot', inpanel=False)
    dotNode1 = nuke.createNode('Dot', inpanel=False)

    reformatNode0.knob('format').setValue('SpaceBetweenUs 2k')
    reformatNode0.knob('pbb').setValue(True)
    curYpos = reformatNode0.ypos()
    reformatNode0.setYpos(curYpos + 20)
    #POSITIONING

    dotNode1.setXpos(beautyPosition[0] - 130 - 130)
    dotNode0.setXpos(beautyPosition[0] + 164 - 130) 

    dotNode0.setYpos(beautyPosition[1] + 150)
    dotNode1.setYpos(beautyPosition[1] + 150)

    #LABELING

    clearSelection()

    allNodes = [beautyReads, reformatNode0, dotNode0, dotNode1]
    for i in allNodes:
        i.knob('selected').setValue(True)

    autoBackdropAdjusted('Beauty')
    clearSelection()

    nodesToConnectTo = [dotNode1, dotNode0]


    allNodesinTree = allNodesinTree + allNodes

    #------------------------------------------------------------------------------
    #UTILITY NODES
    #------------------------------------------------------------------------------

    for i in utilityReads:
        
        clearSelection()
        i.knob('selected').setValue(True)
        
        indexnumber = utilityReads.index(i)
        i.setXpos(beautyPosition[0] -130)
        i.setYpos((beautyPosition[1]+230) - (-170*indexnumber))
        
        reformatNode = nuke.createNode('Reformat', inpanel=False)
        reformatNode.knob('format').setValue('SpaceBetweenUs 2k')
        reformatNode.knob('pbb').setValue(True)
        
        dotNode = nuke.createNode('Dot', inpanel=False)
        copyNode = nuke.createNode('Copy', inpanel=False)
        copyNode.setInput(0,nodesToConnectTo[1])
        copyNode.setInput(1,dotNode)
        
        nodesToConnectTo = [nodesToConnectTo[0], copyNode]
        
        clearSelection()
        
        if i.knob('label').value() == 'Z':
            copyNode.knob('from0').setValue('rgba.alpha')
            copyNode.knob('to0').setValue('depth.Z')        
            
            copyNode.setYpos(copyNode.ypos()-6)
            
        elif i.knob('label').value() == 'N':
            nuke.Layer('N', ['N.x', 'N.y', 'N.z']) 
            copyNode.knob('from0').setValue('rgba.red')
            copyNode.knob('from1').setValue('rgba.green')
            copyNode.knob('from2').setValue('rgba.blue')
            copyNode.knob('to0').setValue('N.x')
            copyNode.knob('to1').setValue('N.y')
            copyNode.knob('to2').setValue('N.z')
            
            copyNode.setYpos(copyNode.ypos()-19)
            
        elif i.knob('label').value() == 'P':
            nuke.Layer('P', ['P.x', 'P.y', 'P.z']) 
            copyNode.knob('from0').setValue('rgba.red')
            copyNode.knob('from1').setValue('rgba.green')
            copyNode.knob('from2').setValue('rgba.blue')
            copyNode.knob('to0').setValue('P.x')
            copyNode.knob('to1').setValue('P.y')
            copyNode.knob('to2').setValue('P.z')
            
            positionToPointsNode = nuke.createNode("PositionToPoints2", inpanel=False)
            positionToPointsNode.setXpos(copyNode.xpos()+130)
            positionToPointsNode.setYpos(copyNode.ypos())
            positionToPointsNode.setInput(0,copyNode)
            positionToPointsNode.knob('P_channel').setValue('P')
            positionToPointsNode.knob('N_channel').setValue('N')
            allNodesinTree.append(positionToPointsNode)
            
            copyNode.setYpos(copyNode.ypos()-19)
                
        elif i.knob('label').value() == 'motionvector':
            nuke.Layer('motion', ['motion.u', 'motion.v', 'motion.w']) 
            copyNode.knob('from0').setValue('rgba.red')
            copyNode.knob('from1').setValue('rgba.green')
            copyNode.knob('from2').setValue('rgba.blue')
            copyNode.knob('to0').setValue('motion.u')
            copyNode.knob('to1').setValue('motion.v')
            copyNode.knob('to2').setValue('motion.w')
            
            copyNode.setYpos(copyNode.ypos()-19)
            
        elif i.knob('label').value() == 'opacity':
            copyNode.knob('from0').setValue('rgba.red')
            copyNode.knob('to0').setValue('rgba.alpha')
            
            copyNode.setYpos(copyNode.ypos()-6)
            
        allNodesinTree.append(reformatNode)
        allNodesinTree.append(copyNode)
        allNodesinTree.append(dotNode)
        
        
    clearSelection()

    #------------------------------------------------------------------------------
    #PASSES NODES
    #------------------------------------------------------------------------------


        
        
    yoffset = 0

    if nodesToConnectTo[0] == dotNode0 or nodesToConnectTo[0].Class() == 'Merge2':
        yoffset = 50
    else:
        yoffset = 170


    for i in passesReads:
                     
        indexnumber = passesReads.index(i)

        i.setXpos(beautyPosition[0] -130)
        i.setYpos(nodesToConnectTo[1].ypos()+ yoffset + ((indexnumber ) * 450))

    for i in passesReads:    
        createSetupPasses(i)
        
        
    #---------------------------------
    #MATTES
    #---------------------------------
    clearSelection()

    for i in mattesReads:
        
        indexnumber = mattesReads.index(i)
        i.setXpos(beautyPosition[0] - 500)
        i.setYpos(beautyPosition[1]+ 260 + (indexnumber*150))
        i.knob('selected').setValue(True)

        selNodes = nuke.selectedNodes()
        
        bdX = min([node.xpos() for node in selNodes])
        bdY = min([node.ypos() for node in selNodes])
        bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
        bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY
          
        left, top, right, bottom = (-50, -80, 50, 35)
        bdX += left
        bdY += top
        bdW += (right - left)
        bdH += (bottom - top)
          
        backdropNode = nuke.nodes.BackdropNode( xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, label = 'Mattes', note_font_size = 50 )
        
        backdropNode.knob('tile_color').setValue(tilecolor)
        
        allNodesinTree.append(backdropNode)
    clearSelection()
        
    #---------------------------------
    #ADD STICKY NODE
    #---------------------------------

    stickyNode = nuke.createNode('StickyNote', inpanel=False)
    labelvalue = '    CG RENDER    '
    stickyNode.knob('label').setValue(labelvalue)
    stickyNode.knob('note_font_size').setValue(100)
    stickyNode.setXpos(beautyPosition[0] - 25 -  (len(labelvalue)*35))
    stickyNode.setYpos(beautyPosition[1]-263)
    stickyNode.knob('tile_color').setValue(tilecolor)

    allNodesinTree.append(stickyNode)

    #---------------------------------
    #SELECT TREE
    #---------------------------------

    clearSelection()

    for i in allNodesinTree: 
        i.knob('selected').setValue(True)
        
    passesReads = []
    utilityReads = []
    mattesReads = []
    
    nodesToConnectTo = []
    allNodesinTree = []
    
    for i in nuke.selectedNodes():
        if i.Class() == 'Read':
            i.knob('label').setValue('')
    
    
menubar = nuke.menu("Nuke").addCommand("SpaceBetweenUs/Grow Tree", buildNodeTree )