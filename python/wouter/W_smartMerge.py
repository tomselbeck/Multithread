# Wouter Gilsing

import nuke

filterList = ['Defocus', 'Soften', 'Toe2', 'VectorBlur', 'ZDefocus2', 'MotionBlur3D', 'MotionBlur2D', 'Matrix', 'Median', 'Bilateral', 'Blur', 'FilterErode', 'Erode', 'Dilate']
timeList = ['Retime', 'TimeBlur', 'FrameHold', 'FrameRange', 'TimeClip', 'TimeWarp', 'TimeOffset', 'TimeEcho']
colorList = ['ColorCorrect', 'Grade', 'Clamp', 'Expression', 'Add', 'Gamma', 'Multiply', 'Invert']
transformList = ['TransformMasked', 'Transform', 'Mirror', 'Crop', 'IDistort', 'CornerPin2D']
channelList = ['ShuffleCopy', 'Shuffle']
othersList = ['Switch', 'NoOp', 'Dot', 'KeyMix']

skipList = filterList + timeList + colorList + transformList + channelList + othersList 

rotoList = ['Roto', 'Bezier', 'ChannelMerge']
keyerList = ['IBKColourV3', 'OFXuk.co.thefoundry.keylight.keylight_v201', 'Primatte3', 'Ultimatte', 'Difference', 'HueKeyer', 'Keyer']
drawList = ['Radial', 'Ramp', 'Rectangle']

channelMergeList = rotoList + keyerList + drawList

onlyAlphaList = ['rgba.alpha']

def smartMerge():

	if not nuke.selectedNodes():
		nuke.createNode('Merge2')
	else:
		focusNode = nuke.selectedNodes()[0]
		print focusNode.name()

		if focusNode.channels() == onlyAlphaList:
			stayinLoop = False
		else:
			stayinLoop = True

		while (focusNode.Class() in skipList) and (stayinLoop == True):
			if focusNode.dependencies():
				focusNode = focusNode.dependencies()[0]
			else:
				stayinLoop = False
			if focusNode.channels() == onlyAlphaList:
				stayinLoop = False

		if (focusNode.Class() in channelMergeList) or (focusNode.channels() == onlyAlphaList):
			if (not focusNode.dependencies()) and (focusNode.Class() in skipList):
				nuke.createNode('Merge2')
			else:
				nuke.createNode('ChannelMerge')
		else:
			nuke.createNode('Merge2')

nuke.toolbar("Nodes").addCommand("Merge/smartMerge", smartMerge, 'm', icon='Merge.png')