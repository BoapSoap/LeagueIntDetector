@echo off

:: Check if running in PowerShell
if defined PSModulePath (
    echo This script cannot be run from PowerShell. Use setup.ps1
    exit /b
)

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

echo Environment setup complete, activating environment...
