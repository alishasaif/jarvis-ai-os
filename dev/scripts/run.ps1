Write-Host ""
Write-Host "======================================" -ForegroundColor DarkYellow
Write-Host "        J.A.R.V.I.S AI OS" -ForegroundColor Yellow
Write-Host "======================================" -ForegroundColor DarkYellow
Write-Host ""

$ProjectRoot = Split-Path $PSScriptRoot -Parent
$ProjectRoot = Split-Path $ProjectRoot -Parent

Set-Location $ProjectRoot

if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
    Write-Host "Virtual environment not found!" -ForegroundColor Red
    exit
}

Write-Host "Activating virtual environment..." -ForegroundColor Cyan

& ".\.venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Launching J.A.R.V.I.S..." -ForegroundColor Green
Write-Host ""

python launcher.py
