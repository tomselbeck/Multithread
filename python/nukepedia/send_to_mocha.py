# Copyright (c) 2014 Imagineer Systems Ltd
# Script: 'Send to mocha'
# Version: 1.0.0
# edited by Wouter Gilsing

import nuke
import nukescripts
import _winreg
import platform
import subprocess
import os

class mocha_locator_dialog(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Choose mocha executable location", "uk.co.thefoundry.FramePanel")
        self.path = nuke.File_Knob("path", "Path:")
        self.addKnob(self.path)

    def showDialog(self):
        result = nukescripts.PythonPanel.showModalDialog(self)
        if result:
            return (self.path.value())

class send_to_mocha():

    def __init__(self):

        self.mocha_path = self.get_mocha_path()
        if self.mocha_path != 'None':
            self.load_mocha_with_clip()

    def get_mocha_path(self):

        sys = platform.system()
        if sys == 'Darwin':
            default_path = '/Applications/mocha Pro.app/Contents/MacOS/mochapro'

        elif sys == 'Windows':
            default_path = r'C:\Program Files\Imagineer Systems Ltd\mocha Pro V4\bin\mochapro.exe'
        else:
            default_path = '/opt/isl/mochaproV4/bin/mochapro'

        if os.path.isfile(default_path) != True:
            nuke.message('Not a valid path:'+str(default_path))

        return default_path

    def get_readnode(self):
        try:
            selected_node = nuke.selectedNode()
        except:
            nuke.message('Please select a read node')
            return 0

        if selected_node.Class() == 'Read':
            footage_path = nuke.filename(selected_node, nuke.REPLACE)
            return footage_path
        else:
            nuke.message('Please select a read node')

    def open_mocha_with_file(self,filepath):

        #Open mocha
        
        #set prefs
        #________________________
        
        sceneFile = nuke.Root().name()

        if sceneFile != '' and sceneFile[:43] == 'Z:/Projects/the_space_between_us/sequences/':
            shot = sceneFile.split('/')[5]
            seq = shot.split('_')[0]
            path = 'Z:\\Projects\\the_space_between_us\\sequences\\' + seq + '\\' + shot+ '\\Matchmove\\publish\\matchmove\\mocha'
        else:
            path = 'C:/MoTemp'

        pathKey = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, 'Software\Imagineer Systems Ltd\mocha Pro 4')
        _winreg.SetValueEx(pathKey,'AbsoluteOutputDirectory',  0, _winreg.REG_SZ, path)
        _winreg.CloseKey(pathKey)


        absKey = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, 'Software\Imagineer Systems Ltd\mocha Pro 4')
        _winreg.SetValueEx(absKey,'OutputDirectoryAbsolutePath',  0, _winreg.REG_SZ, 'true')
        _winreg.CloseKey(absKey)

        #________________________
        
        footage_firstframe = nuke.selectedNode().firstFrame()

        in_point = str(nuke.Root().firstFrame()-footage_firstframe)
        out_point = str(nuke.Root().lastFrame()-footage_firstframe)

        frame_rate = str(nuke.Root().fps())
        cmd = [self.mocha_path, '--in', in_point, '--out', out_point, '--frame-rate', frame_rate, filepath]
        
        try:
            err = subprocess.Popen(cmd) #open mocha with the project file as a separate process
        except subprocess.CalledProcessError, e:
            print "Ping stdout output:\n", e.output

        return err

    def load_mocha_with_clip(self):
        filepath = self.get_readnode()
        if filepath:
            self.open_mocha_with_file(filepath)