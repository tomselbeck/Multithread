#Wouter Gilsing 2015

import nuke

def toggleInvertMask():
    for i in nuke.selectedNodes():
        try:
            i.knob('invert_mask').setValue(1-i.knob('invert_mask').value()) 
        except:
            continue

toggleInvertMask()


# Add to menu
        
nuke.menu("Nuke").addCommand("Edit/Node/Toggle Invert Mask", toggleInvertMask, 'alt+shift+x')