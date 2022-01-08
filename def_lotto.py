import win32con
import win32gui
import win32api
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import time
from datetime import datetime
import pandas as pd
from pywinauto.application import Application
from slack_engin import *
import def_xyp as dx
from def_kw import kw_window, check_window
from passdoc import pw
# from def_ui import closeLotto
import subprocess
# from typing_extensions import Unpack
import uiautomation as auto
# from def_loggin import __get_logger
# logger = __get_logger()

pw = pw.passWord()
# import sys
# import os
# import main


def today_nowDate():
    datetime.today()
    today_now_date = datetime.today().strftime("%Y%m%d")
    return today_now_date


def typewrite_def(typewrite, commend=0):
    pag.typewrite(typewrite, interval=0)
    if commend == 0:
        time.sleep(0.5)
        return
    else:
        time.sleep(0.3)
        print(commend)


def winActivate(winName, l=0, r=0):
    i = 0
    while i < 10:
        try:
            i = i + 1
            winHandle = win32gui.FindWindow(None, winName)
            logger.info(f"{winName} : {winHandle}")
            if winHandle > 0:
                win = gw.getWindowsWithTitle(winName)[0]
                time.sleep(0.3)
                win.activate()
                win_left = win.left
                win_top = win.top
                pag.click(win_left+l, win_top+r)
                return win_left, win_top
            else:
                time.sleep(1)
                logger.info(f"{winName} : 없음")
                continue
        except:
            logger.info(f"{win} : 창 없음")
            pass


def winActivate_debug(winName, l, r):
    time.sleep(1)
    win = gw.getWindowsWithTitle(winName)[0]
    if win.isActive == False:
        pywinauto.application.Application().connect(
            handle=win._hWnd).top_window().set_focus()
    win.activate()  # 윈도우 활성화
    time.sleep(0.3)
    win_left = win.left
    win_top = win.top
    # pag.moveRel(win.left+l, win.top+r)
    # pag.moveTo(win.left+l, win.top+r)
    pag.click(win.left+l, win.top+r)
    print(win_left, win_top)
    return win_left, win_top


def winActivate_moveto(winName, l, r):
    time.sleep(1)
    win = gw.getWindowsWithTitle(winName)[0]
    # if win.isActive == False:
    #     pywinauto.application.Application().connect(
    #         handle=win._hWnd).top_window().set_focus()
    win.activate()  # 윈도우 활성화
    # print(win.left)
    # print(win.top)
    # time.sleep(0.3)
    # pag.move(win.left+l, win.top+r)
    # pag.click(win.left+l, win.top+r)


def check_message_login():
    title_9988 = "간편인증 인증서 선택 (Ver 1.1.0.0)  [AnN]"
    time.sleep(0.5)
    check_message_title = win32gui.FindWindow(None, title_9988)
    mag = win32gui.FindWindowEx(check_message_title, None, "Edit", None)

    if check_message_title == 0:
        return "False"
    else:
        mouseClick(mag)
        return "True"


def kw_Login(user="kwak", xy=2):
    subprocess.Popen(r'C:\KiwoomGlobal\bin\NFStarter.exe')
    time.sleep(5)
    anWindow = auto.WindowControl(
        searchDepth=2, Name='인증서 선택  (Ver 9.9.8.8)         [AnN2]')
    if not anWindow.Exists(10, 1):
        print('Can not find 영웅문 인증서 window')
        exit(0)
    anWindow.SetActive()
    time.sleep(5)
    if user == "kwak":
        pag.press("tab", 4)
        pag.press("down")
        pag.press("tab", 4)
        pag.press("down")
    elif user == "lee":
        pag.press("tab", 4)
        pag.press("down")
    elif user == "han":
        pass
    time.sleep(0.5)
    pag.write("rhkr5241^^")
    anWindow.ButtonControl(Name='인증서 선택(확인)').Click()
    msg = user + " 로그인 하였습니다."
    return slackSendMsg(msg)


# def openLoto_org(user="kwak", x=1, tradetype="아바타"):
#     time.sleep(20)
#     checkLottoOpen()
#     # while True:
#     try:
#         program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe"
#         Application(backend="uia").start(program_file)
#         # win_left, win_top = winActivate("iLabAuto", 30, 675)
#         time.sleep(10)
#         winActivate("iLabAuto", 0, 0)  # 만약 에러가 발생하면, 예외처리로 다시 생각해보자.
#     except:
#         slackSendMsg("Lotto 실행시 문제 발생 다시 실행.")
#     win_left, win_top = pag.position()
#     dx.movingAndClick(win_left+300, win_top+738)  # 동의
#     dx.movingAndClick(win_left+485, win_top+607, 3)  # 동의 accpet
#     time.sleep(1)
#     logger.info("start 클릭")
#     if user == "kwak":
#         pass
#     elif user == "han":
#         dx.movingAndClick(win_left+223, win_top+620)  # select 클릭
#         time.sleep(2)
#         dx.movingAndClick(win_left+245, win_top+390)  # 3번클릭
#         time.sleep(1)
#     dx.movingAndClick(win_left+500, win_top+736)  # start
#     time.sleep(0.5)
#     dx.movingAndClick(win_left+485, win_top+630)  # start accpet
#     # print(pag.position())
#     time.sleep(1)
#     dx.movingAndClick(win_left, win_top)  # 임시
#     slackSendMsg("Loto 프로그램을 실행했습니다.")


def openLoto(user="kwak", x=1, tradetype="아바타"):
    # time.sleep(20)
    closeLotto()
    if user == "kwak":
        logger.info("start 클릭")
        program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -ib1=1 -close=2"
        Application(backend="uia").start(program_file)
        time.sleep(250)
    elif user == "han":
        program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -ib3=1 -close=2"
        Application(backend="uia").start(program_file)
        time.sleep(250)
    elif user == "lee":
        program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -ib4=1 -close=2"
        Application(backend="uia").start(program_file)
        time.sleep(250)
    slackSendMsg("Loto 프로그램을 실행했습니다.")


def select_test():
    winActivate("iLabAuto", 0, 0)
    win_left, win_top = pag.position()
    dx.movingAndClick(win_left+223, win_top+620)  # select 클릭
    time.sleep(2)
    dx.movingAndClick(win_left+245, win_top+390)  # 3번클릭

# def kw_window(l=0, r=0):
#     # pag.press("esc", 5)
#     time.sleep(0.3)
#     kw_win = gw.getWindowsWithTitle("영웅문Global")[0]
#     if kw_win.isActive == False:
#         pywinauto.application.Application().connect(
#             handle=kw_win._hWnd).top_window().set_focus()
#     kwActivage = kw_win.activate()  # 윈도우 활성화
#     time.sleep(0.3)
#     return kwActivage,kw_win

# def kw_window(l=0, r=0):
#     try:
#         # pag.press("esc", 5)
#         time.sleep(0.3)
#         # kw_win = gw.getWindowsWithTitle("영웅문Global")[0]
#         HG_titleName = 0
#         HG_titleName = win32gui.FindWindow(None, "영웅문Global")
#         logger.debug(f"HG_titleName: {HG_titleName}")
#         win32gui.SetForegroundWindow(HG_titleName)
#         # print(kw_win,HG_titleName)
#         # if kw_win.isActive == False:
#         #     pywinauto.application.Application().connect(
#         #         handle=kw_win._hWnd).top_window().set_focus()
#         # kwActivage = kw_win.activate()  # 윈도우 활성화
#         time.sleep(0.3)
#         # return kwActivage
#         # pag.click(kw_win.left+l, kw_win.top+r)
#     except:
#         logger.info("kw_window() 에러")
#         pass


def check_message_lotto():
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


def mouseClick(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    # time.sleep(0.2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)


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


def ilab_window(l=0, r=0):
    # pag.press("esc", 5)
    time.sleep(0.3)
    kw_win = gw.getWindowsWithTitle("iLabAuto")[0]
    if kw_win.isActive == False:
        pywinauto.application.Application().connect(
            handle=kw_win._hWnd).top_window().set_focus()
    kwActivage = kw_win.activate()  # 윈도우 활성화
    time.sleep(0.3)
    return kw_win


# "iLabAuto 2nd"
# "iLabAuto 3rd"
# "iLabAuto 4th"

# def closeLoto():
#     lotoList = ["iLabAuto", "iLabAuto 2nd", "iLabAuto 3rd", "iLabAuto 4th"]
#     for loto in lotoList:
#         if check_window(loto) > 0:
#             try:
#                 # check_window(loto) == None
#                 close_Loto(loto)
#             except:
#                 print("닫혀있다.")
#         else:
#             pass


def waitApp(title):
    Application().connect(title=title, timeout=20)


def KW_Win(l, r):
    kw_win = gw.getWindowsWithTitle("영웅문Global")[0]
    if kw_win.isActive == False:
        pywinauto.application.Application().connect(
            handle=kw_win._hWnd).top_window().set_focus()
    kw_win.activate()  # 윈도우 활성화
    print("영웅문Global : ")
    time.sleep(0.3)
    pag.click(kw_win.left+l, kw_win.top+r)


def kw_close():
    check_window("영웅문Global")
    anWindow = auto.WindowControl(searchDepth=2, Name="영웅문Global")
    anWindow.SetActive()
    anWindow.GetWindowPattern().Close()
    time.sleep(0.3)
    pag.press('enter')


def check_windowLoto(loto):
    handle_loto = win32gui.FindWindow(None, loto)
    # if handle_loto == 0:
    #     handle_loto = win32gui.FindWindow(None, "iLabAuto 2nd")
    #     if handle_loto == 0:
    #         handle_loto = win32gui.FindWindow(None, "iLabAuto 3rd")
    #         if handle_loto == 0:
    #             handle_loto = win32gui.FindWindow(None, "iLabAuto 4th")
    return handle_loto


def check_windowLoto_after():
    handle_loto = win32gui.FindWindow(None, "iLabAuto 2nd")
    return handle_loto


# "iLabAuto 2nd"
# "iLabAuto 3rd"
# "iLabAuto 4th"


def checkLottoOpen():
    windowLoto = check_windowLoto("iLabAuto")
    # while windowLoto > 0:
    if windowLoto == 0:
        logger.info("실행된 Lotto 없음")
        pass
        # break
    else:
        # win32gui.SetForegroundWindow(windowLoto)
        # check_window("iLabAuto", 0, 0)
        slackSendMsg("실행전 Lotte가 Open되어있어 우선 종료합니다.")
        closeLotto("iLabAuto")
        # windowLoto = check_windowLoto()


def startAvatar():
    checkLottoOpen()
    try:
        program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe"
        Application(backend="uia").start(program_file)
        # win_left, win_top = winActivate("iLabAuto", 30, 675)
        time.sleep(10)
        winActivate("iLabAuto", 0, 0)  # 만약 에러가 발생하면, 예외처리로 다시 생각해보자.
        win_left, win_top = pag.position()
        dx.movingAndClick(win_left+36, win_top+52)  # select 클릭
        time.sleep(1)
        dx.movingAndClick(win_left+45, win_top+290)  # 3번클릭
        time.sleep(1)
        dx.movingAndClick(win_left+500, win_top+580)  # start 클릭
        time.sleep(1)
        dx.movingAndClick(win_left+480, win_top+630)  # accept 클릭
        logger.info(slackSendMsg("아바타를 실행하였습니다."))

    except:
        slackSendMsg("Lotto 실행시 문제 발생 다시 실행.(아바타)")


def activeLotto():
    pag.getWindowsWithTitle("iLabAuto")[0].close()
    time.sleep(0.2)


if __name__ == '__main__':
    # try:
    # pag.getWindowsWithTitle("안내")[0].close()
    # # winActivate('iLabAuto')
    closeLotto()
    # checkLottoOpen()
    # activeLotto()
    # openLoto()
    # closeLotto()
    # kw_close()
    # kw_window()
    # pag.hotkey('alt', 'f4')
    # pag.hotkey('enter')
    # program_file = r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -av1=1"
    # Application(backend="uia").start(program_file)
    # closeLoto()

    # a = check_windowLoto("iLabAuto  ")
    # print(a)
    # startAvatar()
    # startAvatar()
    # checkLottoOpen()
    # # winActivate("iLabAuto",0,0)
    # pass
    # kw_Login()
    # x,y = winActivate("iLabAuto",0,0)
    # print(pag.position())
    # x1,y1 = pag.position()
    # pag.moveTo(x1+307,y1+737)
    # pag.click()
    # pag.click(x+307,y+736)
    # openLoto("han",0)
    # closeLoto("iLabAuto 2nd")

    # kw_Login_2("han")
    # close_Loto()
    # checkLoto()
    # closeLoto()
    # sleep5m()
    # kw_close()
    # today_nowDate()
    # a = check_message()
    # print(a)
    # if a == None:
    #     print("무한매수를 완료하였습니다.")
    # else:
    #     print(a)
    # sleep5m(1)
    # try:
    #     kw_window()
    # except:
    #     print('Hello Error!')
    # kw_Login_2()
    # ;
    # kw_close()
    #     pass
    # except:
    #     # logging.error(traceback.format_exc())
    #     pass
