#!/usr/bin/python3
from fabric.api import run, put, env
import os

env.hosts = ['54.196.180.228', '23.22.186.247']  # Replace with your web servers IPs

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to /tmp/ directory
    try:
        put(archive_path, '/tmp/')
    except Exception as e:
        print(f"Failed to upload archive: {e}")
        return False

    # Extract the file name (without extension) from the archive
    archive_name = os.path.basename(archive_path)
    folder_name = archive_name.split('.')[0]

    # Create the release folder
    try:
        run(f'mkdir -p /data/web_static/releases/{folder_name}/')
    except Exception as e:
        print(f"Failed to create release folder: {e}")
        return False

    # Uncompress the archive
    try:
        run(f'tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{folder_name}/')
    except Exception as e:
        print(f"Failed to extract archive: {e}")
        return False

    # Remove the archive from the server
    try:
        run(f'rm /tmp/{archive_name}')
    except Exception as e:
        print(f"Failed to remove the archive: {e}")
        return False

    # Move the content from web_static to the release folder
    try:
        run(f'mv /data/web_static/releases/{folder_name}/web_static/* /data/web_static/releases/{folder_name}/')
    except Exception as e:
        print(f"Failed to move content: {e}")
        return False

    # Remove the empty web_static directory
    try:
        run(f'rm -rf /data/web_static/releases/{folder_name}/web_static')
    except Exception as e:
        print(f"Failed to remove empty web_static directory: {e}")
        return False

    # Delete the current symbolic link
    try:
        run(f'rm -rf /data/web_static/current')
    except Exception as e:
        print(f"Failed to remove current symbolic link: {e}")
        return False

    # Create a new symbolic link pointing to the release folder
    try:
        run(f'ln -s /data/web_static/releases/{folder_name}/ /data/web_static/current')
    except Exception as e:
        print(f"Failed to create symbolic link: {e}")
        return False

    print("New version deployed!")
    return True
