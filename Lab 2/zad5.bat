@echo off
echo Podany tytul filmu: %1
ffmpeg.exe -i %1.flv  -ss 00:00:%2.0 -vframes 1 miniaturka.png
if %errorLevel% equ 0  (
	miniaturka.png 
) else ( 
	echo Plik lub sekunda nie istnieje! 
)
