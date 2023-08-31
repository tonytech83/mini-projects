###
### PowerShell template profile
###

# Prediction History with list view of predictions
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows

# Find out if the current user identity is elevated (has admin rights)
$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal $identity
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# If so and the current host is a command line, then change to red color
# as warning to user that they are operating in an elevated context
# Useful shortcuts for traversing directories
function cd... { cd ..\.. }
function cd.... { cd ..\..\.. }

# Compute file hashes - useful for checking successful downloads
function md5 { Get-FileHash -Algorithm MD5 $args }
function sha1 { Get-FileHash -Algorithm SHA1 $args }
function sha256 { Get-FileHash -Algorithm SHA256 $args }

# Quick shortcut to start notepad
function n { notepad $args }

# Drive shortcuts
function HKLM: { Set-Location HKLM: }
function HKCU: { Set-Location HKCU: }
function Env: { Set-Location Env: }

# Creates drive shortcut for Work Folders, if current user account is using it
if (Test-Path "$env:USERPROFILE\Work Folders") {
        New-PSDrive -Name Work -PSProvider FileSystem -Root "$env:USERPROFILE\Work Folders" -Description "Work Folders"
        function Work: { Set-Location Work: }
}

# Set up command prompt and window title. Use UNIX-style convention for identifying
# whether user is elevated (root) or not. Window title shows current version of PowerShell
# and appends [ADMIN] if appropriate for easy taskbar identification
function prompt {
        if ($isAdmin) {
                "[" + (Get-Location) + "] # "
        }
        else {
                "[" + (Get-Location) + "] $ "
        }
}

$Host.UI.RawUI.WindowTitle = "PowerShell {0}" -f $PSVersionTable.PSVersion.ToString()
if ($isAdmin) {
        $Host.UI.RawUI.WindowTitle += " [ADMIN]"
}

# Does the the rough equivalent of dir /s /b. For example, dirs *.png is dir /s /b *.png
function dirs {
        if ($args.Count -gt 0) {
                Get-ChildItem -Recurse -Include "$args" | Foreach-Object FullName
        }
        else {
                Get-ChildItem -Recurse | Foreach-Object FullName
        }
}

# Simple function to start a new elevated process. If arguments are supplied then
# a single command is started with admin rights; if not then a new admin instance
# of PowerShell is started.
function admin {
        if ($args.Count -gt 0) {
                $argList = "& '" + $args + "'"
                Start-Process "$psHome\pwsh.exe" -Verb runAs -ArgumentList $argList
        }
        else {
                Start-Process "C:\Program Files\PowerShell\7\pwsh.exe" -Verb runAs
        }
}

# Set UNIX-like aliases for the admin command, so sudo <command> will run the command
# with elevated rights.
Set-Alias -Name su -Value admin
Set-Alias -Name sudo -Value admin


# Make it easy to edit this profile once it's installed
function Edit-Profile {
        if ($host.Name -match "ise") {
                $psISE.CurrentPowerShellTab.Files.Add($profile.CurrentUserAllHosts)
        }
        else {
                notepad $profile.CurrentUserAllHosts
        }
}

# We don't need these any more; they were just temporary variables to get to $isAdmin.
# Delete them to prevent cluttering up the user profile.
Remove-Variable identity
Remove-Variable principal

# Quick shortcut to start Remoute Desktop Connection Manager
function rdcman {
        C:\Tools\RDCMan\RDCMan.exe
}

# Quick shortcut to start btop4win
function htop {
        C:\Tools\btop4win\btop4win.exe
}

function disk_clean {
        #Remove the temp files in AppData\Local\Temp
        Remove-Item -Path $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue

        #Disk Clean up Tool
        cleanmgr /sagerun:1 /VeryLowDisk /AUTOCLEAN | Out-Null
}
function net_cls {
        ipconfig /release & ipconfig /renew & ipconfig /flushdns
}
# Get local network settings and external IP address
function myip {
        $ip = (Get-WmiObject Win32_NetworkAdapterConfiguration).IPAddress
        $mask = (Get-WmiObject Win32_NetworkAdapterConfiguration).IPSubnet
        $gateway = (Get-WmiObject Win32_NetworkAdapterConfiguration).DefaultIPGateway
        $dns = (Get-WmiObject Win32_NetworkAdapterConfiguration).DNSServerSearchOrder
        $domain = (Get-WmiObject Win32_NetworkAdapterConfiguration).DNSDomain
        $pub_ip = (Invoke-WebRequest -uri "http://ifconfig.me/ip").Content

        if ($ip) {
                Write-Host
                Write-Host "Local:" -ForegroundColor DarkCyan
                Write-Host "IPv4 Address:         "$ip
                Write-Host "IPv4 Subnet Mask:     "$mask
                Write-Host "IPv4 Default Gateway: "$gateway
                Write-Host "IPv4 DNS Server:      "$dns
                Write-Host "Domain:               "$domain
                Write-Host
                Write-Host "External:" -ForegroundColor red
                Write-Host "IPv4 Address:         "$pub_ip
                Write-Host
        }
}
# Help function - gives a breaf description on some of the functions
function help_ {
        $commands = @{
                "admin"         = "- Simple function to start a new elevated process. If arguments are supplied then
a single command is started with admin rights; if not then a new admin instance
of PowerShell is started."
                "df"            = "- Get information about all volumes on device"
                "disk_clean"    = "- Remove the temp files in AppData\Local\Temp"
                "htop"          = "- Quick shortcut to start btop4win"
                "ll"            = "- List only files under current directory"
                "ls"            = "- List all files and directories under current directory"
                "myip"          = "- Get local network settings and external IP address"
                "net_cls"       = "- Total reset all network settings for current Ethernet adapter"
                "pgrep"         = "- Get information for process / pgrep brave /"
                "pkill"         = "- Kill proccess by name / pkill brave /"
                "reload-profile"= "- Reload PowerShell prifile"
                "rdcman"        = "- Quick shortcut to start Remoute Desktop Connection Manager"
                "touch"         = "- Creates new file / touch example.txt /"
                "uptime"        = "- Get device uptime"
        }

        $sortedCommands = $commands.Keys | Sort-Object
        Write-Host

        foreach ($command in $sortedCommands) {
                $underlineCount = 74 - $command.Length
                $underline = "_" * $underlineCount

                Write-Host "_____" -NoNewline
                Write-Host " $command " -ForegroundColor Red -NoNewline
                Write-Host $underline
                Write-Host $commands[$command]
                Write-Host
        }

}


function ll { Get-ChildItem -Path $pwd -File }
function g { cd $HOME\Documents\Github }
function gcom {
        git add .
        git commit -m "$args"
}
function lazyg {
        git add .
        git commit -m "$args"
        git push
}
function uptime {
        $currentdate = Get-Date
        $bootuptime = (Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime
        $uptime = $CurrentDate - $bootuptime
        Write-Host
        Write-Host "Device uptime:" -ForegroundColor DarkCyan
        Write-Host $($uptime.days)"days" $($uptime.Hours)"hours" $($uptime.Minutes)"minutes"
        Write-Host
}
function reload-profile {
        & $profile
}
function find-file($name) {
        ls -recurse -filter "*${name}*" -ErrorAction SilentlyContinue | foreach {
                $place_path = $_.directory
                echo "${place_path}\${_}"
        }
}
function unzip ($file) {
        echo("Extracting", $file, "to", $pwd)
        $fullFile = Get-ChildItem -Path $pwd -Filter .\cove.zip | ForEach-Object { $_.FullName }
        Expand-Archive -Path $fullFile -DestinationPath $pwd
}
function grep($regex, $dir) {
        if ( $dir ) {
                ls $dir | select-string $regex
                return
        }
        $input | select-string $regex
}
function touch($file) {
        "" | Out-File $file -Encoding ASCII
}
function df {
        get-volume
}
function sed($file, $find, $replace) {
        (Get-Content $file).replace("$find", $replace) | Set-Content $file
}
function which($name) {
        Get-Command $name | Select-Object -ExpandProperty Definition
}
function export($name, $value) {
        set-item -force -path "env:$name" -value $value;
}
function pkill($name) {
        ps $name -ErrorAction SilentlyContinue | kill
}
function pgrep($name) {
        ps $name
}


## Final Line to set prompt
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\capr4n.omp.json" | Invoke-Expression
# oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\space.omp.json" | Invoke-Expression
# oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\slimfat.omp.json" | Invoke-Expression
# oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\rudolfs-dark.omp.json" | Invoke-Expression


# Add icons
Import-Module -Name Terminal-Icons
