from ahk import AHK
from ahk.window import Window
ahk = AHK()
# win = ahk.win_get(title='영웅문Global')
# win = ahk.active_window
# win = list(ahk.windows())
# # win = ahk.windows()

# win = Window(ahk, ahk_id='0x60d98')

# print(win.pid)


def findWindow_ahk(title):
    win_list = ahk.windows()
    winDic = {}
    for window in win_list:
        i = 0
        winTitle = window.title
        winPid = window.pid
        winTitle = winTitle.decode('euc-kr')
        # print(winTitle, winId)
        winDic[winTitle] = winPid
    return winDic[title]
    # print(winDic)


def checkActiveWindow():
    activeWindow = ahk.active_window
    activeWindow = activeWindow.title.decode('euc-kr')
    print(activeWindow)


def findClassNN(title):

    titlePid = findWindow_ahk(title)
    # print(win.pid)
    print(titlePid)


myScript = r"D:\TaiCloud\Documents\Project\Lotto\ank_test\myScript.ahk"


def ahkcommunication():
    myScript = r"D:\myScript.ahk"
    result = ahk.run_script(myScript)
    print(result)  # Hello Data!
    result = ahk.run_script(myScript, decode=False)
    print(result.stdout)  # b'Hello Data!'


if __name__ == '__main__':
    # checkActiveWindow()
    ahkcommunication()
