# from re import A
import win32con
import win32gui
import win32api
import pyautogui as pag
import pygetwindow as gw
import pywinauto
import time
# import datetime
from datetime import date
# from def_lotto import closeLotto
from def_ss import *
import exchange_calendars as ecals
import pyperclip
# import csv
from slack_engin import *
from def_xyp import xyp_findxy
# import subprocess
import uiautomation as auto
from def_ui import *
# from def_loggin import accunt_info


def accunt_info(user, type):
    # {"무메":[계좌순서,매수수량]]}
    acc_type = {"kwak": {"무매": [0, 0], "적립식": [1, 2], "거치식": [
        2, 7], "ava": [3, 0], "TLP2": [4, 0]}, "lee": {"무매": [0, 0], "적립식": [0, 1], "거치식": [2, 7]},
        "han": {"무매": [0, 0], "적립식": [0, 1], "거치식": [2, 14]}}
    # accuntInfo = accunt_info(user, type)
    accNum = acc_type[user][type][0]
    vr_qty = acc_type[user][type][1]
    return accNum, vr_qty


def today_nowDate():
    datetime.today()
    today_now_date = datetime.today().strftime("%Y%m%d")

    return today_now_date


def typewrite_def(typewrite, commend=0):
    pag.typewrite(typewrite, interval=0.1)
    if commend == 0:
        time.sleep(0.5)
        return
    else:
        time.sleep(0.3)
        print(commend)


def get_today_week():
    weeks = [1, 2, 3, 4, 5, 6, 7]
    return weeks[datetime.datetime.today().weekday()]


def get_today_hoilday():
    XNYS = ecals.get_calendar("XNYS")
    todayis = str(date.today())
    return XNYS.is_session(todayis)


def kw_window_org(l=0, r=0):
    i = 1
    while i < 10:
        try:
            HG_titleName = win32gui.FindWindow(None, "영웅문Global")
            if HG_titleName > 0:
                time.sleep(0.3)
                win32gui.SetForegroundWindow(HG_titleName)
                time.sleep(0.3)
                logger.debug(HG_titleName)
                return HG_titleName
            else:
                time.sleep(3)
                logger.info(f"영웅문Global 확인안됨. {i}회 재 확인")
                i = i + 1
        except:
            pass


def kw_window(l=0, r=0):
    try:
        anWindow = auto.WindowControl(
            searchDepth=2, Name='영웅문Global')
        if not anWindow.Exists(10, 1):
            print('Can not find Notepad window')
            # exit(0)
            return 0
        anWindow.SetActive()
        return 1
    except:
        # print("asdf")
        pass


def activeWindow(title, l=0, r=0):
    # pag.press("esc", 5)
    time.sleep(0.3)
    kw_win = gw.getWindowsWithTitle(title)[0]
    if kw_win.isActive == False:
        pywinauto.application.Application().connect(
            handle=kw_win._hWnd).top_window().set_focus()
    kwActivage = kw_win.activate()  # 윈도우 활성화
    time.sleep(0.3)
    return kwActivage


def kw_window_check_kwlogin(l=0, r=0):
    i = 0
    while i < 10:
        try:
            i = i+1
            HG_titleName = win32gui.FindWindow(None, "영웅문Global Login")
            if HG_titleName > 0:
                time.sleep(0.3)
                win32gui.SetForegroundWindow(HG_titleName)
                time.sleep(0.3)
                logger.debug(HG_titleName)
                return HG_titleName
                break
            else:
                time.sleep(1)
                logger.info(f"{i}창없음")
                continue
        except:
            # raise kw_window()
            pass


def kw_window_click(window, l=0, r=0):
    i = 0
    while i < 10:
        try:
            i = i+1
            HG_titleName = win32gui.FindWindow(None, window)
            if HG_titleName > 0:
                time.sleep(0.3)
                win32gui.SetForegroundWindow(HG_titleName)
                time.sleep(0.3)
                logger.DEBUG(window, HG_titleName)
                return HG_titleName
            else:
                logger.info(f"{i}: {window} 창없음")
                time.sleep(3)
                continue
        except:

            pass


def sendText(hwnd, text):
    # print(f"test: {hwnd} : {text}")
    time.sleep(0.3)
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)  # 엔터키
    time.sleep(0.3)
    pag.press('enter')


def mouseClick(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    # time.sleep(0.2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)


child_classname_1 = []
child_handles_1 = []
child_classname_MDIClient_1 = []
child_handles_MDIClient_1 = []
child_txt_MDIClient = []
AfxControlBar110_classname_MDIClient = []
AfxControlBar110_handles_MDIClien = []


def all_ok_1(hwnd, param):
    na = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    child_classname_1.append(clas)
    child_handles_1.append(hwnd)
    # child_handles = child_handles[clas].append(na)
    # print(f"all_ok_1 {na}: {hwnd} : {clas}")
    return True


def all_ok_AfxControlBar110(hwnd, param):
    na = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    AfxControlBar110_classname_MDIClient.append(clas)
    AfxControlBar110_handles_MDIClien.append(hwnd)
    # child_handles = child_handles[clas].append(na)
    # print(f"all_ok_1 {na}: {hwnd} : {clas}")
    return True


def all_ok_MDIClient(hwnd, param):
    # child_classname_MDIClient_1 = []
    # child_handles_MDIClient_1 = []
    # child_txt_MDIClient = []
    txt = win32gui.GetWindowText(hwnd)
    clas = win32gui.GetClassName(hwnd)
    child_classname_MDIClient_1.append(clas)
    child_handles_MDIClient_1.append(hwnd)
    child_txt_MDIClient.append(txt)
    # child_handles = child_handles[clas].append(na)
    # print(f"{hwnd} : {clas} : {txt}")
    return True


# HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
# print(f"HG_titleName_1 : {HG_titleName_1}")


# 에러검토
#   File "d:/TaiCloud/Documents/Project/Lotto/main_han.py", line 36, in <module>
#     save_screenshot(user)
#   File "d:\TaiCloud\Documents\Project\Lotto\def_kw.py", line 382, in save_screenshot
#     sendText(kw_secrch_Edit(), "2152")
#   File "d:\TaiCloud\Documents\Project\Lotto\def_kw.py", line 213, in kw_secrch_Edit
#     class_list_1 = AfxControlBar110_classname_MDIClient.index("Edit")
# ValueError: 'Edit' is not in list
# def kw_secrch_Edit_test():  # 메인 검색창의 Edit 29번
#     # HG_titleName_1 = globalHandleV()
#     HG_titleName_1 = kw_window()
#     # HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
#     # child_classname_1.clear
#     whnd = win32gui.FindWindowEx(
#         HG_titleName_1, None, "AfxControlBar110", None)
#     win32gui.EnumChildWindows(whnd, all_ok_AfxControlBar110, None)
#     class_list_1 = AfxControlBar110_classname_MDIClient.index("Edit")
#     logger.debug(AfxControlBar110_classname_MDIClient)
#     return AfxControlBar110_handles_MDIClien[class_list_1]


def kw_secrch_Edit():  # 메인 검색창의 Edit 29번
    # HG_titleName_1 = globalHandleV()
    child_classname_all_ok_AfxControlBar110_def = []
    child_handles_all_ok_AfxControlBar110_def = []
    child_txt_all_ok_AfxControlBar110_def = []

    def all_ok_AfxControlBar110_def(hwnd, param):
        txt = win32gui.GetWindowText(hwnd)
        clas = win32gui.GetClassName(hwnd)
        child_classname_all_ok_AfxControlBar110_def.append(clas)
        child_handles_all_ok_AfxControlBar110_def.append(hwnd)
        child_txt_all_ok_AfxControlBar110_def.append(txt)
        # print(f"{hwnd} : {clas} : {txt}")  # debug 용
        return True
    HG_Global = win32gui.FindWindow(None, "영웅문Global")
    whnd = win32gui.FindWindowEx(
        HG_Global, None, "AfxControlBar110", None)
    win32gui.EnumChildWindows(whnd, all_ok_AfxControlBar110_def, None)
    cla = child_classname_all_ok_AfxControlBar110_def
    hand = child_handles_all_ok_AfxControlBar110_def
    txt = child_txt_all_ok_AfxControlBar110_def
    class_list = cla.index("Edit")
    logger.debug(f"결과: {hand[class_list]}")
    return hand[class_list]


# def find_handle_2(title):  # 62는 2102의 종목??
#     # child_handles_MDIClient_1.clear
#     # child_txt_MDIClient.clear
#     HG_titleName = win32gui.FindWindow(None, "영웅문Global")
#     whnd = win32gui.FindWindowEx(
#         HG_titleName, None, "MDIClient", None)
#     # print(f"find_handle_2 :{whnd}")
#     win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
#     # print(f"{child_txt_MDIClient} : {child_classname_MDIClient_1} : {child_handles_MDIClient_1}")
#     child_txt_MDIClient1 = child_txt_MDIClient.index(title)
#     hendle = child_handles_MDIClient_1[child_txt_MDIClient1]
#     return hendle


def find_handle_3(title, childNum):
    titleNum, child_handles_MDIClient_1 = find_titleNum(title)
    logger.debug(child_handles_MDIClient_1)
    Num = titleNum + childNum
    logger.debug(f"NUM : {Num}")
    hendle = child_handles_MDIClient_1[Num]
    mouseClick(hendle)
    return hendle


def find_handle_3_nonClick(title, childNum):
    titleNum, child_handles_MDIClient_1 = find_titleNum(title)
    Num = titleNum + childNum
    hendle = child_handles_MDIClient_1[Num]
    return hendle


def MDIClient_def():
    child_classname_MDIClient_def = []
    child_handles_MDIClient_def = []
    child_txt_MDIClient_def = []

    def all_ok_MDIClient11(hwnd, param):
        # child_classname_MDIClient_1 = []
        # child_handles_MDIClient_1 = []
        # child_txt_MDIClient = []
        txt = win32gui.GetWindowText(hwnd)
        clas = win32gui.GetClassName(hwnd)
        child_classname_MDIClient_def.append(clas)
        child_handles_MDIClient_def.append(hwnd)
        child_txt_MDIClient_def.append(txt)
        # child_handles = child_handles[clas].append(na)
        # print(f"{hwnd} : {clas} : {txt}")  #DEBUG
        return True
    HG_Global = win32gui.FindWindow(None, "영웅문Global")
    whnd = win32gui.FindWindowEx(HG_Global, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient11, None)
    cla = child_classname_MDIClient_def
    hand = child_handles_MDIClient_def
    txt = child_txt_MDIClient_def
    return cla, hand, txt


def find_titleNum(title):
    cls, hand, txt = MDIClient_def()
    titleNum = txt.index(title)  # 타이틀의 순번찾기
    # print(f"titleNum: {titleNum},hand : {hand[16]}")
    # print(f"txt : {txt[16]}")
    # print(f"hand : {hand[16]}")
    # print(f"cls : {cls[16]}")
    return int(titleNum), hand


def handle_32770():
    titleName = win32gui.FindWindow(None, "확인")
    titleName_2 = win32gui.FindWindow(None, "안내")
    whnd = win32gui.FindWindowEx(titleName, None, "Static", None)
    whnd2 = win32gui.FindWindowEx(titleName_2, None, "Static", None)
    if whnd == 0:
        logger.debug("없음")
        return
    else:
        txt = win32gui.GetWindowText(whnd)
        txt2 = win32gui.GetWindowText(whnd2)
        if txt == "매수가격이 현재가의 15% 범위보다 낮습니다. 계속하시겠습니까?":
            whnd = win32gui.FindWindowEx(titleName, None, "Button", "예(&Y)")
            mouseClick(whnd)
            print("매수가격이 현재가의 15% 범위보다 낮게 주문합니다.")
        elif txt == "매도가격이 현재가의 15% 범위보다 높습니다. 계속하시겠습니까?":
            whnd = win32gui.FindWindowEx(titleName, None, "Button", "예(&Y)")
            mouseClick(whnd)
            print("매수가격이 현재가의 15% 범위보다 높게 주문합니다.")
        # elif txt2 == "[855056] 매수증거금이 부족합니다. 매수가능(0)주" :
        #     print("txt2")
        #     whnd2 = win32gui.FindWindowEx(titleName_2, None, "Button", "확인")
        #     mouseClick(whnd2)
            # return print("매수가능(0)주 임으로 , 매수를 종료합니다.")
        else:
            return


def handle_855056():
    titleName_2 = win32gui.FindWindow(None, "안내")
    whnd2 = win32gui.FindWindowEx(titleName_2, None, "Static", None)
    if whnd2 == 0:
        # print("없음")
        return
    else:
        txt2 = win32gui.GetWindowText(whnd2)
        if txt2 == "[855056] 매수증거금이 부족합니다. 매수가능(0)주":
            whnd2 = win32gui.FindWindowEx(titleName_2, None, "Button", "확인")
            mouseClick(whnd2)
            return 0
        else:
            return


# def MDIClient_handle(num):  # 사용안함
#     HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
#     whnd = win32gui.FindWindowEx(
#         HG_titleName_1, None, "MDIClient", None)
#     win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
#     mouseClick(child_handles_MDIClient_1[num])
#     return child_handles_MDIClient_1[num]
# # print(MDIClient_handle(32))


# def MDIClient_handle_test(title, num):  # 사용안함
#     HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
#     titleNUM = find_titleNum(title)
#     tergetNum = num + titleNUM
#     mouseClick(child_handles_MDIClient_1[tergetNum])
#     return child_handles_MDIClient_1[tergetNum]


# def MDIClient_handle_nonclick(num):  # 62는 2102의 종목??
#     HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
#     # child_handles_MDIClient_1 =[]
#     whnd = win32gui.FindWindowEx(
#         HG_titleName_1, None, "MDIClient", None)
#     win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
#     # mouseClick(child_handles_MDIClient_1[num])
#     return child_handles_MDIClient_1[num]


# def save_screenshot_hwnd(user):
#     kw_window()
#     sendText(kw_secrch_Edit(), "2152")
#     time.sleep(2)
#     # hwnd = MDIClient_handle(21)
#     hwnd = find_handle_3_nonClick("[2152] 계좌정보(T) - 해외주식 실시간미체결", 21)
#     win32gui.SetForegroundWindow(hwnd)
#     x, y, x1, y1 = win32gui.GetClientRect(hwnd)
#     x, y = win32gui.ClientToScreen(hwnd, (x, y))
#     filename = user
#     pag.screenshot(f'img/{filename}.png', region=(x, y, 933, 500))
#     slackSendMsg(f"{user}")
#     slackSendFile(user)
#     # print(x,y)
#     return


def save_screenshot(user, type=0):  # 캡쳐로 실행여부 확인
    kw_window()
    pag.press('esc', 5)
    sendText(kw_secrch_Edit(), "2152")
    time.sleep(2)
    x, y = xyp_findxy("2152")
    logger.info(x, y)
    filename = user
    pag.screenshot(f'img/{filename}.png',
                   region=(x-130, y-20, 933, 500))
    # pag.screenshot(f'img/{filename}_{type}.png',
    #                region=(x-130, y-20, 933, 500))
    slackSendMsg(f"{user}: {type}의 스크린샷")
    slackSendFile(user, type)
    return
# save_screenshot('kwak')
# im3 = pyautogui.screenshot('my_region.png', region=(0, 0, 300, 300))


def screen_xy():
    # hwnd = MDIClient_handle(32)
    hwnd = find_handle_3('[2150] 계좌정보(T) - 해외주식 실시간잔고', 21)
    logger.info(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    # logger.debug(x, y, x1, y1)
    # pag.press('up', 3, 0.1)
    # time.sleep(0.5)
    # pag.press("enter", 1, 0.1)
    time.sleep(1)
    pag.click(x, y+150, button='right')
    time.sleep(0.5)
    pag.press("down", 10)  # 9 or 10
    pag.press('enter')
    time.sleep(0.1)
    data = pyperclip.paste()
    pag.press('esc')
    return data


def screen_xy_2111(title, acc):
    # kw_window()
    # setMainSearch("2111")
    setAccNum(acc, "2111")
    time.sleep(1)
    # handl(handle)
    time.sleep(0.5)
    pag.press("tab", interval=0.2)
    pag.press('enter')
    hwnd = find_handle_3(title, 10)
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    time.sleep(0.5)
    pag.click(x+30, y+250, button='right')
    time.sleep(0.5)
    pag.press("down", 8)  # 9 or 10
    pag.press('enter')
    time.sleep(0.1)
    pasteTxt = pyperclip.paste()
    pag.press('esc')
    return pasteTxt


def screen_xy_2153(title, acc):
    setAccNum(acc, "2153", 6)
    time.sleep(1)
    hwnd = find_handle_3(title, 24)  # 24 체결기간 시작일
    # mouseClick(hwnd)
    time.sleep(1)
    YesterDay = str(int(today_nowDate()) - 1)
    # typewrite_def("20211101")
    typewrite_def(YesterDay)
    pag.hotkey("shift", "tab")
    pag.hotkey("shift", "tab")
    pag.press('enter')
    time.sleep(0.2)
    # find_handle_3(title, 39)  # 조회
    if check_message() == "[571758] 조회내역이 없습니다.":
        time.sleep(0.5)
        pag.press('esc')
        pag.press('esc')
        return "False"
    else:
        win32gui.SetForegroundWindow(hwnd)
        x, y, x1, y1 = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        time.sleep(0.5)
        pag.click(x+0, y+250, button='right')
        # # print("x/y 클릭")
        time.sleep(0.5)
        pag.press("down", 9)  # 9 or 10
        pag.press('enter')
        time.sleep(0.1)
        pasteTxt = pyperclip.paste()
        pag.press('esc')
        return pasteTxt


def csv_save(fileName, user="kwak", type="무매", accNUM=0):
    text = pyperclip.paste()
    with open(f'stockFile\{user}_{fileName}_{type}_{accNUM}.tsv', 'w', encoding='utf8', newline="") as file:
        file.write(text)
    pyperclip.copy("")


# def save_stockQty_org(user, type, acc):
#     kw_window()
#     sendText(kw_secrch_Edit(), "2150")
#     popUp_2150_SelectAccount(acc)
#     screen_xy()
#     accuntInfo = accunt_info(user, type)
#     accNUM = accuntInfo[0]
#     csv_save("mystockdata", user, type, accNUM)


def save_stockQty(user, type, acc):
    # kw_window()
    # setMainSearch("2150")
    setAccNum(acc, "2150")
    screen_xy()
    csv_save("mystockdata", user, type, acc)


def saveMyDeposit(user, type, acc):
    screen_xy_2111('[2111] 계좌정보(T) - 해외주식 예수금', acc)
    # setAccNum(acc)
    csv_save("MyDeposit", user, type, acc)
    pass


def saveMyRevenue(user, type, acc):
    commd = screen_xy_2153('[2153] 손익/수익률현황(T) - 해외주식 실현손익', acc)
    if commd == "False":
        pyperclip.copy("")
        slackSendMsg(f"금일 {user}의 {type} 수익이 없습니다.")
        csv_save("MyRevenue", user, type, acc)
    else:
        slackSendMsg(f"{user}의 {type} 수익 업데이트 합니다.")
        csv_save("MyRevenue", user, type, acc)


def input2102_Stockname(stock):
    kw_window()
    HG_titleName_1 = win32gui.FindWindow(None, "영웅문Global")
    whnd = win32gui.FindWindowEx(
        HG_titleName_1, None, "MDIClient", None)
    win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
    # # MDIClient_handle(62)
    stockName = find_handle_3('[2102] 해외주식 미니주문', 62)
    mouseClick(stockName)
    pag.typewrite(stock)
    pag.press('enter')
    # slackSendMsg(f"종목 : {stock} 입력완료.")
    print(f"종목 : {stock} 입력완료.")
    return


def input2102_Qty(qty):
    find_handle_3('[2102] 해외주식 미니주문', 83)
    # MDIClient_handle(83)
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
    # MDIClient_handle(78)
    find_handle_3('[2102] 해외주식 미니주문', 78)
    time.sleep(0.3)
    if test == "test":
        handle_32770()
        pag.press('esc')
        print("매수 Test모드")
    elif test == "start":
        handle_32770()
        time.sleep(0.5)
        pag.press('enter')
        time.sleep(0.5)
        if handle_855056() == 0:
            time.sleep(0.5)
            pag.press('enter')
            time.sleep(0.5)
            return "end"
        time.sleep(0.5)
        pag.press('enter')
        time.sleep(0.5)


def input2102_finshsell(test):
    # MDIClient_handle(74)
    find_handle_3('[2102] 해외주식 미니주문', 74)
    time.sleep(0.3)
    if test == "test":
        handle_32770()
        pag.press('esc')
        print("매도 Test모드")
    elif test == "start":
        pag.press('enter')
        time.sleep(0.5)
        handle_32770()
        pag.press('enter')
        time.sleep(0.5)


def check_message():
    time.sleep(0.5)
    check_message_title = win32gui.FindWindow(None, "안내")
    mag = win32gui.FindWindowEx(check_message_title, None, "Static", None)
    button = win32gui.FindWindowEx(check_message_title, None, "Button", None)
    kw_window()
    if check_message_title == 0:
        return 0
    else:
        time.sleep(0.3)
        win32gui.SetForegroundWindow(check_message_title)
        txt = win32gui.GetWindowText(mag)
        mouseClick(button)
        # print(f"check_message_title: {check_message_title}")
        # print(f"mag: {mag}")
        # print(f"button: {button}")
        # return
        # pyperclip.copy(txt)
        return txt


def check_window_org(titleName, x=0, y=0):
    try:
        handle = win32gui.FindWindow(None, titleName)
        win32gui.SetForegroundWindow(handle)
    except:
        # print("윈도우 없음")
        return handle
    else:
        print(handle)
        return handle

    # kw_window()


def check_window(titleName, x=0, y=0):
    try:
        anWindow = auto.WindowControl(
            searchDepth=2, Name=titleName)
        if not anWindow.Exists(10, 1):
            exit(0)
        anWindow.SetActive()
    except:
        logger.info(f"{titleName} : 윈도우 없음")
        return 0
    else:
        return 1234


def input2102_check_accuntNumber(acount=0):
    # MDIClient_handle(15)  # 15 or 10
    # print(child_handles_MDIClient_1)
    # MDIClient_handle_test('[2102] 해외주식 미니주문',18)
    find_handle_3('[2102] 해외주식 미니주문', 16)
    pag.press("up", 10)
    pag.press("down", acount)
    pag.press('enter')


def input2102_check_loc():
    find_handle_3('[2102] 해외주식 미니주문', 67)
    pag.press("up", 8)
    pag.press("down", 3)
    pag.press('enter')


def input2102_check_after():
    find_handle_3('[2102] 해외주식 미니주문', 67)
    pag.press("up", 8)
    pag.press("down", 2)
    pag.press('enter')


# def input2102_check_check(loc=3):
#     if loc == 3:
#         i = 3
#     elif loc == 2:
#         i = 2
#     find_handle_3('[2102] 해외주식 미니주문', 67)
#     pag.press("up", 8)
#     pag.press("down", i)
#     pag.press('enter')


# def input2102_buy(stockname, qty, price, test="test"):
#     time.sleep(0.3)
#     input2102_Stockname(stockname)
#     time.sleep(0.3)
#     input2102_check_loc()
#     time.sleep(0.3)
#     input2102_Qty(qty)
#     time.sleep(0.3)
#     input2102_price(price)
#     input2102_finshBuy(test)  # 실제주문시 필요한
#     time.sleep(0.3)


def input2102_buy_VR(stockname, user="kwak", qty=2, test="test", type="적립식"):
    logger.info("VR 매수시작")
    buy_valueList = buy_values(user, type)
    for i in buy_valueList:
        time.sleep(0.1)
        input2102_Stockname(stockname)  # 2102의 시작
        time.sleep(0.1)
        input2102_check_after()
        time.sleep(0.1)
        input2102_Qty(qty)
        time.sleep(0.1)
        input2102_price(i)
        if input2102_finshBuy(test) == "end":
            slackSendMsg("증거금 부족으로 매수 종료")
            break
        # check_message()
        print("-----------------------")  # 실제주문시 필요한
    print("VR 매수 완료.")


# def input2102_sell(stockname, qty, price, test="test", loc="loc"):
#     time.sleep(0.1)
#     input2102_Stockname(stockname)
#     input2102_Qty(qty)
#     input2102_price(price)
#     input2102_finshsell(test)


def input2102_sell_VR(stockname, user="kwak", qty=2, test="test", type="적립식"):
    slackSendMsg("VR 매도시작")
    sell_valueList = sell_values(user, type)
    # input2102_check_accuntNumber(1)
    # print(buy_valueList)
    if sell_valueList == 0:
        slackSendMsg("매도할 수량이 없습니다.")
        slackSendMsg("VR 매도를 종료 합니다.")
    else:
        for s in sell_valueList:
            # print(buy_valueList)
            time.sleep(0.1)
            input2102_Stockname(stockname)
            input2102_check_after()
            input2102_Qty(qty)
            input2102_price(s)
            input2102_finshsell(test)
            print("-----------------------")  # 실제주문시 필요한
        print("VR 매도완료")


# def startGlobal_org():
#     a = check_window("인증서 선택  (Ver 9.9.8.8)         [AnN2]")
#     b = check_window("영웅문Global Login")
#     c = check_window("영웅문Global")
#     logger.debug(a, b, c)
#     if a > 0:
#         time.sleep(1)
#         kw_window_click("인증서 선택  (Ver 9.9.8.8)         [AnN2]", 0, 0)
#         pag.press("esc")
#         # kw_window_click("영웅문Global Login",0,0)
#         # pag.press("esc")
#         if b > 0:
#             time.sleep(1)
#             kw_window_click("영웅문Global Login", 0, 0)
#             pag.press("esc")
#         else:
#             pass
#     elif b > 0:
#         time.sleep(1)
#         kw_window_click("영웅문Global Login", 0, 0)
#         pag.press("esc")
#     elif c > 0:
#         time.sleep(1)
#         kw_window()
#         pag.hotkey('alt', 'f4')
#         pag.hotkey('enter')
#     else:
#         pass


def closeTitle(title):
    anWindow = auto.WindowControl(
        searchDepth=2, Name=title)
    if not anWindow.Exists(0.3, 1):
        logger.info(f'{title} : 윈도우 없음.')
        # exit(0)
        return 0
    anWindowName = anWindow.Name
    try:
        if title == "영웅문Global":
            # a = pag.getWindowsWithTitle(title)[0]
            if title == anWindowName:
                kw_window()
                pag.hotkey('alt', 'f4')
                time.sleep(1)
                pag.hotkey('enter')
            else:
                pass
        # elif title == "iLabAuto":
        #     # iaList = ["iLabAuto", "iLabAuto 2nd", "iLabAuto 3rd"]
        #     for i in range(1, 6):
        #         ia = auto.PaneControl(searchDepth=1, ClassName="SDL_app")
        #         # anWindow.EditControl(
        #         #     foundIndex=1)
        #         ia.SetActive()
        #         # pag.hotkey("alt", "f4")
        #         # anWindow.SendKeys("{alt}{f4}")
        #         # i = i+1
        else:
            # title == "인증서 선택  (Ver 9.9.8.8)         [AnN2]":
            anWindow.SetActive()
            anWindow.SendKeys("{alt}{f4}")
        # elif title == "영웅문Global Login":
        #     anWindow.

    except:
        logger.info(f"{title} : 윈도우 없음.(에러)")


def closeLotto():
    i = 1
    try:
        while i < 7:
            pag.getWindowsWithTitle("iLabAuto")[0].close()
            print(f"{i}lotto 닫기 성공")
            time.sleep(2)
            i = i+1
    except:
        pass


def startGlobal():
    closeTitle("인증서 선택  (Ver 9.9.8.8)         [AnN2]")
    closeTitle("영웅문Global Login")
    closeTitle("영웅문Global")
    closeLotto()
    # closeTitle("iLabAuto")
    # closeTitle("iLabAuto")
    # closeTitle("iLabAuto")
    # closeTitle("iLabAuto")
    # closeLotto()
    # kw_Login()


# def find_handle_2_test(title):  # 62는 2102의 종목??
#     # child_txt_MDIClient = []
#     HG_titleName = win32gui.FindWindow(None, "영웅문Global")
#     whnd = win32gui.FindWindowEx(
#         HG_titleName, None, "MDIClient", None)
#     a = win32gui.GetWindowText(whnd)
#     win32gui.EnumChildWindows(whnd, all_ok_MDIClient, None)
#     print(a)


# def try_while(module):
#     i = 0
#     while i < 10:
#         i = i+1
#         try:
#             result = module
#             return result
#         except Exception as e:
#             logger.debug(str(e))
#             logger.debug(f"에러로 반복하는 횟수 {i}")
#             module


def getText(accHendle):
    check_message_title = win32gui.FindWindow(None, "안내")
    print(accHendle)
    mag = win32gui.FindWindowEx(accHendle, None, None, None)
    txt = win32gui.GetWindowText(accHendle)
    print(txt)


# def popUp_2150_SelectAccount_오리지널(accNum):
#     kw_window()
#     # kw_secrch = kw_secrch_Edit()
#     # try_while(sendText(kw_secrch, "2150"))
#     # time.sleep(0.5)
#     accHendle = find_handle_3('[2150] 계좌정보(T) - 해외주식 실시간잔고', 32)  # 계좌클릭
#     getText(accHendle)
#     time.sleep(1)
#     pag.press("up", 10)
#     pag.press("down", accNum)
#     time.sleep(0.5)
#     pag.press('enter')
#     # time.sleep(0.5)
#     # pag.press("esc", 2)


def popUp_2150_SelectAccount(accNum):
    kw_window()
    pag.press("up", 10)
    pag.press("down", accNum)
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)


# def SelectAccount(accNum):
#     kw_window()
#     pag.press("up", 10)
#     pag.press("down", accNum)
#     time.sleep(0.5)
#     pag.press('enter')
#     time.sleep(0.5)


if __name__ == '__main__':
    save_screenshot("kwak")
    # startGlobal()
    # save_stockQty("kwak", "무매", "45")
    # saveMyDeposit("kwak", "무매", "45")
    # mouseClick("13438516")
    # print(kw_window())
    # screen_xy_2153('[2153] 손익/수익률현황(T) - 해외주식 실현손익', 4)
    # popUp_2150_SelectAccount_오리지널(2)
    # pag.hotkey("shift", "tab")
    # screen_xy_2111('[2111] 계좌정보(T) - 해외주식 예수금')
    # saveMyRevenue("kwak", "TLP2", 4)
    # a = check_message()
    # print(a)
    # kw_window()
    # saveMyRevenue("kwak", "무매", 0)
    # pyperclip.copy("")
    # a = pyperclip.paste()
    # print(a)
    # print(today_nowDate())
    # popUp_2150_SelectAccount(0)
    # screen_xy_2153('[2153] 손익/수익률현황(T) - 해외주식 실현손익', 0)
    # save_stockQty("kwak", "무매")
    # a = date.today()
    # screen_xy()
    # pass
