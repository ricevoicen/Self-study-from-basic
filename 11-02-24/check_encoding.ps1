# Add at the very beginning of the script
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Get the current script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
# Construct full path to Binary.py
$filePath = Join-Path $scriptPath "Binary.py"

Write-Host "Checking file: $filePath"

# Check if file exists
if (-not (Test-Path $filePath)) {
    Write-Host "Error: File not found at $filePath"
    exit
}

# Read the file content as bytes
try {
    $bytes = Get-Content -Path $filePath -Encoding Byte -ReadCount 1024 -ErrorAction Stop

    # Check for BOM (Byte Order Mark)
    if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        Write-Host "Encoding: UTF-8 with BOM"
    } elseif ($bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) {
        Write-Host "Encoding: UTF-16 LE"
    } elseif ($bytes[0] -eq 0xFE -and $bytes[1] -eq 0xFF) {
        Write-Host "Encoding: UTF-16 BE"
    } else {
        # Try to detect UTF-8 without BOM
        $isUtf8 = $true
        $position = 0
        while ($position -lt $bytes.Count) {
            if ($bytes[$position] -lt 0x80) {
                $position++
            } elseif ($bytes[$position] -ge 0xC0 -and $bytes[$position] -le 0xDF) {
                if ($position + 1 -ge $bytes.Count -or $bytes[$position + 1] -lt 0x80 -or $bytes[$position + 1] -ge 0xC0) {
                    $isUtf8 = $false
                    break
                }
                $position += 2
            } else {
                $isUtf8 = $false
                break
            }
        }
        
        if ($isUtf8) {
            Write-Host "Encoding: UTF-8 without BOM"
        } else {
            Write-Host "Encoding: ANSI/ASCII or other encoding"
        }
    }

    # Additional check using .NET
    $content = [System.IO.File]::ReadAllBytes($filePath)
    $encoding = [System.Text.Encoding]::Default
    try {
        $decoded = $encoding.GetString($content)
        Write-Host "`nSystem default encoding detection: $($encoding.WebName)"
    } catch {
        Write-Host "`nFailed to decode with system default encoding"
    }
} catch {
    Write-Host "Error reading file: $_"
} 