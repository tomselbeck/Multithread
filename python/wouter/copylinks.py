#Wouter Gilsing 2014

import nuke
# import this module (comes with nuke) to use the clipboard
from PySide import QtGui

clipboard = QtGui.QApplication.clipboard()

# create variables for diffent knobs

UVList = ['u','v']
UV_KnobList = ['UV_Knob']

WHList = ['w','h']
WH_KnobList = ['WH_Knob']


XYZList = ['x','y','z']
XYZ_KnobList = [ 'XY_Knob' , 'Scale_Knob' , 'XYZ_Knob' ]

ColorList = ['r','g','b','a']
Color_KnobList = ['AColor_Knob' , 'Color_Knob']

IArray_KnobList = ['IArray_Knob']

KeyerList = ['A','B','C','D']
Keyer_KnobList = ['Keyer_Knob']

Box3List =  ['x','y','n','r','t','f']
Box3_KnobList = ['Box3_Knob']


BBoxList = ['x','y','r','t']
BBox_KnobList = ['BBox_Knob']

multiFieldKnobList = UV_KnobList + WH_KnobList + XYZ_KnobList + Color_KnobList + IArray_KnobList + Keyer_KnobList + Box3_KnobList + BBox_KnobList

# apperently the only way to get the index of a knob field is to use a piece of TCL code, grabbed from Nukepedia : http://www.nukepedia.com/python/getting-the-index-context-of-a-knob/

def getKnobIndex(x):
	try:
		tclGetAnimIndex = """
		 
		set thisanimation [animations]
		if {[llength $thisanimation] > 1} {
		 return "-1"
		 } else {
		  return [lsearch [in [join [lrange [split [in $thisanimation {animations}] .] 0 end-1] .] {animations}] $thisanimation]
		 }
		"""
		 
		indexNumber =  int(nuke.tcl(tclGetAnimIndex))
		if indexNumber < 0:
			raise

		curKnobClass = nuke.thisKnob().Class()

		if curKnobClass in UV_KnobList:
			fieldName = UVList[indexNumber]

		elif curKnobClass in WH_KnobList:
			fieldName = WHList[indexNumber]

		elif curKnobClass in XYZ_KnobList:
			fieldName = XYZList[indexNumber]

		elif curKnobClass in Color_KnobList:
			fieldName = ColorList[indexNumber]

		elif curKnobClass in IArray_KnobList:
			fieldName = str(indexNumber)

		elif curKnobClass in Keyer_KnobList:
			fieldName = KeyerList[indexNumber]

		elif curKnobClass in Box3_KnobList:
			fieldName = Box3List[indexNumber]

		elif curKnobClass in BBox_KnobList:
			fieldName = BBoxList[indexNumber]

		x = x + '.' + fieldName
		return x
	except:
		return x

def copyLinks():

	knobName = nuke.thisKnob().name()
	nodeName = nuke.thisNode().name()
	combinedName = nodeName+'.'+ knobName

	if nuke.thisKnob().Class() in multiFieldKnobList:
		combinedName = getKnobIndex(combinedName)

	# Copy the nodename, knobname and (when avialable)  the fieldname to the clipboard to be used in expressions
	clipboard.setText(combinedName)

nuke.menu('Animation').addCommand('copyClip','copyLinks()')