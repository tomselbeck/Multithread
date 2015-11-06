# Regular expression example, replace 'Shot_003' with 'Shot_002'
import re
import nuke
oReadNodes = nuke.allNodes('Read')
oWriteNodes = nuke.allNodes('Write')


def local():
    
    print ("Setting file paths to local")
    oReadNodes = nuke.allNodes('Read')
    for oReadNode in oReadNodes:
        oPath =  oReadNode["file"].value()
        oNewPath = re.sub('(Z:/persoonlijk/tom/07_TWT_SYNC/)', 'A:/02_projects/03_twt/', oPath)
        oReadNode["file"].setValue(oNewPath)
        
    oWriteNodes = nuke.allNodes('Write')
    for oWriteNode in oWriteNodes:
        oPath =  oWriteNode["file"].value()
        oNewPath = re.sub('(Z:/persoonlijk/tom/07_TWT_SYNC/)', 'A:/02_projects/03_twt/', oPath)
        oWriteNode["file"].setValue(oNewPath)    

    
def server():
    
    print ("Setting file paths to server")
    oReadNodes = nuke.allNodes('Read')
    for oReadNode in oReadNodes:
        oPath =  oReadNode["file"].value()
        oNewPath = re.sub('(A:/02_projects/03_twt/)', 'Z:/persoonlijk/tom/07_TWT_SYNC/', oPath)
        oReadNode["file"].setValue(oNewPath)
        
    oWriteNodes = nuke.allNodes('Write')
    for oWriteNode in oWriteNodes:
        oPath =  oWriteNode["file"].value()
        oNewPath = re.sub('(A:/02_projects/03_twt/)', 'Z:/persoonlijk/tom/07_TWT_SYNC/', oPath)
        oWriteNode["file"].setValue(oNewPath) 
    







