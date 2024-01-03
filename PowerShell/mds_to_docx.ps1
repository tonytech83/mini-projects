###############
### Point 1 ###
###############

$currentUser = $env:USERNAME
$userName = (Get-WmiObject -Class Win32_UserAccount -Filter "Name = '$currentUser'").FullName

# $userName = Read-Host -Prompt "Enter your name"
$userMobile = Read-Host -Prompt "Enter your mobile"

### Point 2

$userLocation = Read-Host -Prompt "Enter your location (for exmp: Sofia, Bulgaria)"

### Point 3

$accessHours = Read-Host -Prompt "Enter site access hours(09:00 - 17:00 Bulgaria local time)"

### Point 4

$ipAddresses = Get-NetIPAddress
$desiredIP = ($ipAddresses | Where-Object { $_.IPAddress -like "10.2*" }).IPAddress

### Point 5

$problemDesc = Read-Host -Prompt "Detailed Problem Description"

### Point 6

$isWorked = Read-Host -Prompt "Has this worked before? (Y/N)"

### Point 7

$affectedApplications = Read-Host -Prompt "Applications affected"

### Point 8

$troubleshooting = Read-Host -Prompt "Any troubleshooting steps that have already been taken (ex: reset pc or router, power)"

### Point 9

$affectedPeopleCount = Read-Host -Prompt "How many people are impacted?"

### Point 10

# Get the network adapter with the name "Ethernet"
$adapter = Get-NetAdapter -Name "Ethernet"

# Get detailed IP configuration for the selected adapter
$ipConfig = Get-NetIPConfiguration -InterfaceIndex $adapter.InterfaceIndex

# Extracting the required details
$dnsSuffix = $ipConfig.DNSSuffix
$ipv4Address = $ipConfig.IPv4Address.IPAddress
$subnetMask = $ipConfig.IPv4Address.PrefixLength
$defaultGateway = $ipConfig.IPv4DefaultGateway.NextHop

### Point 11

$destination = Read-Host -Prompt "11. Destination IP Address (server IP, URL, etc..., this will be used for test)"

### Point 12

$tracertResult = Invoke-Expression "tracert -d $destination" | Out-String


### Point 13

$pingResult = Invoke-Expression "ping.exe -n 10 $destination" | Out-String

#############################
### Word Documet creation ###
#############################

# The file path
$FilePath = "C:\temp\MDS.docx"

# Create a new instance of Microsoft Word
$Word = New-Object -ComObject Word.Application

# Make Word visible (can be set to $false to hide the Word application)
$Word.Visible = $false

# Add a new document
$Document = $Word.Documents.Add()

# Add text to the document
$textToAdd = "1. Users contact information (name, number): $userName, $userMobile" + "`n" +
"2. Users location (City and State): $userLocation" + "`n" +
"3. Site Access hours user can be contacted: $accessHours" + "`n" +
"4. Asset Name or IP address: $desiredIP" + "`n" +
"5. Detailed Problem Description: $problemDesc" + "`n" +
"6. Has this worked before? (Y/N) When did it stop working?: $isWorked" + "`n" +
"7. Applications affected: $affectedApplications" + "`n" +
"8. Any troubleshooting steps that have already been taken (ex: reset pc or router, power): $troubleshooting" + "`n" +
"9. How many people are impacted?: $affectedPeopleCount" + "`n" +
"10. Source IP Address: " + "`n" +
"`t" + "Connection-specific DNS Suffix: $dnsSuffix" + "`n" +
"`t" + "IPv4 Address: $ipv4Address" + "`n" +
"`t" + "Subnet Mask Length: $subnetMask" + "`n" +
"`t" + "Default Gateway: $defaultGateway" + "`n" +
"11. Destination IP Address (server IP, URL, etc...): $destination" + "`n" +
"12. Trace route from Source IP to Destination IP: " + "`n" +
"`t" + "$tracertResult" + "`n" +
"13. Ping long from Source IP to Destination IP: " + "`n" +
"`t" + "$pingResult" + "`n"


$Document.Content.Text = $textToAdd

# Save the document
$Document.SaveAs([ref] $FilePath)

# Close Word if you don't need it open anymore
$Word.Quit()

