import os


name = "PR010_"
shotname = 9

createdir = 'Z:\Projects\Infinity\editorial\plates\\'


for x in xrange(1,21):
	shotname = x
	if shotname < 10:
		name = "PR010_0"
		pass
	else:
		name = "PR010_"
		pass



	dirname = createdir+ name + str(shotname) + "00"
	print dirname
	if not os.path.exists(dirname):
	    os.makedirs(dirname)
	else:
		print "folder already exists"
	
	pass




