$path = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\LunaAgent.bat"
Copy-Item ".\run_luna.bat" $path
Write-Host "Luna installed in Windows startup"
