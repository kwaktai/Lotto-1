# -*- coding: utf-8 -*-
import subprocess
import uiautomation as auto
import time
import pyautogui as pag


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


def def_accNumEdit_2150():
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.EditControl(foundIndex=2)
    return accNumEdit


def def_accNumEdit_2153():
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.EditControl(foundIndex=6)
    getAccValue = accNumEdit.GetValuePattern().Value
    # print(getAccValue)
    return accNumEdit


# accNumEdit_2150 = def_accNumEdit_2150()
# accNumEdit_2153 = def_accNumEdit_2153()


def getAccNumbers():
    accNumEdit_2150 = def_accNumEdit_2150()
    # winControl = auto.WindowControl(
    #     searchDepth=1, ClassName='_NFHeroMainClass')
    # accNumEdit = winControl.EditControl(foundIndex=2)

    def getAccNum():
        # winControl = auto.WindowControl(
        #     searchDepth=1, ClassName='_NFHeroMainClass')
        # accNumEdit = winControl.EditControl(foundIndex=2)
        # zoom.SetTopmost(True)  # 화면고정
        # zoom.SetTopmost(False)  # 화면고정
        getAccValue = accNumEdit_2150.GetValuePattern().Value
        getAccValue = getAccValue[-2:]
        # print(getAccValue)  # 계좌번호 가져왔다!
        return getAccValue

    def checkAccNum():
        # winControl = auto.WindowControl(
        #     searchDepth=1, ClassName='_NFHeroMainClass')
        # accNumEdit = winControl.EditControl(foundIndex=2)
        def setNumUp():
            for i in list(range(0, 10)):
                accNumEdit_2150.SendKeys('{up}')
        setNumUp()
        accNumList = []
        for i in list(range(0, 10)):
            accNumList.append(getAccNum())
            accNumEdit_2150.SendKeys('{down}')
        print(accNumList)
        return accNumList
    return checkAccNum()
    # print(getAccNum())


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


def main_ui():
    setMainSearch("2150")
    # setAccNum("45")


def checkAccNow():
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    edit = winControl.EditControl(foundIndex=1)


def getAccNumber(menuNum="2150"):
    setMainSearch(menuNum)
    accNumEdit_2150 = def_accNumEdit_2150()
    getAccValue = accNumEdit_2150.GetValuePattern().Value
    getAccValue = getAccValue[-2:]
    return getAccValue


def getAccNumber_2153(menuNum="2153"):
    setMainSearch(menuNum)
    accNumEdit_2153 = def_accNumEdit_2153()
    getAccValue = accNumEdit_2153.GetValuePattern().Value
    getAccValue = getAccValue[-2:]
    return getAccValue


def moveAccNumUp(count):
    accNumEdit_2150 = def_accNumEdit_2150()
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{up}')
    pass


def moveAccNumDown(count):
    accNumEdit_2150 = def_accNumEdit_2150()
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{down}')
    pass


# numList = ['45', '49', '53', '04',
#            '02', '09', '24', '23', '62', '82']


def setAccNum(acc, menuNum):
    numList = ['45', '49', '53', '04',
               '02', '09', '24', '23', '62', '82']
    try:
        # setMainSearch("2150")
        nowAccNum = getAccNumber(menuNum)
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


def setAccNum_2153(acc, menuNum):
    numList = ['45', '49', '53', '04',
               '02', '09', '24', '23', '62', '82']
    nowAccNum = getAccNumber_2153(menuNum)
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


def infoList(user):
    userInfo = {"kwak": {"무매": "45",  "ava1": "24",
                         "ava2": "23", "ava3": "62", "TLP1": "04", "TLP2": "02", "TLP3": "09"}}
    # userInfo = {"kwak": {"무매": "45", "적립식": "49", "거치식": "53", "ava1": "24",
    #                      "ava2": "23", "ava3": "62", "TLP1": "04", "TLP2": "02", "TLP3": "09"}}
    listKey = list(userInfo['kwak'])
    listValue = list(userInfo['kwak'].values())
    return listKey, listValue


def saveStock(user):
    listKey = infoList(user)[0]
    listValue = infoList(user)[1]
    # listKey = listKey.index("무매")
    # listValue = listValue[listKey]
    print(len(listKey))

    for i in range(len(listKey)):
        print(listKey[i])
        print(listValue[i])


def closeLotto():
    a = pag.getWindowsWithTitle("iLabAuto")[0]
    a.close()


if __name__ == '__main__':
    # saveStock('kwak')
    closeLotto()
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
    pass
