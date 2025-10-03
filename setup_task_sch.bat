@echo off
:: Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb runAs"
    exit /b
)
@echo off
:: Install watchdog package if not already installed
python -m pip install --upgrade watchdog

REM Creates a Task Scheduler task to run run_invs.vbs on user logon

schtasks /Create /TN "FileManager" /TR "\"wscript.exe\" \"%~dp0run_invs.vbs\"" /SC ONSTART /RL HIGHEST /F
schtasks /Run /TN "FileManager"

echo Task Scheduler entry created.
pause