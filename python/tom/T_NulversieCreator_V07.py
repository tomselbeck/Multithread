import os
import T_DictionaryCreator
import shutil
import T_LogCreator

from T_DictionaryCreator import *


## Projectkeuze ## 

def PipelineDev():

    project = "PipelineDev/"
    Null(project)
    pass


## Uitvoering ##  


def Null(project):







    shotdir = {}
    shotcount = 0
    serv = "Z:/projects/"
    editorial = "editorial/"
    plates ="plates/"
    nulversie = "nulversie/"
    lastpublish ="lastpublish/"
    null = "null//"
    sequences = "sequences/"
    Comp = "Comp/"
    comp = "comp/"
    publish = "publish/"
    elements = "elements/"
    fslash = "/"
    resolution = "/1920x1080/"

    logname = project[0:len(project)-1] + "_Database.txt"
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
        if os.path.exists(vpath) == True: 
            v = max(os.listdir(vpath))
            
                #print shotdir[x][0],shotdir[x][1]        
        ## folder to look for published shots
            sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp+v+resolution
            destdir = serv+project+editorial+nulversie+null+shotdir[x][0]+fslash+shotdir[x][1]+fslash
            #print (sourcedir)
            


            ## List all filenames 
            for dirName, subdirList, fileList in os.walk(sourcedir):
                print('Found directory: %s' % dirName)
                
                
                for fname in fileList:
                    sourcefilename =('%s' % fname)   


                    
                    ## Create new filepaths and replace version numbers to 0's
                    destfilename = sourcefilename.replace("%s" %v , "v000")
                    destdir = destdir.replace("%s" %v , "v000")
                    
                    
                    
                    ## Create folders       
                    if os.path.exists(destdir) == False:
                        print ("Destination folder does not yet exist, Creating folder: %s" %destdir)
                        os.makedirs (destdir)
                    
                    ## Copying Files:
                    
                    ## check the log if there has been an existing version
                    log = open(logpath, "r");
                    logread=log.read().splitlines()
                    #print logread
                    #sourcefilename = "'"+sourcefilename + "'"
                    #print logread
                    if not sourcefilename in logread:
                        print sourcefilename
                        print ("Log says we have a new version,")
                        print ("Copying files from %s" %sourcedir, "to %s" %destdir)
                        #shutil.copy(sourcedir+sourcefilename,destdir+destfilename) 
                    #if logread == sourcefilename:
                    #    print ("It equals!")
                    #    pass
                    #shutil.copy(sourcedir+sourcefilename,destdir+destfilename)  
                       
                        





        else:
            #print ("Shot has no publishes, Doing Nothing")
            pass


            

             
        #sourcefilename=
        #destdir=
        #destfilename=

    ## Update the logs 
    print ("")
    T_LogCreator.log(project)

    pass


#PipelineDev()
