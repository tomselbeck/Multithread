import nuke


def importAxes():
    for i in nuke.allNodes():
        i.knob('selected').setValue(False)
    beaconSpotSL = nuke.createNode('Axis2')
    for i in nuke.allNodes():
        i.knob('selected').setValue(False)
    beaconSpotSR = nuke.createNode('Axis2')

    beaconSpotSL.knob('translate').setValue([-918,515,-815])
    beaconSpotSR.knob('translate').setValue([-275,515,-815])

    beaconSpotSL.knob('label').setValue('beaconSpotSL')
    beaconSpotSR.knob('label').setValue('beaconSpotSR')

    beaconSpotSL.knob('tile_color').setValue(4290970879L)
    beaconSpotSR.knob('tile_color').setValue(4290970879L)

nuke.menu("Nuke").addCommand("SpaceBetweenUs/Sequence/GE040/import Spotlight Axes", importAxes )
