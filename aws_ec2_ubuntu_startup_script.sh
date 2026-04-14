#!/bin/bash

# Update package list
sudo apt update -y

# Install ssh server on ubuntu
sudo apt install openssh-server
sudo systemctl start ssh -y
sudo systemctl enable --now ssh
sudo ufw allow ssh

# Install Apache
sudo apt install -y apache2

# Start Apache service
sudo systemctl start apache2

# Enable Apache to start on boot
sudo systemctl enable apache2

# Open firewall
ufw allow 'Apache'
ufw enable

# Create index.html
echo "<h1>Hello World from C-DAC, Pune</h1>" > /var/www/html/index.html