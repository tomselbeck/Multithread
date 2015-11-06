from hiero.core import *


sequenceName = "AUTO"
trackloc = 'C:\Users\t.selbeck\Desktop\testedit_01\GB010.edl'

# get the project by name
myProject = project("pipelineTest")
clipsBin = myProject.clipsBin()

for item in myProject.clipsBin().items():
  print item

sequence = Sequence(sequenceName)
clipsBin.addItem(BinItem(sequence)) 
# create a track to add items/clips to
track = VideoTrack("VideoTrack") 
sequence.importTracks(trackloc)



##AUTO.