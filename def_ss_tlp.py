import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from slack_engin import *
from def_kw import input2102_buy, kw_secrch_Edit, sendText, kw_window, input2102_sell, input2102_check_check, setAccNum
import def_ui
import time
import pyautogui as pag
import csv
from def_loggin import __get_logger

# test 20211224-B


def main(test):
    setSheet()
    for pig in ["one", "two", "three"]:
        setTLP(pig, test)


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
worksheet_TLP = doc.worksheet('TLP')  # 시트선택
worksheet_TLP.acell("C2").value


def getTLPvalue(acc):
    try:
        n = ["TLP1_04", "TLP2_02", "TLP3_09"]
        # kwak_mystockdata_TLP1_04
        revenueFile = f"D:\TaiCloud\Documents\Project\Lotto\stockFile\kwak_mystockdata_{acc}.tsv"
        f = open(revenueFile, 'r', encoding='utf-8')
        rdr = csv.reader(f, delimiter='\t')
        r = list(rdr)
        myValue = r[1][5]
        myQty = r[1][6]
        stockName = r[1][1]
        return stockName, myValue, myQty
    except:
        myValue = 0
        myQty = 0
        stockName = 0
        return stockName, myValue, myQty


def setTLPvalue(acc):
    stockName, myValue, myQty = getTLPvalue(acc)

    if acc == "TLP1_04":
        worksheet_TLP.update_acell('D30', myValue)
        worksheet_TLP.update_acell('E30', myQty)
    elif acc == "TLP2_02":
        worksheet_TLP.update_acell('G30', myValue)
        worksheet_TLP.update_acell('H30', myQty)
    elif acc == "TLP3_09":
        worksheet_TLP.update_acell('J30', myValue)
        worksheet_TLP.update_acell('K30', myQty)
    pass


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
        # print(pigDic)
    return pigDic


def pig_test():
    pigList = {'첫째': '일하자', '종목': 'TQQQ', '169.54': '3',
               '186.49': '3', '큰수': '-', '+0%': '-', '+5%': '-', '186.61': '20'}
    pigList2 = {'둘째': '쉬자', '종목': 'TECL', '평단': '3',
                '+10%': '-', '큰수': '-', '+0%': '-', '+5%': '-'}
    return pigList


# {'첫째': '일하자', '종목': 'TECL', '88.76': '6', '93.19': '5', '101.98': '-',
#     '+0%': '-', '93.26': '18', '97.69': '54', 'acc': '04'}
# {'둘째': '쉬자', '종목': 'TECL', '평단': '3', '+5%': '-',
#     '큰수': '-', '+0%': '-', '+10%(매도)': '-', 'acc': '02'}


# def open2102():
#     kw_window()
#     pag.press("esc", 5)
#     kw_secrch = kw_secrch_Edit()
#     time.sleep(1)
#     sendText(kw_secrch, "2102")
#     # input2102_check_loc()


def setTLP(pig, test):
    user = "kwak"
    pigList = dataList(pig)
    checkWork = list(pigList.values())[0]  # 일하자? 쉬자? 존버?
    pigAcc = pigList['acc']  # 계좌번호
    stockName = list(pigList.values())[1]  # TQQQ TECL
    setAccNum(pigAcc, "2102")
    if checkWork == "일하자":
        pigName = list(pigList.keys())[0]
        print(f"{pigName} : {pigAcc}")
        for buy in range(2, 5):
            print(buy)
            checkValue = list(pigList.values())[buy]
            if checkValue == "-":
                print("매수 거래 없음.")
                pass
            else:
                stockName = list(pigList.values())[1]
                buyPrice = str(float(list(pigList.keys())[buy][2:]))
                buyQty = str(int(checkValue))
                def_ui.set2102_Buy(stockName, user, buyQty,
                                   buyPrice, test, "LOC", pigAcc)
                # input2102_buy(stockName, buyQty, buyPrice, test)  #
        for sell in range(5, 8):
            checkValueSell = list(pigList.values())[sell]
            if checkValueSell == "-":
                print("sell not")
            else:
                if sell == 5 or sell == 6:
                    # i = 3
                    # print("LOC")
                    i = "LOC"
                elif sell == 7:
                    # i = 2
                    # print("After")
                    i = "AFTER지정"
                sellPrice = str(float(list(pigList.keys())[sell][2:]))
                sellQty = str(int(checkValueSell))
                # input2102_check_check(i)
                # time.sleep(0.2)
                def_ui.set2102_Sell(stockName, user, sellQty,
                                    sellPrice, test, i, pigAcc)
                # input2102_sell(stockName, sellQty, sellPrice, test)
                # print(sellPrice)
                # print(sellQty)
                pass
    elif checkWork == "쉬자":
        pass
    elif checkWork == "존버":
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


def setSheet():
    n = ["TLP1_04", "TLP2_02", "TLP3_09"]
    for i in range(0, 2):
        setTLPvalue(n[i])


    # setTLPvalue("TLP1_04")
if __name__ == '__main__':
    main("start")
    # setSheet()
    # def_ui.set2102_Buy("TQQQ", "kwak", "34", "160.22", "test", "LOC", "82")
    pass
