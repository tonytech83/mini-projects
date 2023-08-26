## 1. Debian application install script.

1. Create a text file named apps.txt and list all the applications you want to install, one per line. For example:

```plain
vim
curl
git
firefox
```

2. Download script named apps_install.sh
3. Make the script executable:

```bash
chmod +x apps_install.sh
```
4. Run the script as root:
```bash
sudo ./apps_isntall.sh
```
The script will read the list of applications from apps.txt and install them one by one. Make sure to run the script with root privileges since package installation requires administrative rights.