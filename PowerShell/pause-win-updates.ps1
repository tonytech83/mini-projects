# Pause Windows Updates for ~30 days (Quality + Feature)
# Simple, PDQ-safe: registry only, no prompts, no external modules.

$ErrorActionPreference = 'Stop'
$uxPath = 'HKLM:\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings'
$nowIso = (Get-Date).ToString('o')

Write-Output "[PauseWU] Creating/ensuring $uxPath ..."
New-Item -Path $uxPath -Force | Out-Null

Write-Output "[PauseWU] Applying pause flags..."
# Quality (Cumulative) updates
Set-ItemProperty -Path $uxPath -Name 'PauseQualityUpdates' -Type DWord -Value 1
Set-ItemProperty -Path $uxPath -Name 'PauseQualityUpdatesStartTime' -Type String -Value $nowIso
# Feature updates
Set-ItemProperty -Path $uxPath -Name 'PauseFeatureUpdates' -Type DWord -Value 1
Set-ItemProperty -Path $uxPath -Name 'PauseFeatureUpdatesStartTime' -Type String -Value $nowIso

# Verify & echo current state
$vals = Get-ItemProperty -Path $uxPath -ErrorAction Stop | Select-Object `
    PauseQualityUpdates, PauseQualityUpdatesStartTime, PauseFeatureUpdates, PauseFeatureUpdatesStartTime

Write-Output "[PauseWU] Current state:"
$vals | Format-List | Out-String | ForEach-Object { $_.TrimEnd() } | Write-Output
Write-Output "[PauseWU] Done. Updates are paused for up to ~35 days by Windows. You must resume before pausing again."

exit 0