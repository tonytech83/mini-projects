# Create or update the registry key
New-Item -Path "HKCU:\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" -Name "InprocServer32" -force -value ""
Write-Host "Restarting explorer.exe ..."
# Terminate and restart explorer
Stop-Process -Name explorer -Force
Start-Process explorer.exe
