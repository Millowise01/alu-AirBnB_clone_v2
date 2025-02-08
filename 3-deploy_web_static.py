#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric import task
from fabric.connection import Connection
from datetime import datetime
import os

# Define your web server IPs
HOSTS = ['142.44.167.228', '144.217.246.195']
USER = "ubuntu"


def do_pack():
    """Generates a tgz archive of the web_static folder."""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        os.makedirs("versions", exist_ok=True)  # Ensure directory exists
        file_name = "versions/web_static_{}.tgz".format(date)
        os.system("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(c, archive_path):
    """Distributes an archive to a web server."""
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = os.path.basename(archive_path)
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        # Upload the archive
        c.put(archive_path, "/tmp/")
        
        # Create the directory & extract files
        c.run(f"mkdir -p {path}{no_ext}/")
        c.run(f"tar -xzf /tmp/{file_n} -C {path}{no_ext}/")
        
        # Clean up
        c.run(f"rm /tmp/{file_n}")
        c.run(f"mv {path}{no_ext}/web_static/* {path}{no_ext}/")
        c.run(f"rm -rf {path}{no_ext}/web_static")
        c.run("rm -rf /data/web_static/current")
        c.run(f"ln -s {path}{no_ext}/ /data/web_static/current")
        
        return True
    except Exception:
        return False


@task
def deploy(c):
    """Creates and distributes an archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False

    success = True
    for host in HOSTS:
        conn = Connection(host=host, user=USER, connect_kwargs={"key_filename": c.config["key_filename"]})
        if not do_deploy(conn, archive_path):
            success = False
    return success
