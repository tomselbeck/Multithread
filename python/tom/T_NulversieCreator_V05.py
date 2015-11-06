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
lastpublish ="lastpublish/"
null = "null//"
sequences = "sequences/"
Comp = "Comp/"
comp = "comp/"
publish = "publish/"
elements = "elements/"
fslash = "/"
resolution = "/1920x1080/"

## Call directory to create shotlist




print ("")
print ("")
print ("")
print ("")


#print shotdir
#print shotcount
 












##################################################
CreateDictionary(project,shotdir,shotcount)
shotcount = CreateDictionary(project,shotdir,shotcount)

# Copy and rename the latest versions to null



##################################################




for x in xrange(0,shotcount):
    
    ## Calculate the latest version #
    vpath = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp
    if os.path.exists(vpath) == True: 
        v = max(os.listdir(vpath))
        print v
            #print shotdir[x][0],shotdir[x][1]        
    ## folder to look for published shots
        sourcedir = serv+project+sequences+shotdir[x][0]+fslash+shotdir[x][1]+fslash+Comp+publish+elements+comp+v+resolution
        destdir = serv+project+editorial+nulversie+null+shotdir[x][0]+fslash+shotdir[x][1]+fslash
        #print (sourcedir)
        


        ## List all filenames 
        for dirName, subdirList, fileList in os.walk(sourcedir):
            print('Found directory: %s' % dirName)
            sw = True;
            
            for fname in fileList:
                sourcefilename =('%s' % fname)   


                
                ## Create new filepaths and replace version numbers to 0's
                destfilename = sourcefilename.replace("%s" %v , "v000")
                destdir = destdir.replace("%s" %v , "v000")
                
                
                
                ## Create folders       
                if os.path.exists(destdir) == False:
                    print ("Destination folder does not yet exist, Creating folder: %s" %destdir)
                    os.makedirs (destdir)
                
                else:

                    
                
                    ## Copy file warning
                    if sw == True:
                        print ("Copying files from %s" %sourcedir, "to %s" %destdir) 
                        sw=False   
                        shutil.copy(sourcedir+sourcefilename,destdir+destfilename) 






    else:
        print ("Shot has no publishes, Doing Nothing")

pass







        

         
    #sourcefilename=
    #destdir=
    #destfilename=


    

