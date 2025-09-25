$printerName = "Lexmark CX825 | SC"
$printerIP = "192.168.88.88"
$driverName = "Lexmark CX825 Series XL"
$portName = "IP_$printerIP"
$driverFolder = "C:\TEMP\lexmark-drv"
$infFile = "$driverFolder\LMU02p40.inf"

Write-Output "=============================================================="
Write-Output "=                                                            ="
Write-Output "=                 Install Lexmark CX825 | SC                  ="
Write-Output "=                                                            ="
Write-Output "=============================================================="

Write-Output ""
Write-Output ">> INF file =================================================="

if (-not (Test-Path -LiteralPath $infFile)) {
    Write-Error "INF file not found: $infFile"
    exit 1
}
else {
    Write-Output "INF file found, installation can proceed..."
}

# Create the TCP/IP printer port if it doesn't exist
Write-Output ""       
Write-Output ">> TCP/IP printer port ======================================="
if (-not (Get-PrinterPort -Name $portName -ErrorAction SilentlyContinue)) {
    try {
        Add-PrinterPort -Name $portName -PrinterHostAddress $printerIP -ErrorAction Stop
        Write-Output "TCP/IP printer port was created successfully..."
    }
    catch {
        Write-Error "Add-PrinterPort failed: $($_.Exception.Message)"
        exit 1
    }
}
else {
    Write-Output "TCP/IP printer port already exists."
}

# Check if driver is registered in spooler
$driverExists = Get-PrinterDriver -Name $driverName -ErrorAction SilentlyContinue

Write-Output ""
Write-Output ">> Installation/Registration driver =========================="
if (-not $driverExists) {
    try {
        # Add to DriverStore + install
        & pnputil /add-driver "$infFile" /install | Out-Null

        if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 259) {
            throw "pnputil failed with exit code $LASTEXITCODE"
        }
        else {
            if ($LASTEXITCODE -ne 259) {
                Write-Output "Driver added or already present in DriverStore."
            }
            else {
                Write-Output "Driver added via pnputil (DriverStore)."
            }
            # Reset exit code, because PDQ treat 259 as failure 
            $global:LASTEXITCODE = 0
        }

        # Register with the Print Spooler
        Add-PrinterDriver -Name $driverName -ErrorAction Stop
        Write-Output "Driver registered with spooler."

        # Some environments need a spooler restart after driver registration
        Restart-Service Spooler -Force
        Start-Sleep -Seconds 2
    }
    catch {
        Write-Error "Driver installation/registration failed: $($_.Exception.Message)"
        exit 1
    }
}
else {
    Write-Output "Driver already exists."
}

# Add printer if not exists
Write-Output ""
Write-Output ">> Add printer ==============================================="
if (-not (Get-Printer -Name $printerName -ErrorAction SilentlyContinue)) {
    try {
        Add-Printer -Name $printerName -DriverName $driverName -PortName $portName -ErrorAction Stop
        Write-Output "Printer successfully added!"
    }
    catch {
        Write-Error "Add-Printer failed: $($_.Exception.Message)"
        exit 1
    }
}
else {
    Write-Output "Printer already exists."
}
