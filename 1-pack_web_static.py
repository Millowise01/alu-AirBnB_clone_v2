#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""

from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Path to the generated archive if successful, None otherwise.
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the archive name using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        # Compress the web_static folder into the archive
        print(f"Packing web_static to {archive_path}")
        c.run(f"tar -cvzf {archive_path} web_static")

        # Check if the archive was created successfully
        if os.path.exists(archive_path):
            archive_size = os.path.getsize(archive_path)
            print(f"web_static packed: {archive_path} -> {archive_size}Bytes")
            return