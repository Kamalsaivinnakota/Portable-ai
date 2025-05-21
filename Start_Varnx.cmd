@echo off
REM Change directory to the Varnx folder on your USB
cd /d %~dp0

REM Activate WinPython python and run your main script
WinPython\python-3.11.5.amd64\python.exe varnx\main.py

pause
