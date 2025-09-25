Write-Host "Reverting pending DISM operations..."
Dism.exe /Online /Cleanup-Image /RevertPendingActions

Write-Host "Starting component cleanup with ResetBase..."
Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase

Write-Host "Running built-in StartComponentCleanup task (fallback)..."
schtasks.exe /Run /TN "\Microsoft\Windows\Servicing\StartComponentCleanup"

Write-Host "Running cleanmgr on C:..."
cleanmgr.exe /d C: /VERYLOWDISK