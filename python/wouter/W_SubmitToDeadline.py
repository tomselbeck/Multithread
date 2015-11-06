#Wouter Gilsing - 2015

import nuke
import sys

def test():
    print 'test'
    
def submit():
    nuke.Root().knob('onScriptLoad').setValue('')
    nuke.scriptSave()
    
    reposPath = 'R://submission/Nuke/Main'
    submittedPath = 'Z:\\Projects\\the_space_between_us\\tmp\\lensdistortion\\submitted'

    if reposPath not in sys.path :
        print "Appending \"" + reposPath + "\" to system path to import SubmitNukeToDeadline module"
        sys.path.append( reposPath )

    import SubmitNukeToDeadline

    SubmitNukeToDeadline.SubmitToDeadlineWithoutPrompt( reposPath )


