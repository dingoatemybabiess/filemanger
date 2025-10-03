# FileManager Automation Repository

## Overview

This repository contains scripts to monitor and organize your Downloads folder automatically using Python Watchdog.

## Files

- `file_Managment.py` - Python file organizer script.
- `file_manager.bat` - Batch file to run the script manually.
- `run_inv.vbs` - Runs the batch file silently (no console window).
- `setup_task_sch.bat` - Sets up a Windows Task Scheduler entry to run on startup.
- `README.md` - This instructions file.

## Setup Instructions

1. Ensure you have Python (Anaconda or system Python) installed.
2. Edit `file_manager.bat` to point to your python executable path if different.
3. Run `file_Managment.py` manually one time to test functionality.
4. To run silently, double-click `run_inv.vbs`.
5. (Optional) To configure auto run on startup:
   - Run `setup_task_sch.bat` as Administrator.
   - This creates a scheduled task that auto-starts the monitoring script on login.

## Troubleshooting

- Check paths in `.bat` and `.vbs` files.
- Verify Python environment and package installations.
- Use Task Scheduler UI or `schtasks /Query` to check the task status.
