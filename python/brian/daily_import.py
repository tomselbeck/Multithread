import os

root = "/Volumes/4dejaar/Projects/the_space_between_us/sequences/CL030/"

for item in os.listdir(root):
    try:
        chdir = os.chdir(os.path.join(root,item))      
        cg_dir = os.path.join(root,item)+"/Lighting/work/images/cg/"        
       
        imagedir = os.listdir(cg_dir)

        versions = [x for x in imagedir if "v" in x]
        if len(versions) == 0:
            continue
        latest =  sorted(versions)[-1]
        read_path = os.path.join(cg_dir,latest)+"/primary/beauty/"
        file = os.listdir(read_path)[-1]
        split = file.split(".")
        lastframe = split[1]
        split[1] = r'%04d'
        seq = ".".join(split)
        
        read_file =os.path.join(read_path, seq)

        read_node = nuke.nodes.Read (file=read_file, first=1001, last=lastframe, on_error=3)
  

        print seq
        
    except Exception, e:
        print "Failed: %s" % e
        continue