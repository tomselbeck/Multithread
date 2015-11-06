import nuke
import os
import sys

#Create Nodes

readNode = nuke.createNode('Read')
reformatNode = nuke.createNode('Reformat')
writeNode = nuke.createNode('Write')
nuke.addFormat( '1024 540 Shotgun Thumbnail' )

#Set Values

readNode.knob('file').setValue(sys.argv[1])
readNode.knob('on_error').setValue('nearest frame')

reformatNode.knob('format').setValue('Shotgun Thumbnail')

writeNode.knob('file').setValue(sys.argv[2])
writeNode.knob('file_type').setValue('png')
writeNode.knob('colorspace').setValue('sRGB')

#Write

nuke.execute(writeNode.name(), start=1, end=1, incr=1)
