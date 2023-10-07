#!/usr/bin/python3
""" Script that distributes an archive to your web servers using do_deploy"""
from fabric.api import *
import time
import os.path
env.hosts = ['54.210.90.11', '52.87.219.193']


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
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Deploy a compressed tarball archive to the web server.

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        nconfig = archive_path.split("/")[-1]
        ndir = ("/data/web_static/releases/" + nconfig.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(ndir))
        run("sudo tar -xzf /tmp/{} -C {}".format(nconfig, ndir))
        run("sudo rm /tmp/{}".format(nconfig))
        run("sudo mv {}/web_static/* {}/".format(ndir, ndir))
        run("sudo rm -rf {}/web_static".format(ndir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(ndir))
        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    try:
        archive_address = do_pack()
        val = do_deploy(archive_address)
        return val
    except Exception as e:
        return False
