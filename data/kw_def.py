import win32con
import win32gui
import win32api
import pyautogui as pag
import pygetwindow as gw
import pywinauto
import time
# from ss_def import *


# FindWindowEx
# 첫번째 인수는 부모 윈도우의 핸들,
# 두번째 인수는 자식 윈도우의 핸들,
# 세번째 인수는 클래스명,
# 네번째 인수는 윈도우 창 제목입니다.


def kw_window(l=0, r=0):
    # pag.press("esc", 5)
    time.sleep(0.3)
    kw_win = gw.getWindowsWithTitle("영웅문Global")[0]
    if kw_win.isActive == False:
        pywinauto.application.Application().connect(
            handle=kw_win._hWnd).top_window().set_focus()
    kwActivage = kw_win.activate()  # 윈도우 활성화
    time.sleep(0.3)
    return kwActivage
    # pag.click(kw_win.left+l, kw_win.top+r)


# kwActivage = kw_window()


def kw_window_click(window, l, r):
    # kw_window()
    time.sleep(0.3)
    win = gw.getWindowsWithTitle(window)[0]
    # win_left = win.left
    # win_top = win.top
    # pag.moveRel(win.left+l, win.top+r)
    # pag.moveTo(win.left+l, win.top+r)
    pag.click(win.left+l, win.top+r)

    # return win_left, win_top
# kw_window_click("영웅문Global", 428, 557)


def sendText(hwnd, text):
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)  # 엔터키
    pag.press('enter')


def mouseClick(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    # time.sleep(0.2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)


def mouseClick_right(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_RBUTTONDOWN, 0, 0)
    # time.sleep(0.2)
    win32gui.PostMessage(hwnd, win32con.WM_RBUTTONUP, 0, 0)


child_classname = []
child_handles = []
child_classname_MDIClient = []
child_handles_MDIClient = []
child_txt_MDIClient = []


def all_ok(hwnd, param):
    # na = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    child_classname.append(clas)
    child_handles.append(hwnd)
    # child_handles = child_handles[clas].append(na)
    # print(f"{na}: {hwnd} : {clas}")
    return True


def all_ok_MDIClient(hwnd, param):
    txt = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    child_classname_MDIClient.append(clas)
    child_handles_MDIClient.append(hwnd)
    # child_handles = child_handles[clas].append(na)
    # print(f"{hwnd} : {clas} : {txt}")
    return True


HG_titleName = win32gui.FindWindow(None, "영웅문Global")


def kw_secrch_Edit():  # 메인 검색창의 Edit 29번
    whnd = win32gui.FindWindowEx(HG_titleName, None, "AfxControlBar110", None)
    win32gui.EnumChildWindows(whnd, all_ok, None)
    class_list = child_classname.index("Edit")
    # print(class_list)
    return child_handles[class_list]


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
            print("매수가격이 현재가의 15% 범위보다 낮게 주문합니다.")
        else:
            return


def MDIClient_handle(num):  # 62는 2102의 종목??
    whnd = win32gui.FindWindowEx(
        HG_titleName, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    mouseClick(child_handles_MDIClient[num])
    return child_handles_MDIClient[num]


def input2102_Stockname(stock):
    kw_window()
    whnd = win32gui.FindWindowEx(
        HG_titleName, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    # MDIClient_handle(62)
    stockName = child_handles_MDIClient[62]
    mouseClick(stockName)
    pag.typewrite(stock)
    pag.press('enter')
    return print(f"종목 : {stock} 입력완료.")


def input2102_Qty(qty):
    MDIClient_handle(83)
    pag.typewrite(str(qty))
    pag.press('enter')
    return print(f"수량 : {qty}개 입력완료.")


def input2102_price(price):
    # if type(print) == "int":
    price = float(price)
    price = str(round(price, 2))
    pag.typewrite(price)
    return print(f"주문금액 : ${price} 입력완료.")


def test_input2102_price(price):
    print("값", type(price))
    if type(price) == "int":
        print("int")
    else:
        type(price) == "str"
        print("str")

# test_input2102_price(111)


def input2102_finshBuy(test):
    MDIClient_handle(78)
    time.sleep(0.3)
    if test == "test":
        handle_32770()
        pag.press('esc')
        print("Test모드")

    else:
        pag.press('enter')
        time.sleep(0.3)
        pag.press('enter')


def input2102_finshsell(test):
    MDIClient_handle(74)
    time.sleep(0.3)
    if test == "test":
        pag.press('esc', 1)
        print("Test모드")
    else:
        pag.press('enter')


def check_message():
    time.sleep(0.5)
    check_message_title = win32gui.FindWindow(None, "안내")
    mag = win32gui.FindWindowEx(check_message_title, None, "Static", None)
    button = win32gui.FindWindowEx(check_message_title, None, "Button", None)
    kw_window()
    if check_message_title == 0:
        return
    else:
        time.sleep(0.3)
        mouseClick(button)
        txt = win32gui.GetWindowText(mag)
        return print(txt)


# check_message()


def input2102_check_accuntNumber(acount=0):
    MDIClient_handle(15)  # 15 or 10
    pag.press("up", 5)
    pag.press("down", acount)
    pag.press('enter')


def input2102_check_loc():
    MDIClient_handle(67)  # 15 or 10
    pag.press("up", 8)
    pag.press("down", 3)
    pag.press('enter')


def input2102_buy(stockname, qty, price, test="test"):
    time.sleep(0.3)
    input2102_Stockname(stockname)
    input2102_check_loc()
    input2102_Qty(qty)
    input2102_price(price)
    input2102_finshBuy(test)  # 실제주문시 필요한


def input2102_buy_VR(stockname, qty=1, test="test"):
    buy_valueList = buy_values()
    # input2102_check_accuntNumber(1)
    # print(buy_valueList)
    for i in buy_valueList:
        # print(buy_valueList)
        time.sleep(0.3)
        input2102_Stockname(stockname)
        input2102_check_loc()
        input2102_Qty(qty)
        input2102_price(i)
        input2102_finshBuy(test)  # 실제주문시 필요한


def input2102_sell(stockname, qty, price, test="test"):
    time.sleep(0.3)
    input2102_Stockname(stockname)
    input2102_Qty(qty)
    input2102_price(price)
    input2102_finshsell(test)


if __name__ == '__main__':
    # kw_window()
    # input2102_buy_VR("TQQQ", 1, "start")
    #     input2102_buy("TQQQ", 33, 123.0000)
    #     check_message()
    #     check_accuntNumber()
    # input2102_Qty(2)
    # input2102_check_accuntNumber(1)
    MDIClient_handle(1)
