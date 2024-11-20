# Ensure the script stops on errors
$ErrorActionPreference = "Stop"

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
& .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

Write-Host "Environment setup complete, activating environment..."
