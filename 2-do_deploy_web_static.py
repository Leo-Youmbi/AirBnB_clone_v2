#!/usr/bin/python3
""" Script that distributes an archive to your web servers using do_deploy"""

from fabric.api import env, local
from fabric.operations import run, put, sudo
import os.path
env.hosts = ['54.210.90.11', '52.87.219.193']


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
    except:
        return False
