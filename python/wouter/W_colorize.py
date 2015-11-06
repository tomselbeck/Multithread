#Wouter Gilsing 2014

import nuke

#Check selection
def colorize():

    if not nuke.selectedNodes():
        nuke.message('No nodes selected')
        return

    #Check for backdrops and stickynodes

    backDropCheck = False

    for n in nuke.selectedNodes():
        if (n.Class() == "BackdropNode") or (n.Class() == "StickyNote"): 
            backDropCheck = True

    #Get color

    currentCol = int(nuke.selectedNodes()[0].knob("tile_color").getValue())
    newCol = nuke.getColor(currentCol)

    #Set color

    if newCol:
        for n in nuke.selectedNodes():

            if backDropCheck == True :
                if (n.Class() == "BackdropNode") or (n.Class() == "StickyNote"):
                    n['tile_color'].setValue(newCol)

            if backDropCheck == False:
                n['tile_color'].setValue(newCol)

# Add to menu
        
nuke.menu("Nuke").addCommand("Edit/Node/Color...", colorize)