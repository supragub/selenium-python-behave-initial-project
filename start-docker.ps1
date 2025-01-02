# Running Docker Compose
Start-Process "powershell" -ArgumentList "-NoExit", "docker-compose up --build"

# Waiting for the Behave server to start
$serverStarted = $false
while (-not $serverStarted) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:4040" -UseBasicParsing
        if ($response.StatusCode -eq 200) {
            $serverStarted = $true
        }
    } catch {
        Start-Sleep -Seconds 3
    }
}

# Opening the browser with the Allure report URL
Start-Process "http://localhost:4040"