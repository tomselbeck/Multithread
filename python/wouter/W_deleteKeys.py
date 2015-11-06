#Wouter Gilsing 2014

import nuke

def deleteKeys(first,last):
    for i in range(first,last):
        nuke.thisKnob().removeKeyAt(i)

# create python panel to ask for desied framerange, then use that frame range to call the deleteKeys function

def deleteKeysCustom():
    
    projectFirst = int(nuke.Root().knob('first_frame').value())
    projectLast = int(nuke.Root().knob('last_frame').value())
    
    newLast = projectFirst
    newFirst = projectLast

    # Panel
    panel = nuke.Panel('Frame Range')
    panel.addSingleLineInput('framerange', str(projectFirst) + ' - ' + str(projectLast) )
    panel.show()

    newRange = panel.value('framerange').split('-')
    newFirst = int(newRange[0])
    newLast = int(newRange[1])  + 1

    # Check if frameRange changd, otherwise abort 

    if (newFirst == projectFirst) and ((newLast -1 )== projectLast):
        return
    else:
        deleteKeys(newFirst,newLast)

#add to menu

keymenu = nuke.menu('Animation').addMenu('Delete keys')

keymenu.addCommand('Delete keys forward','deleteKeys(nuke.frame()+1 , int(nuke.Root().knob("last_frame").value()))')
keymenu.addCommand('Delete keys backward','deleteKeys(int(nuke.Root().knob("first_frame").value()), nuke.frame())')
keymenu.addCommand('Delete keys custom','deleteKeysCustom()')

