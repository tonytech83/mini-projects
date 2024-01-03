<##############
    Point 1
###############>

# $currentUser = $env:USERNAME
# $userName = (Get-WmiObject -Class Win32_UserAccount -Filter "Name = '$currentUser'").FullName

$userName = Read-Host -Prompt "Enter your name"
$userMobile = Read-Host -Prompt "Enter your mobile"

<##############
    Point 2
###############>

$userLocation = Read-Host -Prompt "Enter your location (for exmp: Sofia, Bulgaria)"

<##############
    Point 3
###############>

$accessHours = Read-Host -Prompt "Enter site access hours(09:00 - 17:00 Bulgaria local time)"

<##############
    Point 4
###############>

$ipAddresses = Get-NetIPAddress
$desiredIP = ($ipAddresses | Where-Object { $_.IPAddress -like "10.2*" }).IPAddress

<##############
    Point 5
###############>

$problemDesc = Read-Host -Prompt "Detailed Problem Description"

<##############
    Point 6
###############>

$isWorked = Read-Host -Prompt "Has this worked before? (Y/N)"

<##############
    Point 7
###############>

$affectedApplications = Read-Host -Prompt "Applications affected"

<##############
    Point 8
###############>

$troubleshooting = Read-Host -Prompt "Any troubleshooting steps that have already been taken (ex: reset pc or router, power)"

<##############
    Point 9
###############>

$affectedPeopleCount = Read-Host -Prompt "How many people are impacted?"

<##############
    Point 10
###############>

# Get the network adapter with the name "Ethernet"
$adapter = Get-NetAdapter -Name "Ethernet"

# Get detailed IP configuration for the selected adapter
$ipConfig = Get-NetIPConfiguration -InterfaceIndex $adapter.InterfaceIndex

# Extracting the required details
$dnsSuffix = $ipConfig.DNSSuffix
$ipv4Address = $ipConfig.IPv4Address.IPAddress
$subnetMask = $ipConfig.IPv4Address.PrefixLength
$defaultGateway = $ipConfig.IPv4DefaultGateway.NextHop

<##############
    Point 11
###############>

$destination = Read-Host -Prompt "11. Destination IP Address (server IP, URL, etc..., this will be used for test)"

<##############
    Point 12
###############>

$tracertResult = Invoke-Expression "tracert -d $destination" | Out-String


<##############
    Point 13
###############>

$pingResult = Invoke-Expression "ping.exe -n 10 $destination" | Out-String

<############################
    Word Documet creation
#############################>

# Create data to be written to a text file
$data = @"
1. Users contact information (name, number): $userName, $userMobile

2. Users location (City and State): $userLocation

3. Site Access hours user can be contacted: $accessHours

4. Asset Name or IP address: $desiredIP

5. Detailed Problem Description: $problemDesc

6. Has this worked before? (Y/N) When did it stop working?: $isWorked

7. Applications affected: $affectedApplications

8. Any troubleshooting steps that have already been taken (ex: reset pc or router, power): $troubleshooting

9. How many people are impacted?: $affectedPeopleCount

10. Source IP Address:

    Connection-specific DNS Suffix: $dnsSuffix
    IPv4 Address: $ipv4Address
    Subnet Mask Length: $subnetMask
    Default Gateway: $defaultGateway

11. Destination IP Address (server IP, URL, etc...): $destination

12. Trace route from Source IP to Destination IP:
    $tracertResult

13. Ping long from Source IP to Destination IP:
    $pingResult
"@

# The file path
$filePath = "C:\temp\MDS.txt"

# Write data to a text file
$data | Out-File -FilePath $filePath -Encoding UTF8

Write-Output "File succesfully saved at: $filePath"
