# Set DNS servers for all Up Ethernet/Wi-Fi adapters (by alias)
$dnsServers = @("1.1.1.1", "8.8.8.8")

$adapters = Get-NetAdapter | Where-Object {
    $_.Status -eq "Up" -and $_.InterfaceAlias -match "Ethernet|Wi-Fi"
}

foreach ($adapter in $adapters) {
    Write-Host "Setting DNS for $($adapter.InterfaceAlias)..."
    Set-DnsClientServerAddress -InterfaceAlias $adapter.InterfaceAlias -ServerAddresses $dnsServers -Verbose
}