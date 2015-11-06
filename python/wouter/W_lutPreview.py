#Wouter Gilsing 2014 

import nuke

def LUTPreview():

    LUTPreviewNode = nuke.createNode('LUTPreview')

    try:
        seqList = ['OP010','HC020','CL030','GE040','UW050']
        curSeq = nuke.root().name().split('/sequences/')[1].split('/')[0]

        if curSeq in seqList:
            LUTPreviewNode.knob('output').setValue(curSeq)

    except Exception:
        pass
   
   
nuke.menu("Nuke").addCommand("SpaceBetweenUs/LUTPreview", LUTPreview )