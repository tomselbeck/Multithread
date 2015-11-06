import os
import sys
import argparse

def maya_bind_rig(anm_file):
    """
    launches maya in standalone mode and maps the
    highres rig onto the published animation
    """
   
    sys.path.append(r'C:/Program Files/Autodesk/Maya2015/Python/Lib/site-packages')
    sys.path.append(r'C:/Program Files/Autodesk/Maya2015/bin')
    sys.path.append(r'C:/solidangle/mtoadeploy/2015/scripts')
    os.environ['PYTHONPATH'] = r'C:/Program Files/Autodesk/Maya2015/bin'
    sys.path.append("Z:/Projects/the_space_between_us/dev/maya/")

    try:
        import maya.standalone
    except Exception, e:
        return e
    
    maya.standalone.initialize()    
    import maya.cmds as cmds
    import maya.mel as mel
    
    os.environ['MTOA_PATH'] = r'C:/solidangle/mtoadeploy/2015/'
    os.environ['ARNOLD_PLUGIN_PATH'] = r'C:/solidangle/plugins/alShaders/bin;C:/solidangle/mtoadeploy/2015/shaders;C:/solidangle/mtoadeploy/2015/shaders;C:/solidangle/mtoadeploy/2015/shaders'
    os.environ['MTOA_EXTENSIONS_PATH'] = r'C:/solidangle/mtoadeploy/2015/extensions;C:/solidangle/mtoadeploy/2015/extensions;C:/solidangle/mtoadeploy/2015/extensions'
    os.environ['MAYA_SCRIPT_PATH'] = os.environ['MAYA_SCRIPT_PATH'] + ";Z:/Projects/the_space_between_us/dev/maya/"
    os.environ['MAYA_SCRIPT_PATH'] += ";R:/submission/Maya/Client/"
    os.environ['MAYA_PLUG_IN_PATH'] += ";Z:/Projects/the_space_between_us/dev/maya/plugins"
    os.environ['solidangle_LICENSE'] = "5053@145.120.28.80"

   
    cmds.evalDeferred("cmds.loadPlugin('mtoa')")
    cmds.evalDeferred("cmds.loadPlugin('AbcExport')")
    cmds.evalDeferred("cmds.loadPlugin('AbcImport')")
    cmds.file(anm_file, open=1, force=True)

    # NOW WE ARE INITIALIZED AND CAN START BINDING THE RIG

    anm_joints = cmds.ls("Adam_Rig_publish_:*JNT", typ="joint")
    if anm_joints == []:
        anm_joints = cmds.ls("*:Adam_Rig_publish_:*JNT", typ="joint")
    if anm_joints == []:
        anm_joints = cmds.ls("*JNT", typ="joint", r=1)

    cmds.file(r"Z:\Projects\the_space_between_us\assets\Character\Adam\Rig\publish\maya\selection\Adam_bind_Rig_v031.ma", i=1, ns="bindRig")

    #anm_joints = cmds.ls("Adam_Rig_publish_:*JNT", typ="joint")
    #anm_ctrls = cmds.ls("Adam_Rig_publish_:*CTRL", tr=1)
    anm_ctrls = cmds.ls("*CTRL", tr=1, r=1)
    bind_joints = cmds.ls("bindRig:*JNT", typ="joint")
    anm_head = cmds.ls("adam_bshpFace_GEO", r=1)[0]
    #begin_frame = cmds.playbackOptions(q=1, min=1)
    begin_frame = 1001
    end_frame = int(cmds.playbackOptions(q=1, max=1)) + 50



    rootdir = cmds.file(q=1, loc=1)
    #rootdir = r"Z:\Projects\the_space_between_us\sequences\CL030\CL030_040\Anm\publish\maya\selection\CL030_040_Anm_v018.ma".replace("\\", "/")
    abc_dir = "/".join(rootdir.split("/")[:-3])+"/elements/cg/"
    abc_file = abc_dir + "%s_head_Anm.abc" % rootdir.split("/")[-1][0:9]

    try:
        anm_ref_file = cmds.referenceQuery(cmds.ls("*adam_rig_GRP", r=1), f=1)
        cmds.file(anm_ref_file, ir=1)
    except:
        pass
    cmds.currentTime(1001)
    cmds.setKeyframe(anm_ctrls)

    blend_source = anm_head
    blend_target = "bindRig:bshpMe_Face_GEO"
    blend_node = cmds.blendShape(blend_source, blend_target, bf=1, name="shot_anim_bldsh")[0]
    cmds.setAttr(blend_node+".adam_bshpFace_GEO", 1)


    cmds.currentTime(950)
    cmds.autoKeyframe(state=0)

    for ctrl in anm_ctrls:
        cmds.xform(ctrl, t=(0,0,0), ro=(0,0,0), os=1)
        
    cmds.setKeyframe(anm_ctrls)

    for jnt in anm_joints:
        name = jnt.split(":")[-1]
        source = jnt
        target = [x for x in bind_joints if  name in x]
        if target == []:
            #print "failed to bind %s" % source
            continue

        
        #print source, target
        try:
            cmds.parentConstraint(source, target[0], mo=1)
        except Exception,e:
            print "failed to bind %s" % source
            
    body_geo = "bindRig:skin_body_01_GES"
    teeth = cmds.ls("teeth*GEO", r=1)
    eyes_list = cmds.ls("eye*GES", r=1)
    eyes = " -root ".join(eyes_list)
    eyes = "bindRig:eyes_01_GRP"
    locators = "bindRig:lighting_loc_GRP"



    alembics = [x for x in os.listdir(abc_dir) if x.endswith(".abc")]
    for item in alembics:
        os.chdir(abc_dir)
        try:
            os.rename(item, item.replace('Anm', 'Anm_bug'))
        except Exception as e:
            print e
    end_frame = int(end_frame)+50
    try:
        mel.eval('AbcExport -j "-root %s -root %s -root %s -root %s -root %s -uvWrite -ws -wfg -ef -s 1.0 -stripNamespaces -fr %s %s -file %s";' % (body_geo, teeth[0], teeth[1], eyes, locators,begin_frame, end_frame, abc_file.replace("head", "full")))
    except:
        mel.eval('AbcExport -j "-root %s -root %s -root %s -root %s -root %s -uvWrite -ws -wfg -ef -s 1.0 -stripNamespaces -fr %s %s -file %s";' % (body_geo, teeth[0], teeth[1], eyes, locators,begin_frame, end_frame, abc_file.replace("head", "full").replace("elements", "publish/elements")))
    #cmds.file(rn="D:\debug.ma")
    #cmds.file(s=1)

    print abc_file.replace("head", "full")

    #############################################
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get the latest publishes of the specified type")
    parser.add_argument("path", help="Patht to the file to bind")


    args = parser.parse_args()

    maya_bind_rig(args.path)





