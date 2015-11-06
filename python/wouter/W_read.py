import nuke

def readKnobDefaults():
    nuke.thisNode().knob('colorspace').setValue('linear')
    nuke.thisNode().knob('on_error').setValue('nearest frame')
	
nuke.addOnUserCreate(readKnobDefaults, nodeClass = 'Read') 

