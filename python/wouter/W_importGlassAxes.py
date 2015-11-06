import nuke

def glass2CornerPin():

    nuke.scriptSource("Z:/Projects/the_space_between_us/dev/nuke/python/wouter/glass2CornerPin.nk")
    
nuke.menu("Nuke").addCommand("SpaceBetweenUs/Sequence/CL030/import Glass Axes Setup", glass2CornerPin )
