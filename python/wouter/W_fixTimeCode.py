import nuke

def changeTimeCode():
    try:
        for i in nuke.allNodes():
            if i.Class() == 'AddTimeCode':
                TimeKnob = i.knob('startcode')
                if TimeKnob.value() == '01:00:00:00':
                    TimeKnob.setValue('00:00:00:00')
                    nuke.message('De timecode van de DPX write stond verkeerd, nu staat ie goed.\nJe kunt dit schermpje wegklikken, ookal suggereert je cursor dat ie nog aan het laden is:)\n\nHappy Nuking  en veel liefs,\nWouter')
    except:
        pass

        
nuke.addOnScriptLoad(changeTimeCode)