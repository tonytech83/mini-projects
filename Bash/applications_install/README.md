# 1. Debian application install script.

### 1. Create a text file named **apt_apps.txt** and list all the applications you want to install via **APT**, one per line. For example:

```plain
vim
curl
git
firefox
```

### 2. Create a text file named **snap_apps.txt** and list all the applications you want to install via **SNAP**, one per line. For example:
```plain
core
pycharm-community --classic
code --classic
obsidian --classic
postman
brave
```
### 3. Download script named **apps_install.sh**
```bash
wget https://raw.githubusercontent.com/tonytech83/mini-projects/main/bash_scripts/applications_install/apps_install.sh
```
### 4. Make the script executable:

```bash
chmod +x apps_install.sh
```
### 5. Run the script as root:
```bash
sudo ./apps_isntall.sh
```
The script will read the list of applications from apps.txt and install them one by one. Make sure to run the script with root privileges since package installation requires administrative rights.