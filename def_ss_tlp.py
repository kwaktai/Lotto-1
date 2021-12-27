import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from slack_engin import *
from def_kw import input2102_buy, kw_secrch_Edit, sendText, kw_window, input2102_sell, input2102_check_check, setAccNum
import time
import pyautogui as pag
from def_loggin import __get_logger

# test 20211224-B

logger = __get_logger()
# "client_email": "gstopy@spreadsheettopython-320114.iam.gserviceaccount.com"

todayNow = datetime.today().strftime('%Y-%m-%d')

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'D:\TaiCloud\Documents\Project\stockRpawin_kw\jsop_Key\spreadsheettopython-320114-0340a7e3e1da.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_TLP = "https://docs.google.com/spreadsheets/d/1b6da8QlPW0EWs-__vbd7gc_mZCoCH_DPDiYYbEogmD4/edit#gid=981824825"

doc = gc.open_by_url(spreadsheet_TLP)
worksheet_order = doc.worksheet('자동거래시트')  # 시트선택
worksheet_order.acell("C2").value


def dataList(pig):
    i = str(pig)
    pigList = {"one": 2, "two": 4, "three": 6}
    valueList = []
    valueList = worksheet_order.col_values(pigList[i] + 1)
    valueList = valueList[1:15]
    # print(valueList)
    qtyList = []
    qtyList = worksheet_order.col_values(pigList[i] + 2)
    qtyList = qtyList[1:15]
    # print(qtyList)
    pigDic = {}
    for dic in range(len(valueList)):
        pigDic[valueList[dic]] = (qtyList[dic])
    return pigDic


def pig_test():
    pigList = {'첫째': '일하자', '종목': 'TQQQ', '169.54': '3',
               '186.49': '3', '큰수': '-', '+0%': '-', '+5%': '-', '186.61': '20'}
    pigList2 = {'둘째': '쉬자', '종목': 'TECL', '평단': '3',
                '+10%': '-', '큰수': '-', '+0%': '-', '+5%': '-'}
    return pigList


def open2102():
    kw_window()
    pag.press("esc", 5)
    kw_secrch = kw_secrch_Edit()
    time.sleep(1)
    sendText(kw_secrch, "2102")
    # input2102_check_loc()


def tryTLP(pig, test):
    pigList = dataList(pig)
    print(pigList)
    checkWork = list(pigList.values())[0]  # 일하자? 쉬자? 존버?
    pigAcc = list(pigList.values())[8]  # 계좌번호
    stockName = list(pigList.values())[1]  # TQQQ TECL
    setAccNum(pigAcc, "2111")
    if checkWork == "일하자":
        pigName = list(pigList.keys())[0]
        print(f"{pigName} : {pigAcc}")
        open2102()
        for buy in range(2, 5):
            print(buy)
            checkValue = list(pigList.values())[buy]
            if checkValue == "-":
                print("buy not")
                pass
            else:
                stockName = list(pigList.values())[1]
                buyPrice = float(list(pigList.keys())[buy])
                buyQty = int(checkValue)
                input2102_buy(stockName, buyQty, buyPrice, test)  #
                # print(buyPrice)
                # print(buyQty)
                # print(stockName)
        for sell in range(5, 8):
            checkValueSell = list(pigList.values())[sell]
            if checkValueSell == "-":
                print("sell not")
            else:
                if sell == 5 or sell == 6:
                    i = 3
                    print("LOC")
                elif sell == 7:
                    i = 2
                    print("After")
                sellPrice = float(list(pigList.keys())[sell])
                sellQty = int(checkValueSell)
                input2102_check_check(i)
                time.sleep(0.2)
                input2102_sell(stockName, sellQty, sellPrice, test)
                # print(sellPrice)
                # print(sellQty)
                pass

    elif checkWork == "쉬자":
        # pigName = list(pigList.keys())[0]
        # print(pigName)
        # print(f"{pigName}는 휴식중.....")
        pass
    elif checkWork == "존버":
        # pigName = list(pigList.keys())[0]
        # print(pigName)
        # print("매도만 하기")
        print("존버 : 매도만 하기")
        for sell in range(5, 8):
            checkValueSell = list(pigList.values())[sell]
            if checkValueSell == "-":
                print("sell not")
            else:
                if sell == 5 or sell == 6:
                    i = 3
                    print("LOC")
                elif sell == 7:
                    i = 2
                    print("After")
                sellPrice = float(list(pigList.keys())[sell])
                sellQty = int(checkValueSell)
                input2102_check_check(i)
                time.sleep(0.2)
                input2102_sell(stockName, sellQty, sellPrice, "test")
            pass


def main(test):
    for pig in ["one", "two", "three"]:
        tryTLP(pig, test)


if __name__ == '__main__':
    main("start")
    pass
