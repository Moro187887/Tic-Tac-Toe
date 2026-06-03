@echo off
cd /d "%~dp0"
python tic_tac_toe.py
if errorlevel 1 py tic_tac_toe.py
pause
