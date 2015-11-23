
import os
import T_DictionaryCreator
import shutil
#import T_LogCreator
#import T_MovExporter
import filecmp



from T_DictionaryCreator import *


## Projectkeuze ## 

def PipelineDev():
    project = "PipelineDev"
    resolution = "/1920x1080/"
    Null(project,resolution)
    #T_MovExporter.Export(project)
    pass

def Eigen():
    project = "Eigen"
    resolution = "/1920x1080/"
    Null(project,resolution)
    #T_MovExporter.Export(project)
    pass

def DarkMachine():
    project = "DarkMachine"
    resolution = "/1920x1080/"
    Null(project,resolution)

    #T_MovExporter.Export(project)
    pass


def Kropsdam():
    project = "Kropsdam"
    resolution = "/1920x1080/"
    Null(project,resolution)

    #T_MovExporter.Export(project)
    pass



def Infinity():
    project = "Infinity"
    resolution = "/1920x1080/"
    Null(project,resolution)

    #T_MovExporter.Export(project)
    pass

def Trouble():
    project = "Trouble"
    resolution = "/1920x1080/"
    Null(project,resolution)

    #T_MovExporter.Export(project)
    pass     

def Null(project,resolution):



    if project == "Infinity":
        Comp = "Concept/"
        comp = "prev/"
        pass
    else:
        Comp = "Comp/"
        comp = "comp/"
        pass


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
    extlist = ['dpx/','jpeg/']
    publish = "publish/"
    elements = "elements/"
    fslash = "/"


    ## projectresoluties 

    print shotdir


    

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
       
        ## Detect Task veriabel 01

        if os.path.exists(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash):
            temp = os.listdir(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash)
            for item in temp:
                #print item
                if item == Comp:                  
                    Comp = item + fslash


                #print "TEST"
            
            
            pass

        # ## Detect Publish type veriabel 01
        # print serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements
        # if os.path.exists(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements):
        #     temp = os.listdir(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements)
        #     print temp
        #     for item in temp:
        #         print item
        #         #if item == Comp:                  
        #         #    Comp = item + fslash


        #         #print "TEST"
            
        #     #print Comp
        #     pass    


        ## Change the elementtest variabel 

        if os.path.exists(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements):
            elementtest = os.listdir(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements)
            if not elementtest:
               
                elementtest = "EMPTY"
                print 'cant find elementtest, result:' + elementtest
            else:
                
                elementtest = str(elementtest[0])
                print elementtest
                print 'Found an element!:' + elementtest
            pass
       
        


        print serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash
        ## Calculate the latest version #
        if os.path.exists(serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash):
            vpath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash
            #print vpath
            pass
        else:
            vpath = "EMPTY"
        
        
        ## If the folder exists do something 

        
        if os.path.exists(vpath) == True: 
            v = max(os.listdir(vpath))
            vtest = v
            v = v + fslash
            ## Pick the newest version
            print v

            ## for boyth JPEG and DPX ##
            for item in extlist:
                ext = item
                print 'checking for ' + ext
                print ""


                ## Change the resolution variable 

                ## Detect the resolution ##
                resolutionTestPath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash+v+ext
                if os.path.exists(resolutionTestPath):
                    resolution = os.listdir(resolutionTestPath)

                    resolution = str(resolution[0]) + fslash







                            #print shotdir[x][0],shotdir[x][1]        
                        ## folder to look for published shots


                    sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash+v+ext+resolution
                    # walkdir = sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+elementtest+fslash+ext+resolution
                    walkdir = sourcedir
                    destdir = serv+project+editorial+nulversie+null+ext+shotdir[x][0]+fslash+shotdir[x][1]+fslash
                    print ""
                    print 'sourcedir:'+sourcedir
                    print 'destdir:'+ destdir            
                    print ""

                    for root, dirs, files in os.walk(walkdir, topdown=False):
                        for name in files:
                            
                            if not os.path.exists(destdir):
                                os.makedirs(destdir)
                                print 'destdir does not exist, creating destination folder'
                            ## Create the new file name for the nullversion file

                            ## Change the extension
                            if ext == 'jpeg/':
                                destfilename = shotdir[x][1] + name[(len(name)-10):len(name)]
                                pass
                            if ext == 'dpx/':
                                destfilename = shotdir[x][1] + name[(len(name)-9):len(name)]
                                pass
                            destfilename = destfilename.replace("_","")
                            #destfilename = name.replace("%s" %vtest , "v000")
                            destdir = destdir.replace("%s" %vtest , "v000")
                            ## check if there is a nullfile
                            print 'Checking frame :' + name
                            
                            if os.path.exists(destdir+destfilename) == False:
                                print ('No file Exists, creating file: %s' %destfilename)
                                
                                shutil.copy(sourcedir+name,destdir+destfilename) 
                                pass
                            else:
                                ## Check if the file is the same, if not, copy the newer file.


                                if filecmp.cmp(sourcedir+name,destdir+destfilename) == False:
                                    print ('File already existst, updating file: %s' %destfilename)
                                    
                                    shutil.copy(sourcedir+name,destdir+destfilename) 
                                    pass
                                else:
                                    print 'Frame is synced'
                                    print destfilename
                            print ""

                pass
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


# #TestScript
# project = "PipelineDev"
# resolution = "/1920x1080/"
# Null(project,resolution)

###########
#Autorun
##########
Infinity()
Eigen()
PipelineDev()
#DarkMachine()
#Mechanic()
#Kropsdam()
#Trouble()