#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create folders and set ownership
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data

# Create symbolic link
sudo ln -sfn /data/web_static/releases/test /data/web_static/current

# Create fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
