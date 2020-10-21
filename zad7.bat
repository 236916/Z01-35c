@echo off
set a=1
setlocal enabledelayedexpansion
if %1 geq 0 (
	for /l %%i in (1,1,%1) do (
		set /a a=!a! * %%i
		REM echo !a!
	)
	echo %1 silnia =  !a!
) else (
	echo Podana liczba nie jest wieksza od 0
)