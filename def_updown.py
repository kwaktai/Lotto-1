import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
# from slack_engin import *
# from def_kw import setAccNum
# import def_ui
# import time
# import csv
# import def_kw
import uiautomation as auto
import pyautogui as pag
from def_ui import setAccNum


scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'D:\TaiCloud\Documents\Project\stockRpawin_kw\jsop_Key\spreadsheettopython-320114-0340a7e3e1da.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_udt = "https://docs.google.com/spreadsheets/d/1WfoW90rSo0gbPZ7fuMqvmrgFDZWXTfkdbcm1th-ugc4/edit#gid=2078891690"
doc = gc.open_by_url(spreadsheet_udt)
worksheet_order = doc.worksheet('거래시트')  # 시트선택
# worksheet_order.acell("C2").value


def replaceDollar(setList):
    for i in range(len(setList)):
        setList[i] = setList[i].replace("$", "")
    return setList


def sellValueList(i):
    # sell_valuelist = []
    sell_valuelist = worksheet_order.col_values(i+1)  # 열읽기
    sell_valuelist = sell_valuelist[1]
    sell_valuelist = sell_valuelist.replace("$", "")
    sell_qytlist = worksheet_order.col_values(i+2)  # 열읽기
    sell_qytlist = sell_qytlist[1]
    sellList = {}
    sellList[sell_valuelist] = sell_qytlist
    return sellList


def tradeList(num):
    if num == 1:
        i = 12
    elif num == 2:
        i = 16
    stockName = worksheet_order.col_values(i)
    stockName = stockName[0]
    buy_valuelist = []
    buy_valuelist = worksheet_order.col_values(i+1)  # 열읽기
    buy_valuelist = buy_valuelist[2:13]
    buy_valuelist = replaceDollar(buy_valuelist)
    buy_qtylist = worksheet_order.col_values(i+2)
    buy_qtylist = buy_qtylist[2:13]
    buyList = {}
    for dic in range(len(buy_qtylist)):
        buyList[buy_valuelist[dic]] = buy_qtylist[dic]
    sellList = sellValueList(i)
    return stockName, sellList, buyList


winControl = auto.WindowControl(
    searchDepth=1, Name='영웅문Global')


def foundWct():
    # winControl = auto.WindowControl(
    #     searchDepth=1, Name='영웅문Global')
    winControl.SetActive()
    for i in range(1, 50):
        try:
            wct = winControl.EditControl(foundIndex=i)
            # wct.Click
            print(f"{i} : {wct}")
        except:
            print(f"{i}는 에러")


def clickWct(i):
    if i == "매수":
        r = 27
    elif i == "매도":
        r = 28
    # winControl = auto.WindowControl(
    #     searchDepth=1, Name='영웅문Global')
    winControl.SetActive()
    winControl.ButtonControl(foundIndex=r).Click(x=0, y=0)
    # wct.Click
    # wct.Click


def clickLOC():
    # winControl = auto.WindowControl(
    #     searchDepth=1, ClassName='_NFHeroMainClass')
    # winControl.SetActive()
    accNumEdit = get_2120Class(6)
    editTarget = accNumEdit.GetValuePattern()
    # editTarget.SetValue(value)
    accNumEdit.SetFocus()
    accNumEdit.SendKeys('{DOWN}')
    accNumEdit.SendKeys('{DOWN}')
    accNumEdit.SendKeys('{DOWN}')
    accNumEdit.SendKeys('{DOWN}')


def setStockName():
    a = winControl.DocumentControl(Classname="Edit")
    print(a)

    return


def get_2120Class(num):
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    # print(winControl1)
    accNumEdit = winControl.EditControl(foundIndex=num)
    return accNumEdit


def set_NFHeroMainClass_WriteValues(num, value=0):
    accNumEdit = get_2120Class(num)
    editTarget = accNumEdit.GetValuePattern()
    editTarget.SetValue(value)
    # DocumentControl


def set_NFHeroMainClass_WriteValuesDocumentControl(num, value=0):
    accNumEdit = get_2120Class(num)
    editTarget = accNumEdit.GetValuePattern()
    editTarget.SetValue(value)
    accNumEdit.SetFocus()
    accNumEdit.SendKeys('{enter}')


def setUpDownTrade(tradeType, stockName, qty, price):
    print(f"{stockName} I 수량 : {qty} / 단가 : {price}")
    set_NFHeroMainClass_WriteValues(7, qty)
    set_NFHeroMainClass_WriteValues(8, price)
    pag.press('enter')
    pass


def setTrade(num, acc=0):
    trade = tradeList(num)
    stockName = trade[0]
    # sellList = trade[1]
    # setAccNum('24', "2120", 9)
    for price, qty in trade[1].items():
        clickWct("매도")
        set_NFHeroMainClass_WriteValuesDocumentControl(4, stockName)
        clickLOC()
        setUpDownTrade("매도", stockName, qty, price)
    for price, qty in trade[2].items():
        clickWct("매수")
        set_NFHeroMainClass_WriteValuesDocumentControl(4, stockName)
        clickLOC()
        setUpDownTrade("매수", stockName, qty, price)
    # print(sellList)


if __name__ == '__main__':
    # setList = ["$4.4", "$4.5"]
    # print(replaceDollar(setList))
    # clickLOC()
    # set_NFHeroMainClass_WriteValues(6, "LOC")
    # setTrade(2)
    setAccNum('24', "2120", 9)
    # print(sellValueList(12))
    pass
    # foundWct()

    # 2	예약주문기간 종료일
    # 3	예약주문기간 시작일
    # 4	종목
    # 5
    # 6	주문종류 LOC
    # 7	주문수량
    # 8	주문단가
    # 9	계좌번호
    # 10	예약번호?
