from def_ui import setMainSearch
# from def_kw import startGlobal
import uiautomation as auto
import pyautogui as pag
import time
import csv
from slack_engin import *

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
    # logger.info(getAccValue)
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
        logger.info(f"{acc}는 요청한 계좌번호임.")
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


def getRevenueAmount(i):
    revenueFile = f"D:\TaiCloud\Documents\Project\Lotto\stockFile\kwak_MyRevenue_{i}.tsv"
    f = open(revenueFile, 'r', encoding='utf-8')
    rdr = csv.reader(f, delimiter='\t')
    r = list(rdr)
    revenues = 0
    try:
        for i in range(1, 20):
            # revenue = float(r[i][9])
            revenue = str(r[i][9])
            revenue = revenue.replace(",", "")
            # print(revenue)
            revenues = float(revenues) + float(revenue)
    except IndexError:
        revenues = round(revenues, 2)
        if revenues <= 0:
            return 0
        else:
            return revenues
        # pass


def def_accNumEdit_info():
    winControl = auto.WindowControl(
        searchDepth=2, Name='안내')
    text1 = "[502409] [502409]동일계좌로의 대체입니다.."
    text2 = "[506503] [506503]출금가능금액이 부족합니다."
    text3 = "[857185] 처리불가(이체/대체 불가시간입니다(HTS마감).)"
    textName = winControl.TextControl(foundIndex=1).Name
    if textName == text1:
        logger.info("동일계좌")
        time.sleep(0.3)
        pag.press("esc")
        pass
    elif textName == text2:
        logger.info("출금계좌에 잔액 부족")
        time.sleep(0.3)
        pag.press("esc")
        pass
    elif textName == text3:
        logger.info("이체/대체 불가시간입니다(HTS마감)")
        time.sleep(0.3)
        # pag.press("enter")
        pag.press("esc")
        pass
    # except LookupError:
    #     pass
    # return accNumEdit


def closeTitle(title):
    try:
        pag.getWindowsWithTitle(title)[0].close()
    except IndexError:
        pass


def main():
    setMainSearch("3135")
    setAccNum_3135("82", 5)  # 받는계좌 세팅
    n = ["무매_45", "ava1_24", "ava2_23", "ava3_62",
         "TLP1_04", "TLP2_02", "TLP3_09"]
    # n = ["무매_45"]
    for i in n:
        try:
            acc = i[-2:]
            logger.info(acc)
            amounts = getRevenueAmount(i)
            if amounts == 0:
                logger.info(f"{i}은 수익 없음.")
                pag.getWindowsWithTitle("안내")[0].close()
            else:
                setAccNum_3135(acc, 7)  # 보내는 계좌 세팅
                logger.info(f"{i}의 일 수익은 : {amounts}")
                pag.press("tab")
                pag.typewrite(str(amounts))
                # pag.typewrite("1231321")
                time.sleep(0.3)
                pag.press("tab")
                pag.press("enter")
                closeTitle("안내")
                # check안내 함수를 응용하자.
                # def_accNumEdit_info()
        except LookupError:
            pass


if __name__ == '__main__':
    # closeTitle("안내")
    main()
    # a = getRevenueAmount("무매_45")
    # print(a)
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
    # def_accNumEdit_info()
    pass
