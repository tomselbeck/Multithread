import nuke

def importBeaconMesh():
    readgeo = nuke.createNode('ReadGeo2')
    readgeo.knob('file').setValue('Z:/Projects/the_space_between_us/assets/Environment/GE040_IslandLayout/Model/work/maya/beacon.abc')

nuke.menu("Nuke").addCommand("SpaceBetweenUs/Sequence/GE040/import Beacon Mesh", importBeaconMesh )