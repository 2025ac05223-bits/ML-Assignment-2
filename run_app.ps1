# PowerShell script to launch the Streamlit application
# Breast Cancer Classification Model Comparison

Write-Host "`n"
Write-Host "=====================================================" -ForegroundColor Green
Write-Host "Breast Cancer Classification Model Comparison App" -ForegroundColor Green
Write-Host "=====================================================" -ForegroundColor Green
Write-Host "`n"

# Set the location to the script directory
Set-Location $PSScriptRoot

# Check if Python is installed
try {
    python --version | Out-Null
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Launch the Streamlit app
Write-Host "Launching Streamlit app..." -ForegroundColor Yellow
Write-Host "The app will open in your default browser at http://localhost:8501`n" -ForegroundColor Cyan

python -m streamlit run streamlit_app.py --logger.level=error

Read-Host "Press Enter to exit"
