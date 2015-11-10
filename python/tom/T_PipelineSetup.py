import os 
import nuke





def setup(project):

	


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
	null = "null//"
	sequences = "sequences/"
	Comp = "Comp/"
	comp = "comp/"
	publish = "publish/"
	elements = "elements/"
	fslash = "/"
	resolution = "/1920x1080/"






	BasePath = serv+project+editorial+nulversie

	## Create list of paths to create

	CreatePath = []

	CreatePath.append(BasePath+"exports/shots")
	CreatePath.append(BasePath+"exports/sequence")
	CreatePath.append(BasePath+"null")

	CreatePath.append(serv+project+editorial+"conform/nukestudio")
	CreatePath.append(serv+project+editorial+"conform/edl/extern")
	CreatePath.append(serv+project+editorial+"conform/edl/intern")

	##  Create Folders 
	print ("")
	print ("Running PipelineSetup")
	print ("Creating Folders")

	for path in CreatePath:
	    
	    if not os.path.exists(path):
	    	print ('Creating folder %s'% path)	
	        os.makedirs(path)
	        pass
	    if os.path.exists(path):
	    	print ('%s : Path already exists, doing nothing!' %path)





	pass






project = "PipelineDev"
setup (project)