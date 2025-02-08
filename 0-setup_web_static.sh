#!/usr/bin/env bash
# 0-setup_web_static.sh

# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$nginx_config"; then
    sudo sed -i '/server_name _;/a \
        location /hbnb_static/ { \
            alias /data/web_static/current/; \
        }' "$nginx_config"
fi

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0
