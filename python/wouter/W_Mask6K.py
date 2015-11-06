import nuke

def Mask6K():
    recNode = nuke.createNode('Rectangle', inpanel = False)
    recNode.knob('area').setValue([0,13,2048,1067])
    recNode.knob('output').setValue('alpha')
    recNode.knob('invert').setValue(True)
    recNode.knob('label').setValue('6K mask')
    recNode.knob('tile_color').setValue(255)

menubar = nuke.menu("Nuke").addCommand("SpaceBetweenUs/RED/6K mask", Mask6K)