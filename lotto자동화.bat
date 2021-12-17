if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
C:/Python38-32/python.exe d:/TaiCloud/Documents/Project/Lotto/def.py