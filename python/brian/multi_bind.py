import multiprocessing
from get_publish import get_publish
from bind_rig import maya_bind_rig
import sys, os
import argparse


sys.path.append(r"C:\Program Files\Autodesk\Maya2015\bin")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get the latest publishes of the specified type")
    parser.add_argument("sequence",  help="the sequence name")
    parser.add_argument("step", help="the pipeline step name name; for example 'anm' or 'lighting'")
    parser.add_argument("--offset", metavar="-o", type=int, default = 0,
                        help="offset the version number to fetch by this value. "
                             "offset of 1 gets the second to last publish.")

    args = parser.parse_args()

    publish_list = get_publish(args.sequence, args.step, args.offset)
    multiprocessing.set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))
    multiprocessing.set_executable('C:\\Program Files\\Autodesk\\Maya2015\\bin\\mayapy.exe')
    p = multiprocessing.Pool(processes=1, maxtasksperchild=1)

    sort_list = sorted(publish_list)
    print sort_list
    
    for item in sort_list:
        
        try:
            p.apply(maya_bind_rig, [item,])
            #maya_bind_rig(item)
            
        except Exception as e:
            print "\n FAILED: ",e, "\n", "\n"
            
        finally:
            p.close()
            p.join()
    # try:
        # p.map_async(maya_bind_rig, publish_list)
    # except:
        # pass
    # finally:
        # p.close()
        # p.join()


