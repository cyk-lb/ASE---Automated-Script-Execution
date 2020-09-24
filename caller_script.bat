@ECHO OFF
:: Some information text
ECHO Automatic scheduled dataloading-task has been started.
:: path to execution-logic script, may also be absolute: C:\User\...\script.py
python script.py
:: wait for the user to end the programm
ECHO Automatic scheduled dataloading-task has finished.
pause