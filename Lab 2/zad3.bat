@echo off
net session >nul 2>&1
if %errorLevel% EQU 0 (
	echo Skrypt uruchomiony jako administrator!
) else (
	echo Skrypt NIE jest uruchomiony jako administrator!
)