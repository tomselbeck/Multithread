
import os



def CreateDictionary(project,shotdir,shotcount):
    

    project = project + "/"
    serv = "Z:/projects/"
    #project = "PipelineDev/"
    editorial = "editorial/"
    plates ="plates/"
    nulversie = "nulversie/"
    lastpublish ="lastpublish/"
    sequences = "sequences/"
    fslash = "/"


    shotlist =[]
    #shotdir = {}
    #shotcount = 0

    #print ("")
    #print ("")
    #print ("")

    print ("Running: dictionary Creator")

    #rint ("Creating dictionary for following Path:")
    lookpath = serv + project + editorial + plates
    #print lookpath
    #print ("")
    # List the sequence folders  #
    seqs = os.listdir(lookpath)

    #print ("These sequences are present:")
    #print seqs
    #print ("")

    # list how many sequences there are 
    #print ("Number of sequences :")
    #print len(seqs)
    #print ("")

    #print ("Creating dictionary")
    #print ("")




    # for every sequence 
    for x in xrange(0,len(seqs)):
        lookpath = serv + project + editorial + plates + seqs[x] + fslash
        #print lookpath
        # List the shot folders  
        shots = os.listdir(lookpath)
        
        
        # For every shot 
        for i in xrange(0,len(shots)):
            shotlist.extend(shots)
            lookpath = lookpath = serv + project + editorial + plates + seqs [x] + fslash + shots [i]
            #print lookpath
            #print shots[i]
            # Check the shot lenth 
            length =  len(os.walk(lookpath).next()[2])
            # Add to shot dictionary
            shotdir [shotcount]  = seqs[x],shots[i],length+1000
            print shotdir[shotcount]
            shotcount = shotcount + 1

 
    #print ("")
    #print shotdir
    #print shotcount

    #print ("")
    #print ("Dictionary created! Saved it in Shotdir variable")
    return shotcount
    return shotdir     
    
    pass


##### TEST SCRIPT 
#project = "PipelineDev"
#shotdir = {}
#shotcount = 0
#CreateDictionary(project,shotdir,shotcount)

