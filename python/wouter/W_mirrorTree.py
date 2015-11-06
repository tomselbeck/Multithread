#Wouter Gilsing 2014

import nuke

def mirrorTree():
	selection = nuke.selectedNodes()

	#check if selection isn't empty

	if selection == []:
		nuke.message('No nodes selected')
		return

	#collect all position data

	allPositions = []

	for i in selection:
		allPositions.append(i.xpos())

	minPosition = min(allPositions)
	maxPosition = max(allPositions)

	#mirror data around centerpoint and apply to selected nodes

	for i in selection:
		newPosition = minPosition + (maxPosition - i.xpos())
		i.setXpos(newPosition)

#add to menu 

nuke.menu("Nuke").addCommand("Edit/Node/Mirror Selected", mirrorTree)