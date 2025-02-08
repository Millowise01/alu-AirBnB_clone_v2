#!/usr/bin/env bash
# Sets up web servers for deploying web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update -y
    sudo apt-get install -y nginx
fi

# Create required directories
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

# Create symbolic link (force replace if exists)
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ as /hbnb_static
CONFIG_FILE="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" "$CONFIG_FILE"; then
    sudo sed -i "/server_name _;/a \\
\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$CONFIG_FILE"
fi

# Restart Nginx to apply changes
sudo service nginx restart

exit 0
