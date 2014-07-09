@echo off
:again 
   echo Running this script outside active virtualenv
   echo can cause wrong python shell to compile the code.
   echo:
   set /p answer=Are you sure you're in active python 2.6 virtualenv (Y/N)?
   if /i "%answer:~,1%" EQU "Y" goto doeet
   if /i "%answer:~,1%" EQU "N" exit /b
   echo Please type Y for Yes or N for No
   goto again

:doeet
	mklink /d lib\tcl8.5 "C:\Python\tcl\tcl8.5\"
	mklink /d lib\tk8.5 "c:\Python\tcl\tk8.5\"

	start cmd /k python -c "from idlelib.PyShell import main; main()"& exit
