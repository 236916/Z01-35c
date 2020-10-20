@echo off

set DEEP_STEP=5
if	"%1"=="" ( 
	echo Start DIR: %CD%
) else ( 
	echo Start DIR: %1
)
goto :startProcedure %1 %2 

:startProcedure

	set /a DEEP=%2 + %DEEP_STEP%
	if	"%1"=="" ( 
		set DIR=%CD%
	) else ( 
		set DIR=%1 
	)

	set DIR=%DIR: =%

	set repeatChar=-
	set returnStr=-

	setlocal enabledelayedexpansion
	for /l %%i IN (1,1,%DEEP%) DO (
	       set returnStr=!returnStr!%repeatChar%
	)
	echo %returnStr%V
	for %%i in ("%DIR%\*") do ( 
		echo %returnStr%%%~ni%%~xi
	)

	for /D %%i in ("%DIR%\*") DO ( 
		echo %returnStr%%%~ni
		call :startProcedure %%i %DEEP%
	)
exit /b
