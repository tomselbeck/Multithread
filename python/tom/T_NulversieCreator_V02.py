import os
import T_DictionaryCreator
import shutil
from T_DictionaryCreator import *


shotdir = {}
shotcount = 0
project = "PipelineDev/"
serv = "Z:/projects/"
editorial = "editorial/"
plates ="plates/"
nulversie = "nulversie/"
lastpublish ="lastpublish2/"
sequences = "sequences/"
Comp = "Comp/"
comp = "comp/"
publish = "publish/"
elements = "elements/"
fslash = "/"
resolution = "/1920x1080/"

## Call directory to create shotlist

CreateDictionary(project,shotdir,shotcount)
shotcount = CreateDictionary(project,shotdir,shotcount)


print ("")
print ("")
print ("")
print ("")


#print shotdir
#print shotcount


## For every Shot
for x in xrange(0,shotcount):
    ## Create the path to look in for versions
    lookpath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp
    destpath = serv+project+editorial+nulversie+lastpublish+shotdir[x][0]+fslash+shotdir[x][1]
    print ("Checking %s" % lookpath)
    ## Skip folders with nothing in them
    i = (os.path.exists(lookpath))
    if i == True:   
        ## List the version numbers      
        v = os.listdir(lookpath)
        print ("Versions available %s" % v)
        v = max(v)
        print ("Version %s is the highest" %v )
        lookpath = lookpath + v
        destpath = destpath + fslash+ v


        #print os.listdir (lookpath)
        ## Pick the heighest numbe
        ##shutil.copytree(lookpath,destpath)    
        if os.path.exists(destpath) == True:
            print ("Folder already exists, Not copying")
            print ("")
            #shutil.rmtree(destpath)   ## Use this for overwriting everything 
        
        print ("Copying !")
        print ("copying from: %s" %lookpath)    
        print ("copying to %s" % destpath)
        ##shutil.copytree(lookpath, destpath)
        rootDir = lookpath
        ## For every file in these folders 
        for dirName, subdirList, fileList in os.walk(rootDir):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                #print v
                old = ('\%s' % fname)
                old = rootDir + resolution + old
               

                newname = fname.replace("%s" %v , "v000")

                dest = serv+project+editorial+nulversie+lastpublish+shotdir[x][0]+fslash+shotdir[x][1]+ fslash + newname
                destfolder = dest = serv+project+editorial+nulversie+lastpublish+shotdir[x][0]+fslash+shotdir[x][1]+ fslash
                dest = os.path.abspath(dest)
                old = os.path.abspath (old)


                print old
                print dest
                ## Create destionation directoryes if they are not already there
                if os.path.exists(destfolder) == False:
                    os.makedirs(destfolder)
                    print ("Creating destfolder: %s" %destfolder)
                else:
                    print ("Destfolder already exists")
                    

                #shutil.copy(old,dest)
                os.rename(old, newname)
                print ("")
                print ("")
                
                #print rootDir + "/1920*1080/"
                
                #print new

                
                #new = rootDir + resolution + new
                #new = serv+project+editorial+nulversie+lastpublish+shotdir[x][0]+fslash+shotdir[x][1] + new

                #print old
                #print new 
                ##os.rename(old, new) ## Werk verder hier..... 
        
        
        
        print ("Done Copying!")
        print ("")
    else:
        print ("Nothing published, booooring, skipping it")
        print ("")        

