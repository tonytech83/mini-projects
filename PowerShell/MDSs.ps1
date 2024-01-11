
###############################################
###           Simple MDS function           ###
###############################################
function simpleMDS {
  ### Point 1
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

  # Get the network adapter with the name "Ethernet*" into list
  $adapters = (Get-NetAdapter -Name "Ethernet*")

  $upAdapter = $adapters | Where-Object {$_.Status -eq "Up"}

  # Get detailed IP configuration for the selected adapter
  $ipConfig = Get-NetIPConfiguration -InterfaceIndex  $upAdapter.InterfaceIndex

  # Extracting the required details
  $dnsSuffix = $ipConfig.NetProfile.Name
  $ipv4Address = $ipConfig.IPv4Address
  $subnetMask = $ipConfig.IPv4Address.PrefixLength
  $defaultGateway = $ipConfig.DNSServer.ServerAddresses

  ### Point 11
  $destination = Read-Host -Prompt "Destination IP Address (server IP, URL, etc..., this will be used for test)"
  Write-Output ""

  ### Point 12
  $tracertResult = Invoke-Expression "tracert -d $destination" | Out-String

  ### Point 13
  $pingResult = Invoke-Expression "ping.exe -n 10 $destination" | Out-String

  #Add text to the document
  $textToAdd = @(
    "1. Users contact information (name, number): $userName, $userMobile"

    "2. Users location (City and State): $userLocation"

    "3. Site Access hours user can be contacted: $accessHours"

    "4. Asset Name or IP address: $desiredIP"

    "5. Detailed Problem Description: $problemDesc"

    "6. Has this worked before? (Y/N) When did it stop working?: $isWorked"

    "7. Applications affected: $affectedApplications"

    "8. Any troubleshooting steps that have already been taken (ex: reset pc or router, power): $troubleshooting"

    "9. How many people are impacted?: $affectedPeopleCount"

    "10. Source IP Address: "

    "`tConnection-specific DNS Suffix: $dnsSuffix"
    "`tIPv4 Address: $ipv4Address"
    "`tSubnet Mask Length: $subnetMask"
    "`tDefault Gateway: $defaultGateway"

    "11. Destination IP Address (server IP, URL, etc...): $destination"

    "12. Trace route from Source IP to Destination IP: "
    "`t$tracertResult"

    "13. Ping long from Source IP to Destination IP: "
    "`t$pingResult"
  )

  return $textToAdd
}


###############################################
###            Other MDS function           ###
###############################################
function otherMDS {

  ### Point 1
  $response_1 = Invoke-WebRequest -Uri "http://ip.zscaler.com"
  $zscalerStatusCode = $response_1.StatusCode

  $zscalerStatus = $null

  if ($zscalerStatusCode -eq 200) {
    $zscalerStatus = "YES"
  }
  else {
    $zscalerStatus = "NO"
  }

  ### Point 2
  $websiteOne = "http://google.com"
  $websiteTwo = "http://yahoo.com"
  $response_2 = Invoke-WebRequest -Uri $websiteOne
  $response_3 = Invoke-WebRequest -Uri $websiteTwo
  $websiteOneStatusCode = $response_2.StatusCode
  $websiteTwoStatusCode = $response_3.StatusCode

  $websiteOneStatus = $null
  $websiteTwoStatus = $null
  $websitesStatus = $null

  if ($websiteOneStatusCode -eq 200 -and $websiteTwoStatusCode -eq 200) {
    $websiteOneStatus = "YES"
    $websiteTwoStatus = "YES"
    $websitesStatus = "YES"
  }
  else {
    $websiteOneStatus = "NO"
    $websiteTwoStatus = "NO"
    $websitesStatus = "NO"
  }

  ### Point 3
  $circuit = $null

  if ($zscalerStatus -eq "NO" -and $websitesStatus -eq "NO") {
    $circuit = "NO"
  }
  else {
    $circuit = "YES"
  }

  ### Point 4
  $hasTicket = Read-Host -Prompt "Has any ticket been opened with Internet service provider ,Incase tunnel is not operational"

  ### Point 5
  $hasAuthServer = Read-Host -Prompt "Has authentication server been validated ?"

  ### Point 6
  $lastWork = Read-Host -Prompt "When was access working last time"

  ### Point 7

  ### Point 8
  $browsers = Read-Host -Prompt "Which Browser you are using (Chrome, Edge, etc..)"

  ### Point 9
  $tryOtherBrowser = Read-Host -Prompt "Did you try to access the website from different Browser (Yes/No)"

  ### Point 10
  $tryFromOtherPC = Read-Host -Prompt "Did you try to access the website from different Computer (Yes/No)"

  ### Point 11
  # $currentUser = $env:USERNAME

  $htmlContent = $response_1.Content

  $regexSpan = '(?<=<span class="detailOutput">).*?(?=</span>)'
  $regexDiv = '(?<=<div class="headline">).*?(?=</div>)'

  $spans = [regex]::Matches($htmlContent, $regexSpan) | ForEach-Object { $_.Value }
  $div = [regex]::Matches($htmlContent, $regexDiv) | ForEach-Object { $_.Value }

  $spanZero, $spanOne, $spanTwo, $spanThree, $spanFour = $spans

  ### Point 12
  $forwardingMethod = Read-Host -Prompt "What is the forwarding method used (Zscaler client ???)"

  ### Point 13

  # Add text to the document
  $textToAdd = @(
    "1. Are you able to access http://ip.zscaler.com: $zscalerStatus"

    "2. Are you able to access any other website:"

    "`t$websiteOne : $websiteOneStatus"
    "`t$websiteTwo : $websiteTwoStatus"

    "3. If Question 1 & 2 are `"No`" then ,Has Internet circuit & tunnel connection been validated as operational?: $circuit"

    "4. Has any ticket been opened with Internet service provider ,Incase tunnel is not operational: $hasTicket"

    "5. Has authentication server been validated ?: $hasAuthServer"

    "6. When was access working last time ?: $lastWork"

    "7. Output of the website which user is trying to access (Attached with MDS)"

    "8. Which Browser you are using ? $browsers"

    "9. Did you try to access the website from different Browser $tryOtherBrowser"

    "10. Did you try to access the website from different Computer $tryFromOtherPC"

    "11. Output of http://ip.zscaler.com (Attached with the MDS):"

    "`t$div"
    "`tThe Zscaler proxy virtual IP is $spanOne"
    "`tThe Zscaler hostname for this proxy appears to be $spanTwo"
    "`tThe request is being received by the Zscaler Proxy from the IP address $spanThree"
    "`tYour Gateway IP Address is $spanFour"
    "`tYour user name is: $currentUser@xxx.com"

    "12. What is the forwarding method used: $forwardingMethod"

    "13. If using zcc as forwarding method please provide us screenshot of app profile in zcc"
  )

  return $textToAdd
}

# Get Timestamp
$timestamp =  Get-Date -Format "ddMMyyyy_HHmm"

# Get username
$currentUser = $env:USERNAME
$userName = (Get-WmiObject -Class Win32_UserAccount -Filter "Name = '$currentUser'").FullName

# Get hostname
$hostname = Invoke-Expression -Command 'hostname' 

Clear-Host

Write-Output "###########################################################################################"
Write-Output "###                                                                                     ###"
Write-Output "###   This is semi-automatic PowerShell script, helping you to generate AT&T MDS file   ###"
Write-Output "###                                                                                     ###"
Write-Output "###########################################################################################"
Write-Output "###                                                                                     ###"
Write-Output "###                         You can chose bewtween:                                     ###"
Write-Output "###                                                                                     ###"
Write-Output "###                         1. Simple MDS                                               ###"
Write-Output "###                         2. Other MSD                                                ###"
Write-Output "###                                                                                     ###"
Write-Output "###########################################################################################"
Write-Output ""
Write-Output "                  Some basic information about you and your system:"
Write-Output ""
Write-Output "                  -- username: $userName" 
Write-Output "                  -- hostname: $hostname"
Write-Output ""
Write-Output ">>> The generated file can be found in C:\Temp\MDS_$timestamp.txt <<<"                            


Write-Output ""
Start-Sleep -Seconds 3

$type = Read-Host -Prompt "Plese select type of MDS"

if ($type -eq 1) {
  $text = simpleMDS
}
else {
  $text = otherMDS
}

# ###############################################
# ###          Word Documet creation          ###
# ###############################################

### This code didn't work on some systems!!!

# # The file path
# $FilePath = "C:\temp\MDS_$timestamp.docx"

# # Create a new instance of Microsoft Word
# $Word = New-Object -ComObject Word.Application

# # Make Word visible (can be set to $false to hide the Word application)
# $Word.Visible = $false

# # Add a new document
# $Document = $Word.Documents.Add()


# # Join the array elements
# $text = $text -join "`n"
# $Document.Content.Text = $text

# # Save the document
# $Document.SaveAs([ref] $FilePath)

# # Close Word if you don't need it open anymore
# $Word.Quit()

###############################################
###           Text file   creation          ###
###############################################

# The file path
$filePath = "C:\temp\MDS_$timestamp.txt"

# Write data to a text file
$text | Out-File -FilePath $filePath -Encoding UTF8

Write-Output "File succesfully saved at: $filePath"