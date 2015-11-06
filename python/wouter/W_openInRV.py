import subprocess
import nuke

def openInRV():
    curNode = nuke.selectedNode()
    if curNode.Class() == 'WriteTank':
        knobName = 'cached_path'
    else:
        knobName = 'file'

    fileName = curNode.knob(knobName).value()

    cmd = ['"C:\\Program Files\\Tweak\\RV-4.0.11-64\\bin\\rv.exe"']

    cmd.append("'" + fileName + "'")
    cmd.append('-rec709')
    ocmd = ' '.join(cmd)
    subprocess.Popen(ocmd, shell=True)

#openInRV()

nuke.toolbar("Nodes").addCommand("rv", openInRV, icon="rvNuke.png")