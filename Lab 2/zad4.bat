@echo off
set a=0
set b=1
setlocal enabledelayedexpansion
if %1 geq 2 (
	echo %b%
	for /l %%i in (2,1,%1) do (
		set /a c=!a!+!b!
		set a=!b!
		set b=!c!
		echo !c!
	)
) else (
	if %1 equ 1 (
		echo %b%
	) else (
			echo Podana liczba nie jest wieksza od 0
	)
)