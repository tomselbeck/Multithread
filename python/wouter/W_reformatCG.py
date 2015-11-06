import nuke

def ReformatCG():
    reformatNode = nuke.createNode('Reformat')
    newName = reformatNode.name().replace('Reformat','ReformatCG')
    reformatNode.knob('name').setValue(newName)
    reformatNode.knob('format').setValue('SpaceBetweenUs 2k')
    reformatNode.knob('resize').setValue('none')
    reformatNode.knob('pbb').setValue('on')
    
menubar = nuke.menu("Nuke").addCommand("SpaceBetweenUs/Reformat CG", ReformatCG )