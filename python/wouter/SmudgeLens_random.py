import nuke
import random

def createSmudgeLens():
    randomValue = random.randrange(0,250)
    smudgeNode = nuke.createNode('SmudgeLens')
    smudgeNode.knob('seed').setValue(randomValue)
    
nuke.menu("Nuke").addCommand("SpaceBetweenUs/RED/SmudgeLens", createSmudgeLens )
nuke.toolbar("Nodes").addCommand("Gizmos/SmudgeLens", createSmudgeLens)
