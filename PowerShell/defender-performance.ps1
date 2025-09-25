# Retrieve the system's hostname
$hostname = hostname

# Define the base path for the output file, incorporating the hostname
$outputFilePath = "C:\${hostname}-Performance-Report.txt"

# Start the recording
Write-Output "Starting the recording"
& wpr.exe -start CPU -start DiskIO -start FileIO -filemode

# Display the current time
$currentTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Output "Current time: $currentTime"

# Check the status
& wpr.exe -status

# Define the countdown duration
$duration = 120

Write-Output "Starting countdown for $duration seconds"

# Start the countdown
for ($i = $duration; $i -ge 0; $i--) {
    Write-Output "Time remaining: $i seconds"
    Start-Sleep -Seconds 1
}

# Check the status
& wpr.exe -status

# Stop the recording and save the file
Write-Output "Stopping the recording"
& wpr.exe -stop C:\Defender.ETL

# Check if the ETL file exists before proceeding
if (Test-Path "C:\Defender.ETL") {
    # Generate a performance report and output to the specified file
    Get-MpPerformanceReport -Path "C:\Defender.ETL" -TopFiles 200 -TopExtensions 100 -TopProcesses 100 -TopScans 200  | Out-File $outputFilePath

    # Append the current task list with services to the file
    tasklist /svc | Out-File $outputFilePath -Append

    # Display the content of the output file in the PowerShell session
    Get-Content $outputFilePath
    Write-Output "getfile $outputFilePath"
}
else {
    Write-Host "Performance recording file not found."
}

