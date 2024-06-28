#!/bin/bash

$dashes = "---------------------------------------------------------------"

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Check if the file apt_apps.txt exists
if [ ! -f apt_apps.txt ]; then
    echo "apt_apps.txt not found!"
    exit
fi

# Check if the file snap_apps.txt exists
if [ ! -f snap_apps.txt ]; then
    echo "snap_apps.txt not found!"
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

    echo $dashes

done < apt_apps.txt

# Install snapd
sudo apt install snapd -y

# Enable Snap support
sudo systemctl enable --now snapd.apparmor

# Create a symbolic link between /var/lib/snapd/snap and /snap:
sudo ln -s /var/lib/snapd/snap /snap

# Read the snap_apps.txt file and install each app
while IFS= read -r line; do
  echo "Installing $line..."
  snap install $line

  if [ $? -ne 0 ]; then
    echo "Error installing $line. Skipping and continuing with the next app."
  fi

  echo $dashes

done < snap_apps.txt

echo "Installation process completed! You can reboot your device to finished the installation."
