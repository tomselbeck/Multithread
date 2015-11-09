
import os
import nuke
import T_DictionaryCreator
from T_DictionaryCreator import *


def log(project):
    projectname = project
    project = project + "/"

    shotdir = {}
    shotcount = 0
    serv = "Z:/projects/"
    editorial = "editorial/"
    #project = "PipelineDev/"
    plates ="plates/"
    nulversie = "nulversie/"
    lastpublish ="lastpublish/"
    elements = "elements/"
    null = "null/"
    sequences = "sequences/"
    Comp = "Comp/"
    comp = "comp/"
    publish = "publish/"
    fslash = "/"
    resolution = "/1920x1080/"



    print ('Running LogCreator,current project %s' % project)

    ## Creating Path variables ##

    logname = projectname + "_Database.txt"
    logpath = serv+project+editorial+nulversie+logname

    print logpath
    ## Check if log already exists, if not, create a new one 

    if not os.path.exists(logpath):
        print ('Log does not yet exists, creating a new log: %s'%logpath)
        log = open(logpath, "w");
        log.close 
        pass




    ## Create a log for every shot, containing Sequencename, Shotname, Latest version, Frame in and Frame Out 

    CreateDictionary(project,shotdir,shotcount)
    shotcount = CreateDictionary(project,shotdir,shotcount)


    log = open(logpath, "w");

    for x in xrange(0,shotcount):
        
        ## Calculate the latest version #
        vpath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp
        if os.path.exists(vpath) == True: 
            v = max(os.listdir(vpath))
            #print v
                #print shotdir[x][0],shotdir[x][1]        
        ## folder to look for published shots
            sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp+v+resolution
            destdir = serv+project+editorial+nulversie+null+shotdir[x][0]+fslash+shotdir[x][1]+fslash
            #print (sourcedir)
            


            ## List all filenames 
            for dirName, subdirList, fileList in os.walk(sourcedir):
                #print('Found directory: %s' % dirName)
                
                
                for fname in fileList:
                    sourcefilename =('%s' % fname)   


                    
                    ## Create new filepaths and replace version numbers to 0's
                    #print (shotdir[x][0]+fslash+shotdir[x][1]+fslash+v)
                    logwrite = sourcefilename
                    #logwrite = ('%s'%shotdir[x][0]+'|'+'%s'%shotdir[x][1]+'|'+v)
                    #print logwrite
                    log.write(logwrite)
                    log.write("\n")


    log.close()
    print ("Finished updating Log")


    pass
project = ("PipelineDev")
log(project)

