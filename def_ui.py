# -*- coding: utf-8 -*-
import subprocess
import uiautomation as auto

import time
import pyautogui as pag

# zoom.SetTopmost(True)  # 화면고정
# zoom.SetTopmost(False)  # 화면고정

numList = ['45', '49', '53', '04',
           '02', '09', '24', '23', '62', '82']


def printControls(items):
    for i in items:
        print(i)


def setEsc():
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    edit = winControl.EditControl(foundIndex=1)
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')


# def getAccNumbers():
#     accNumEdit = get_NFHeroMainClass(2)

#     def getAccNum():
#         getAccValue = accNumEdit.GetValuePattern().Value
#         getAccValue = getAccValue[-2:]
#         return getAccValue

#     def _setAccNum():
#         def setNumUp():
#             for i in list(range(0, 10)):
#                 accNumEdit.SendKeys('{up}')
#         setNumUp()
#         accNumList = []
#         for i in list(range(0, 10)):
#             accNumList.append(getAccNum())
#             accNumEdit.SendKeys('{down}')
#         print(accNumList)
#         return accNumList
#     return _setAccNum()
#     # print(getAccNum())


def setMainSearch(menuNum):
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    winControl.SetActive()
    setEsc()
    edit = winControl.EditControl(foundIndex=1)
    # print(edit.GetValuePattern().Value)  # 계좌번호 가져왔다!
    editTarget = edit.GetValuePattern()
    editTarget.SetValue(menuNum)
    edit.SendKeys('{Enter}')


def checkAccNow():
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    edit = winControl.EditControl(foundIndex=1)


def getAccNumber(menuNum="2150", num=2):
    setMainSearch(menuNum)
    accNumEdit = get_NFHeroMainClass(num)
    getAccValue = accNumEdit.GetValuePattern().Value
    getAccValue = getAccValue[-2:]
    return getAccValue


def moveAccNumUp(count, num=2):
    accNumEdit_2150 = get_NFHeroMainClass(num)
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{up}')
    pass


def moveAccNumDown(count, num=2):
    accNumEdit_2150 = get_NFHeroMainClass(num)
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{down}')
    pass


# numList = ['45', '49', '53', '04',
#            '02', '09', '24', '23', '62', '82']


def setAccNum(acc, menuNum, num=2):
    try:
        nowAccNum = getAccNumber(menuNum, num)
        while acc == nowAccNum:
            print(f"{acc}는 원하는 계좌번호임.")
            break
        else:
            selectAccNumIndex = numList.index(acc)
            nowAccNumIndex = numList.index(nowAccNum)
            indexValue = selectAccNumIndex - nowAccNumIndex
            if indexValue > 0:
                moveAccNumDown(indexValue)
            else:
                moveAccNumUp(indexValue*-1)
                pass
    except LookupError:
        print("2150 창이 없습니다.실행합니다.")


def infoList(user):
    userInfo = {"kwak": {"무매": "45",  "ava1": "24",
                         "ava2": "23", "ava3": "62", "TLP1": "04", "TLP2": "02", "TLP3": "09"}}
    listKey = list(userInfo['kwak'])
    listValue = list(userInfo['kwak'].values())
    return listKey, listValue


def saveStock(user):
    listKey = infoList(user)[0]
    listValue = infoList(user)[1]
    print(len(listKey))
    for i in range(len(listKey)):
        print(listKey[i])
        print(listValue[i])


def closeLotto():
    a = pag.getWindowsWithTitle("iLabAuto")[0]
    a.close()


def kw_window(l=0, r=0):
    try:
        anWindow = auto.WindowControl(
            searchDepth=2, Name='영웅문Global')
        if not anWindow.Exists(0.3, 1):
            print('Can not find 영웅문Global')
            # exit(0)
            return 0
        anWindow.SetActive()
        return 1
    except:
        # print("asdf")
        pass


def secletTab(tabName):
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.TabItemControl(
        foundIndex=1, Name=tabName)
    if not accNumEdit.Exists(0.2, 1):
        exit(0)
    accNumEdit.GetSelectionItemPattern().Select()
    print(f"{tabName}: Tab click")


def secletEventEnter():
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.WindowControl(foundIndex=1, Name="확인")
    if not accNumEdit.Exists(0.2, 1):
        accNumEdit = winControl.WindowControl(foundIndex=1, Name="안내")
        if not accNumEdit.Exists(0.2, 1):
            exit(0)
        else:
            print(accNumEdit.TextControl(foundIndex=1).Name)
            accNumEdit.SendKeys('{enter}')
    else:
        print(accNumEdit.TextControl(foundIndex=1).Name)
        accNumEdit.SendKeys('{enter}')


def set2102_Buy(stockname, user, qty, price, test, locType, acc):
    # kw_window()
    # setAccNum(acc, "2102")
    secletTab("매수")
    set_NFHeroMainClass_WriteValues(4, stockname)
    set_NFHeroMainClassSetLOC(5, locType)
    set_NFHeroMainClass_WriteValues(7, qty)
    set_NFHeroMainClass_WriteValues(6, price)
    pag.press("enter")
    secletEventEnter()
    if test == "test":
        pag.press("esc")
    else:
        pag.press("enter")
    secletEventEnter()


def set2102_Sell(stockname, user, qty, price, test, locType, acc):
    # kw_window()
    # setAccNum(acc, "2102")
    secletTab("매도")
    time.sleep(1)
    set_NFHeroMainClassSetLOC(5, locType, trade="매도")
    set_NFHeroMainClass_WriteValues(5, stockname)
    set_NFHeroMainClass_WriteValues(8, qty)
    set_NFHeroMainClass_WriteValues(7, price)
    pag.press("enter")
    secletEventEnter()
    if test == "test":
        pag.press("esc")
    else:
        pag.press("enter")
    secletEventEnter()


def get_NFHeroMainClass(num):
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.EditControl(foundIndex=num)
    return accNumEdit


def set_NFHeroMainClass_WriteValues(num, value=0):
    accNumEdit = get_NFHeroMainClass(num)
    editTarget = accNumEdit.GetValuePattern()
    editTarget.SetValue(value)
    # editTarget.SendKey('{down}')


def set_NFHeroMainClassSetLOC(num, LocType="LOC", trade="매수"):
    secletTab(trade)
    accNumEdit = get_NFHeroMainClass(num)
    editTarget = accNumEdit.GetValuePattern()
    nowLocType = editTarget.Value
    numList = {"LOC": 3, "AFTER지정": 2}
    # try:
    while LocType == nowLocType:
        break
    else:
        moveAccNumUp(5, 5)
        moveAccNumDown(numList[LocType], 5)
        secletTab(trade)
    # except LookupError:
        # pass


if __name__ == '__main__':
    # saveStock('kwak')
    # set_NFHeroMainClass_WriteValuesDocumentControl(5)
    # moveAccNumDown(2, 5)
    # set_NFHeroMainClassSetLOC(5, "AFTER지정")
    # getAccNumbers()\se
    # get_NFHeroMainClass(6)
    # set_NFHeroMainClassSetLOC(6, "LOC")
    # set2102_Sell("TQQQ", "kwak", "34", "150.21", "start", "LOC", "82")
    # secletEventEnter()
    # selsetTab("실시간잔고")
    set2102_Buy("TQQQ", "kwak", "34", "160", "start", "LOC", "82")
    # warningMsg()
    # set_NFHeroMainClass_WriteValues(7, "111")
    # set_NFHeroMainClass_WriteValues(5, "시장가")
    # setAccNum_2102("82")
    # print(a)
    # setAccNum("62")
    # consoleWindow = auto.GetConsoleWindow()
    # zoom_test()
    # test_global()
    # moveAccNum()
    # setAccNum("82")
    # kw_Login_2()
    # main_ui()
    # a = getAccNumber_2153()
    # print(a)
    # setMainSearch("2153")
    # setAccNum("62")
