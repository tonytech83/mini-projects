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

# Read the apps.txt file and install each app
while IFS= read -r app; do
    echo "Installing $app..."
    apt-get install -y "$app"

    # Check the exit status of the last command
    if [ $? -ne 0 ]; then
        echo "Error installing $app. Skipping and continuing with the next app."
    fi

done < apps.txt

# Install PyCharm
snap install core
snap install pycharm-community --classic

echo "Installation process completed!"
