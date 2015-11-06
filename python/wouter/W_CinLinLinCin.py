import nuke

def cinToLin():
    colorSpaceNode = nuke.createNode('Colorspace')
    colorSpaceNode.knob('colorspace_in').setValue('Cineon')
    colorSpaceNode.knob('colorspace_out').setValue('RGB')

def LinToCin():
    colorSpaceNode = nuke.createNode('Colorspace')
    colorSpaceNode.knob('colorspace_in').setValue('RGB')
    colorSpaceNode.knob('colorspace_out').setValue('Cineon')

nuke.toolbar("Nodes").addCommand("Color/Cin2Lin", cinToLin)
nuke.toolbar("Nodes").addCommand("Color/Lin2Cin", LinToCin)