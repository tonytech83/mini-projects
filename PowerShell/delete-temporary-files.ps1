# Clean "C:\Windows\Temp"
Get-ChildItem -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue |
ForEach-Object {
    try {
        Remove-Item -LiteralPath $_.FullName -Force -Recurse -ErrorAction Stop
    }
    catch {
        Write-Verbose "Skipping: $($_.FullName) — $($_.Exception.Message)"
    }
}

# Clean C:\Users\<current user>\AppData\Local\Temp
Get-ChildItem -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue |
ForEach-Object {
    try {
        Remove-Item -LiteralPath $_.FullName -Force -Recurse -ErrorAction Stop
    }
    catch {
        Write-Verbose "Skipping: $($_.FullName) — $($_.Exception.Message)"
    }
}
