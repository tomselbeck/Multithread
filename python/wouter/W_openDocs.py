import os
import sys
import nuke

def openDocs():

    try:
        import subprocess
        def _run(cmd, shell, wait):
            opener = subprocess.Popen(cmd, shell=shell)
            if wait:
                opener.wait()
            return opener.pid
    except ImportError:
        import popen2
        def _run(cmd, shell, wait):
            opener = popen2.Popen3(cmd)
            if wait:
                opener.wait()
            return opener.pid

    def _open(url, wait=0):
        if sys.platform == "darwin":
            cmd = ["open", url]
        elif hasattr(os, "startfile"):
            return os.startfile(url)
        elif os.environ.has_key("KDE_FULL_SESSION") or os.environ.has_key("KDE_MULTIHEAD") or \
            os.environ.has_key("GNOME_DESKTOP_SESSION_ID") or os.environ.has_key("GNOME_KEYRING_SOCKET"):
            cmd = ["xdg-open", url]
        else:
            raise OSError, "Desktop not supported."

        return _run(cmd, 0, wait)

    _open('https://145.102.112.133/index.php/Nuke')
    
nuke.menu("Nuke").addCommand("Help/NFA Documentation", openDocs )