import nuke

def setDefaultsJPGRender():
    curNode = nuke.thisNode()
    if curNode.knob('file_type').value() == 'jpeg' or curNode.knob('file_type').value() == ' ':

        nuke.thisNode().knob("file_type").setValue('jpeg')
        nuke.thisNode().knob("_jpeg_quality").setValue(1)
