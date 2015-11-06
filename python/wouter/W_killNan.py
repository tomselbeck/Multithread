import nuke

def killNan():
    expressionNode = nuke.createNode('Expression')
    expressionNode.knob('expr0').setValue('isnan(r)? 0 : r')
    expressionNode.knob('expr1').setValue('isnan(g)? 0 : g')
    expressionNode.knob('expr2').setValue('isnan(b)? 0 : b')
    expressionNode.knob('expr3').setValue('isnan(a)? 0 : a')
    expressionNode.knob('label').setValue('kill nan')


nuke.toolbar("Nodes").addCommand("Gizmos/W_killNan", killNan)