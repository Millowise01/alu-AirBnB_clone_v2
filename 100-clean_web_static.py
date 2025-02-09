from fabric.api import env, local, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your actual web server IPs

def do_clean(number=0):
    """Delete out-of-date archives."""
    number = int(number)
    if number < 1:
        number = 1
    
    # Local cleanup: Keep the most recent `number` of archives
    archives = sorted(os.listdir("versions"))
    archives_to_delete = archives[:-number]
    
    for archive in archives_to_delete:
        local(f"rm -rf versions/{archive}")
    
    # Remote cleanup: Keep the most recent `number` of archives in `/data/web_static/releases/`
    for host in env.hosts:
        run("ls -t /data/web_static/releases | grep web_static_ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
