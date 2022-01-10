
taskkill /f /pid 22260
timeout /t 1
xcopy "D:\TaiCloud\Documents\Project\Lotto\Lotto/Updater" "D:\TaiCloud\Documents\Project\Lotto\Lotto" /e /y
rmdir /s /q "Updater"
"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe"            
del "D:\TaiCloud\Documents\Project\Lotto\Lotto\Dispatch.bat"
            