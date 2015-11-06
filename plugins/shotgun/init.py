# Save this file as init.py in your nuke plug-in path as described here:
#
#   http://docs.thefoundry.co.uk/nuke/63/pythondevguide/startup.html
#

# Tell the script where the Toolkit Core API is installed.
# This is often referred to as the 'studio' location.
# Don't forget back slashes in the windows path!

SGTK_STUDIO_LOCATION_LINUX   = "/mnt/software/shotgun/studio"
SGTK_STUDIO_LOCATION_MAC     = "/mnt/software/shotgun/studio"
SGTK_STUDIO_LOCATION_WINDOWS = "z:\\Projects"

# Tell the script where the project root is located. 
# This location will be used if no .nk file is specified on the command line

SGTK_DEFAULT_WORK_AREA_LINUX   = "/mnt/Projects/the_space_between_us"
SGTK_DEFAULT_WORK_AREA_MAC     = "/mnt/Projects/the_space_between_us"
SGTK_DEFAULT_WORK_AREA_WINDOWS = "z:\\Projects\\the_space_between_us"

def init_sgtk():
    """
    Minimal setup to ensure the tk-nuke engine is up
    and running when Nuke is started outside or the
    Tank command or Shotgun context menus 
    """    
    import sys, os

    studio_map = {"linux2": SGTK_STUDIO_LOCATION_LINUX,
                  "win32":  SGTK_STUDIO_LOCATION_WINDOWS,
                  "darwin": SGTK_STUDIO_LOCATION_MAC }

    work_area_map = {"linux2": SGTK_DEFAULT_WORK_AREA_LINUX,
                     "win32":  SGTK_DEFAULT_WORK_AREA_WINDOWS,
                     "darwin": SGTK_DEFAULT_WORK_AREA_MAC }

    # make sure sgtk module can be found in the python path:
    core_python_path = os.path.join(studio_map[sys.platform], "install", "core", "python")
    if core_python_path not in sys.path: 
        sys.path.append(core_python_path)

    # Check that we need to start the engine:
    if "TANK_ENGINE" in os.environ:
        # tk-nuke engine is going to be set up by
        # tk-multi-launchapp so we don't need to bother
        return

    # Check that the engine isn't already running
    if "TANK_NUKE_ENGINE_MOD_PATH" in os.environ:
        # tk-nuke engine is running which will handle all 
        # engine & context management from now on
        return

    # initialize tk-nuke engine:
    try:
        # Determine the work area path that will be used to
        # create the initial context the engine will be
        # started with.  If a file path was specified on the
        # command line then this will be sys.argv[0]
        work_area_path = work_area_map[sys.platform]
        if len(sys.argv) > 0 and sys.argv[0].endswith(".nk") and os.path.exists(sys.argv[0]):
            # file path was passed through the command line
            work_area_path = sys.argv[0] 

        import sgtk
        tk = sgtk.sgtk_from_path(work_area_path)
        ctx = tk.context_from_path(work_area_path)
        sgtk.platform.start_engine("tk-nuke", tk, ctx)
    except Exception, e:
        print "Failed to start Toolkit Engine - %s" % e
        

init_sgtk()