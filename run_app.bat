@echo off
REM Batch script to launch the Streamlit application
REM Breast Cancer Classification Model Comparison

echo.
echo =====================================================
echo Breast Cancer Classification Model Comparison App
echo =====================================================
echo.

REM Navigate to the project directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

REM Launch the Streamlit app
echo Launching Streamlit app...
echo The app will open in your default browser at http://localhost:8501
echo.
python -m streamlit run streamlit_app.py --logger.level=error

pause
