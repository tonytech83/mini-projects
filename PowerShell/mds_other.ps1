<#
1. Are you able to access http://ip.zscaler.com
2. Are you able to access any other website
3. If Question 1 & 2 are "No" then ,Has Internet circuit & tunnel connection been validated as operational?
4. Has any ticket been opened with Internet service provider ,Incase tunnel is not operational
5. Has authentication server been validated ?
6. When was access working last time ?
7. Output of the website which user is trying to access (Attached with MDS)
8. Which Browser you are using ?
9. Did you try to access the website from different Browser
10. Did you try to access the website from different Computer
11. Out put of http://ip.zscaler.com (Attached with the MDS)
12. what is the forwarding method used
13. if using zcc as forwarding method please provide us screenshot of app profile in zcc
#>


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

if ($websiteOneStatusCode -eq 200 && $websiteTwoStatusCode -eq 200) {
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

if ($zscalerStatus -eq "NO" && $websitesStatus -eq "NO") {
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

$currentUser = $env:USERNAME

$htmlContent = $response_1.Content

$regexSpan = '(?<=<span class="detailOutput">).*?(?=</span>)'
$regexDiv  = '(?<=<div class="headline">).*?(?=</div>)'

$spans = [regex]::Matches($htmlContent, $regexSpan) | ForEach-Object { $_.Value }
$div = [regex]::Matches($htmlContent, $regexDiv) | ForEach-Object { $_.Value}

$spanZero, $spanOne, $spanTwo, $spanThree, $spanFour = $spans


### Point 12
$forwardingMethod = Read-Host -Prompt "What is the forwarding method used (Zscaler client ???)"


### Point 13


<############################
    Word Document creation
#############################>

# Create data to be written to a text file
$data = @"
1. Are you able to access http://ip.zscaler.com: $zscalerStatus

2. Are you able to access any other website:

    $websiteOne : $websiteOneStatus
    $websiteTwo : $websiteTwoStatus

3. If Question 1 & 2 are `"No`" then ,Has Internet circuit & tunnel connection been validated as operational?: $circuit

4. Has any ticket been opened with Internet service provider ,Incase tunnel is not operational: $hasTicket

5. Has authentication server been validated ?: $hasAuthServer

6. When was access working last time ?: $lastWork

7. Output of the website which user is trying to access (Attached with MDS)

8. Which Browser you are using ? $browsers

9. Did you try to access the website from different Browser $tryOtherBrowser

10. Did you try to access the website from different Computer $tryFromOtherPC

11. Out put of http://ip.zscaler.com (Attached with the MDS):

    $div
    Your request is arriving at this server from the IP address $spanZero
    The Zscaler proxy virtual IP is $spanOne
    The Zscaler hostname for this proxy appears to be $spanTwo
    The request is being received by the Zscaler Proxy from the IP address $spanThree
    Your Gateway IP Address is $spanFour

    Your user name is: $currentUser@xxx.com

12. What is the forwarding method used $forwardingMethod

13. If using zcc as forwarding method please provide us screenshot of app profile in zcc
"@

# The file path
$filePath = "C:\temp\MDS.txt"

# Write data to a text file
$data | Out-File -FilePath $filePath -Encoding UTF8

Write-Output "File succesfully saved at: $filePath"



