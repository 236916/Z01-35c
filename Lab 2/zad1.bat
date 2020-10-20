@echo off
set CUR_DIR=%CD%
cd %2
if %errorlevel% equ 0 ( 
	dir "*.%1" 
	cd %CUR_DIR%
)