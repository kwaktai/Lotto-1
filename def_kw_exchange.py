from def_ui import setMainSearch
# from def_kw import kw_window
import uiautomation as auto
import pyautogui as pag
import time

# 받는 계좌 4
# 보내는계좌 7


def def_accNumEdit_3135(ec):
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.EditControl(foundIndex=ec)
    # print(accNumEdit)
    return accNumEdit


def getAccNumber_3135(ec):
    accNumEdit_2150 = def_accNumEdit_3135(ec)
    getAccValue = accNumEdit_2150.GetValuePattern().Value
    getAccValue = getAccValue[-2:]
    print(getAccValue)
    return getAccValue


def moveAccNumUp_3135(count, ec):
    accNumEdit_2150 = def_accNumEdit_3135(ec)
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{up}')
    pass


def moveAccNumDown_3135(count, ec):
    accNumEdit_2150 = def_accNumEdit_3135(ec)
    for i in list(range(0, count)):
        accNumEdit_2150.SendKeys('{down}')
    pass


def setAccNum_3135(acc, ec):
    numList = ['45', '49', '53', '04',
               '02', '09', '24', '23', '62', '82']
    nowAccNum = getAccNumber_3135(ec)
    while acc == nowAccNum:
        print(f"{acc}는 원하는 계좌번호임.")
        break
    else:
        def_accNumEdit_3135(ec).SetFocus()
        selectAccNumIndex = numList.index(acc)
        nowAccNumIndex = numList.index(nowAccNum)
        indexValue = selectAccNumIndex - nowAccNumIndex
        if indexValue > 0:
            moveAccNumDown_3135(indexValue, ec)
        else:
            moveAccNumUp_3135(indexValue*-1, ec)
            pass


def setReceiverAcc():
    setAccNum_3135("82", 4)


def getRevenueAmount(i):
    revenueFile = f"D:\TaiCloud\Documents\Project\Lotto\stockFile\kwak_MyRevenue_{i}.tsv"
    acc = i[-2:]
    # print(revenueFile)
    amount = "123422"
    return acc, amount


def setAmount(amount):
    winControl = auto.PaneControl(searchDepth=5, ClassName='AfxWnd110')
    winControl.MiddleClick()
    time.sleep(0.3)
    pag.typewrite(amount)


def setBottom():
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    winControl.SetActive()
    # notepadWindow = auto.WindowControl(searchDepth=1, ClassName='Notepad')
    winControl.ButtonControl(searchDepth=3, Name=">>").Click()
    # Name = ">>"
#


def main():
    setMainSearch("3135")
    setAccNum_3135("82", 5)  # 받는계좌 세팅
    n = ["무매_45", "ava2_23", "ava3_62", "TLP1_04", "TLP2_02", "TLP3_09"]
    # n = ["무매_45"]
    for i in n:
        acc, amount = getRevenueAmount(i)
        setAccNum_3135(acc, 7)  # 보내는 계좌 세팅
        pag.press("tab")
        pag.typewrite(amount)
        time.sleep(0.3)
        pag.press("enter")
        # setAmount(amount)


if __name__ == '__main__':
    # setBottom()
    # kw_window()
    # setMainSearch("3135")
    # setAmount("2132")
    # getAmount()
    # setMainSearch("3135")
    # setAccNum_3135("09", 7)
    # setAccNum_3135("82", 5)
    # getAccNumber_3135(5)
    # print(setAccNum_3135("82", "4"))

    main()
    pass
