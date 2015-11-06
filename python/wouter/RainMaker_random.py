import nuke
import random

def createRainMaker():
    randomValue = random.randrange(0,40)
    rainNode = nuke.createNode('RainMaker4')
    rainNode.knob('lifetime').setValue(nuke.Root().knob('last_frame').value() - 950)
    rainNode.knob('start_frame').setValue(950)
    rainNode.knob('start_frame_1').setValue(950)
    rainNode.knob('start_frame_2').setValue(950)
    rainNode.knob('label').setValue('[value prerender_seed]')
    try:
        rainNode.knob('prerender_seed').setValue(randomValue)
    except:
        pass
    
nuke.toolbar("Nodes").addCommand("Gizmos/RainMaker", createRainMaker)
