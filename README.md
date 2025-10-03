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
2. run `setup_task_sch.bat` this will run as Adminstrator.
3. enshure the program ran properly by opiening
4. task scheduler then search in task scheduler library for FileManager
5. optional: press right click then run it

## Troubleshooting

- Edit `file_manager.bat` to point to your python executable path if different.
- Check paths in `.bat` and `.vbs` files.
- Verify Python environment and package installations.
- Use Task Scheduler UI or `schtasks /Query` to check the task status.
