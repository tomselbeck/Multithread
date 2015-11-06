#Wouter Gilsing 2014

import nuke

# main function

def AlignNodes(a):

    allHorizontal = []
    allVertical = []

    if not nuke.selectedNodes():
        nuke.message('No nodes selected')

    else:

        for i in nuke.selectedNodes():
            allHorizontal.append(i['xpos'].value())
            allVertical.append(i['ypos'].value())

        destinationLeft = min(allHorizontal)
        destinationRight = max(allHorizontal)
        destinationUp = min(allVertical)
        destinationDown = max(allVertical)
        
        if a == "left":
            for i in nuke.selectedNodes():
                i['xpos'].setValue(destinationLeft)

        if a == "right":
            for i in nuke.selectedNodes():
                i['xpos'].setValue(destinationRight)

        if a == "up":
            for i in nuke.selectedNodes():
                i['ypos'].setValue(destinationUp)

        if a == "down":
            for i in nuke.selectedNodes():
                i['ypos'].setValue(destinationDown)

# Define seperate functions for directions

def AlignLeft():
    AlignNodes("left")

def AlignRight():
    AlignNodes("right")

def AlignUp():
    AlignNodes("up")

def AlignDown():
    AlignNodes("down")

# Add to menu

nuke.menu("Nuke").addCommand("Edit/Node/Align/Left", AlignLeft, "Alt+left")
nuke.menu("Nuke").addCommand("Edit/Node/Align/Right", AlignRight, "Alt+right")
nuke.menu("Nuke").addCommand("Edit/Node/Align/Up", AlignUp, "Alt+up")
nuke.menu("Nuke").addCommand("Edit/Node/Align/Down", AlignDown, "Alt+down")