#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Check if the file apps.txt exists
if [ ! -f apps.txt ]; then
    echo "apps.txt not found!"
    exit
fi

# Update the package list
apt-get update

# Read the apt_apps.txt file and install each app
while IFS= read -r app; do
    echo "Installing $app..."
    apt-get install -y "$app"

    # Check the exit status of the last command
    if [ $? -ne 0 ]; then
        echo "Error installing $app. Skipping and continuing with the next app."
    fi

done < apt_apps.txt

# Read the snap_apps.txt file and install each app
while IFS= read -r app; do
  echo "Installing $app..."
  snap install "$app"

  if [ $? -ne 0 ]; then
    echo "Error installing $app. Skipping and continuing with the next app."
  fi

done < snap_apps.txt

echo "Installation process completed!"
