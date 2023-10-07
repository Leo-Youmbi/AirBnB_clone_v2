#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
 web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local
import time


def do_pack():
    """
    Create a compressed tarball archive of the web_static/ directory.

    Returns:
        str: Path to the created tarball archive.
            If an exception occurs during the process, returns None.
    """
    time_string = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_string))
        return ("versions/web_static_{}.tgz".format(time_string))
    except:
        return None
