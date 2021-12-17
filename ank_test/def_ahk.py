
import time
import ahk
from ahk import AHK, Hotkey
import logging
# logging.basicConfig(level=logging.DEBUG)

ahk = AHK()

# a = ahk.mouse_position
# print(a)

# 출처: https://developer-joe.tistory.com/210 [코드 조각-Android, Java, Spring, JavaScript, C#, C, C++, PHP, HTML, CSS, Delphi]
# try:
#     ahk = AHK(executable_path="C:\\Program Files\\AutoHotkey\\AutoHotkeyU64.exe")
# except:
#     ahk = AHK(executable_path="C:\\Program Files\\AutoHotkey\\AutoHotkeyU32.exe")

# win = list(ahk.windows())
# print(win)
# ahk.run_script('Run Notepad')
for window in ahk.windows():
    a = window.title
    b = window.pid
    c = window.id
    # a = "\uc790\uc720 \ub300\ud55c\ubbfc\uad6d \ub9cc\uc138"
    # a = a.encode('utf-8')
    a = a.decode('euc-kr')
    print(a, b, c)
    # print(window.text)


# you should be able to run it this way, did not test.

# ahk_Script = ['BlockInput, MouseMove',
#               'sleep 5000', 'BlockInput, MouseMoveOff']

# for snipet in ahk_Script:
#     ahk.run_script(snipet, blocking=True)
