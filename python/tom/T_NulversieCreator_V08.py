import os
import T_DictionaryCreator
import shutil
import T_LogCreator
import T_MovExporter
import filecmp



from T_DictionaryCreator import *


## Projectkeuze ## 

def PipelineDev():
    project = "PipelineDev"
    resolution = "/1920x1080/"
    Null(project,resolution)
    T_LogCreator.log(project)
    T_MovExporter.Export(project)
    pass

def Eigen():
    project = "Eigen"
    resolution = "/1920x1080/"
    Null(project,resolution)
    T_LogCreator.log(project)
    T_MovExporter.Export(project)
    pass

def DarkMachine():
    project = "DarkMachine"
    resolution = "/1920x1080/"
    Null(project,resolution)
    T_LogCreator.log(project)
    T_MovExporter.Export(project)
    pass


def Kropsdam():
    project = "Kropsdam"
    resolution = "/1920x1080/"
    Null(project,resolution)
    T_LogCreator.log(project)
    T_MovExporter.Export(project)
    pass



def Infinity():
    project = "Infinity"
    resolution = "/1920x1080/"
    Null(project,resolution)
    T_LogCreator.log(project)
    T_MovExporter.Export(project)
    pass              


def Null(project,resolution):




    projectname = project
    project = project + "/"
    print project

    shotdir = {}
    shotcount = 0
    serv = "Z:/projects/"
    editorial = "editorial/"
    plates ="plates/"
    nulversie = "nulversie/"
    lastpublish ="lastpublish/"
    null = "null/"
    sequences = "sequences/"
    Comp = "Comp/"
    comp = "comp/"
    publish = "publish/"
    elements = "elements/"
    fslash = "/"


    ## projectresoluties 




    

    logname = projectname + "_Database.txt"
    logpath = serv+project+editorial+nulversie+logname

    ## Call directory to create shotlist

    CreateDictionary(project,shotdir,shotcount)
    shotcount = CreateDictionary(project,shotdir,shotcount)


    print ("")
    print ("")
    print ("")
    print ("")


    #print shotdir
    #print shotcount
     
















    ##################################################

    # Copy and rename the latest versions to null
    print ("")
    print ('Running nullversiecreator voor %s'% project)
    print ("Scanning for new versions")
    print ("")
    ##################################################




    for x in xrange(0,shotcount):
        
        ## Calculate the latest version #
        vpath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp

        
        print vpath
        ## If the folder exists do something 
        if os.path.exists(vpath) == True: 
            v = max(os.listdir(vpath))
            ## Pick the newest version
            print v
            
                #print shotdir[x][0],shotdir[x][1]        
            ## folder to look for published shots
            sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp+v+resolution
            walkdir = sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp+v+resolution
            destdir = serv+project+editorial+nulversie+null+shotdir[x][0]+fslash+shotdir[x][1]+fslash
            print sourcedir
            print destdir            


            for root, dirs, files in os.walk(walkdir, topdown=False):
                for name in files:

                    destfilename = name.replace("%s" %v , "v000")
                    destdir = destdir.replace("%s" %v , "v000")
                    ## check if there is a nullfile
                    if os.path.exists(destdir+destfilename) == False:
                        print ('No file Exists, creating file: %s' %name)
                        shutil.copy(sourcedir+name,destdir+destfilename) 
                        pass
                    
                    ## Check if the file is the same, if not, copy the newer file.
                    if filecmp.cmp(sourcedir+name,destdir+destfilename) == False:
                        print name
                        print ('File already existst, updating file: %s' %name)
                        shutil.copy(sourcedir+name,destdir+destfilename) 
                        pass


                      







            ## Compare the file to be copyied with the log 
            
               
            ## Compare sourcedir to the log ## 

            ## List all filenames 
             
                       
                        





        else:
            #print ("Shot has no publishes, Doing Nothing")
            pass


            

             
        #sourcefilename=
        #destdir=
        #destfilename=



    pass


## TestScript
project = "PipelineDev"
resolution = "/1920x1080/"
Null(project,resolution)
