from pywinauto.application import Application
from kw_def import *


# app = Application(backend="uia").connect(path="nfrunlite.exe")
# a = app.top_window()
# print(a)

child_classname = []
child_handles = []
child_classname_MDIClient = []
child_handles_MDIClient = []
child_txt_MDIClient = []


def all_ok_MDIClient(hwnd, param):
    txt = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    child_classname_MDIClient.append(clas)
    child_handles_MDIClient.append(hwnd)
    child_txt_MDIClient.append(txt)
    # child_handles = child_handles[clas].append(na)
    print(f"{hwnd} : {clas} : {txt}")
    return True


def MDIClient_handle_debug(num):  # 62는 2102의 종목??
    whnd = win32gui.FindWindowEx(
        HG_titleName, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    # print(whnd)
    n = child_handles_MDIClient[num]
    # mouseClick(n)
    # print(n)
    return n


def find_handle():  # 62는 2102의 종목??
    whnd = win32gui.FindWindowEx(
        HG_titleName, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    class_list_MDIClient = child_classname_MDIClient.index("Edit")
    print(class_list_MDIClient)
    # print(whnd)
    return


def find_handle_2(title):  # 62는 2102의 종목??
    whnd = win32gui.FindWindowEx(
        HG_titleName, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    child_txt_MDIClient1 = child_txt_MDIClient.index(title)
    hendle = child_handles_MDIClient[child_txt_MDIClient1]
    print(hendle)
    # print(child_txt_MDIClient)
    # txt = win32gui.GetWindowText(class_list_MDIClient)
    # print(txt)
    return
# find_handle_2("조회")


def findTitleNameHandle(tn):
    titleName = win32gui.FindWindow(None, tn)
    print(titleName)
    whnd = win32gui.FindWindowEx(titleName, None, "Static", None)
    print(whnd)


def handle_32770():
    titleName = win32gui.FindWindow(None, "확인")
    whnd = win32gui.FindWindowEx(titleName, None, "Static", None)
    if whnd == 0:
        # print("없음")
        return
    else:
        txt = win32gui.GetWindowText(whnd)
        if txt == "매수가격이 현재가의 15% 범위보다 낮습니다. 계속하시겠습니까?":
            whnd2 = win32gui.FindWindowEx(titleName, None, "Button", "예(&Y)")
            mouseClick(whnd2)
        else:
            return
    # print(txt)
    # win32gui.EnumChildWindows(titleName, all_ok, None)
    # class_list = child_classname.index("Edit")
    # print(class_list)
    # # return child_handles_32770[class_list]

# 매수중 증거금 부족으로 안내창이 뜨는경우
# class = #32770 (Dialog) caption = 안내


def handle_32770_info():  # 매수 증거금 부족으로 에러
    titleName = win32gui.FindWindow(None, "안내")
    whnd = win32gui.FindWindowEx(titleName, None, "Static", None)
    if whnd == 0:
        # print("없음")
        return
    else:
        txt = win32gui.GetWindowText(whnd)
        if txt == "[855056] 매수증거금이 부족합니다. 매수가능(16)주":
            whnd2 = win32gui.FindWindowEx(titleName, None, "Button", "확인")
            mouseClick(whnd2)
        else:
            return


def screen_xy_debug(num):
    hwnd = MDIClient_handle_debug(num)
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    print(x, y, x1, y1)
    pag.click(x, y+(y*0.4), button='right')
    print("debug끝")


if __name__ == "__main__":
    # findTitleNameHandle("예수금")
    pass
    # screen_xy_debug(30)
    # mouseClick(1902216)
    # # MDIClient_handle(74)  # 15 or 10
    # # acc_window = MDIClient_handle(74)  # 15 or 10
    # # mouseClick(acc_window)
    # # print(len(child_handles_MDIClient))
    # # txt = win32gui.GetWindowText(acc_window)
    # # print(f"Handle : {acc_window}")
    # # print(f"TEXT : {txt}")
    # # titles = gw.getAllTitles()
    # # print(titles)
    # kw_window_click("[2102] 해외주식 미니주문", 0, 0)
    # # kw_win = gw.getWindowsWithTitle("[2102] 해외주식 미니주문")
    # # kw_win = gw.getWindowsWithTitle("영웅문Global")[0]
    # # print(kw_win)
    # MDIClient_handle_debug(18)
    # mouseClick(MDIClient_handle_debug(18))
    # mouseClick_right(3934636)
    # screen_xy_debug(18)
