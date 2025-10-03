@echo off
REM Creates a Task Scheduler task to run run_hidden.vbs on user logon

schtasks /Create /TN "FileManagerMonitor" /TR "\"%~dp0run_hidden.vbs\"" /SC ONLOGON /RL HIGHEST /F

echo Task Scheduler entry created.
