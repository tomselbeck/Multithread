import nuke

def wigglewiggle():
    import random 

    expr = 'noise((t+seed)/speed)*amplitude'
    speedKnob = nuke.Double_Knob('speed','speed')
    amplitudeKnob = nuke.Double_Knob('amplitude','amplitude')
    randomKnob = nuke.Double_Knob('seed','seed')

    wiggleNode = nuke.createNode('Transform')
    wiggleNode.addKnob(speedKnob)
    wiggleNode.addKnob(amplitudeKnob)
    wiggleNode.addKnob(randomKnob)

    randomKnob.setValue(random.randrange(0,100))
    speedKnob.setValue(50)
    amplitudeKnob.setValue(25)

    wiggleNode.knob('translate').setExpression(expr,1)

    wiggleNode.knob('label').setValue('wiggle')

nuke.menu("Nuke").addCommand("SpaceBetweenUs/Sequence/UW050/WiggleWiggle", wigglewiggle )