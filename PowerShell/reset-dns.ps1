# Revert DNS settings to automatic for all Up Ethernet/Wi-Fi adapters
$adapters = Get-NetAdapter | Where-Object {
    $_.Status -eq "Up" -and $_.InterfaceAlias -match "Ethernet|Wi-Fi"
}

foreach ($adapter in $adapters) {
    Write-Host "Reverting DNS for $($adapter.InterfaceAlias)..."
    Set-DnsClientServerAddress -InterfaceAlias $adapter.InterfaceAlias -ResetServerAddresses -Verbose
}