# Create logs directory if it doesn't exist
if (-Not (Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" > $null
}

# Create virtual environment if it doesn't exist
if (-Not (Test-Path -Path "venv")) {
    Write-Host "`nCreating virtual environment..." -NoNewline
    python -m venv venv
    Write-Host " Done.`n"
}

# Load environment variables from .env file
$envFile = ".env"

if (Test-Path -Path $envFile) {
    Write-Host "`nLoading environment variables from $envFile..." -NoNewline
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^\s*([^#][^=]*)\s*=\s*(.*)\s*$") {
            [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
        }
    }
    Write-Host " Done.`n"
}
else {
    Write-Host "`n$envFile file not found. Please create it manually.`n"
}

# Activate virtual environment
Write-Host "`nActivating virtual environment..." -NoNewline
& .\venv\Scripts\Activate
Write-Host " Done.`n"

# Install dependencies
Write-Host "`nCheck dependencies..." -NoNewline
Invoke-Expression  "pip install -r requirements.txt" > logs/requirements.log 2>&1
Write-Host " Done.`n"

# Run behave tests and generate Allure report
Write-Host "Test execution in progress... `n" -NoNewline
Invoke-Expression "behave -f allure_behave.formatter:AllureFormatter -o reports > logs/allure.log 2>&1"

# Open Allure report
Write-Host ""
Invoke-Expression "allure serve reports"