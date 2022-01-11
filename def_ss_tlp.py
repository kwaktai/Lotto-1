import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from slack_engin import *
# from def_kw import setAccNum
import def_ui
import time
import csv
# import pyautogui as pag

# test 20211224-B


def main(test):
    setSheet()
    for pig in ["one", "two", "three"]:
        setTLP(pig, test)


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
    pigList = {'첫째': '일하자', '종목': 'TECL', '매수83.54': '7', '매수87.72': '-', '매수85.84': '6', '+0%(매도)': '-', '매도87.77':
               '34', '매도91.95': '102', 'acc': '04'}
    pigList2 = {'둘째': '쉬자', '종목': 'TECL', '평단': '3',
                '+10%': '-', '큰수': '-', '+0%': '-', '+5%': '-'}
    return pigList


def setTLP(pig, test):
    try:
        user = "kwak"
        pigList = dataList(pig)
        # pigList = pig_test()
        checkWork = list(pigList.values())[0]  # 일하자? 쉬자? 존버?
        pigAcc = pigList['acc']  # 계좌번호
        stockName = list(pigList.values())[1]  # TQQQ TECL
        def_ui.setAccNum(pigAcc, "2102")
        if checkWork == "일하자":
            pigName = list(pigList.keys())[0]
            logger.info(f"{pigName} : {pigAcc}")
            for buy in range(2, 5):
                logger.info(buy)
                checkValue = list(pigList.values())[buy]
                if checkValue == "-":
                    logger.info("매수 거래 없음.")
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
                    logger.info("sell not")
                else:
                    if sell == 5 or sell == 6:
                        i = "LOC"
                    elif sell == 7:
                        i = "AFTER지정"
                    sellPrice = str(float(list(pigList.keys())[sell][2:]))
                    sellQty = str(int(checkValueSell))
                    def_ui.set2102_Sell(stockName, user, sellQty,
                                        sellPrice, test, i, pigAcc)
                    pass
        elif checkWork == "쉬자":
            logger.info(f"{pig}: 쉬는 타임.")
            pass
        elif checkWork == "존버":
            logger.info(f"{pig}는 존버(매도만 하기)")
            for sell in range(5, 8):
                checkValueSell = list(pigList.values())[sell]
                if checkValueSell == "-":
                    logger.info("sell not")
                else:
                    if sell == 5 or sell == 6:
                        i = "LOC"
                        logger.info("LOC")
                    elif sell == 7:
                        i = "AFTER지정"
                        logger.info("After")
                    sellPrice = float(list(pigList.keys())[sell])
                    sellQty = int(checkValueSell)
                    def_ui.set2102_Sell(stockName, user, sellQty,
                                        sellPrice, test, i, pigAcc)
                pass
    except:
        print("에러")


def setSheet():
    n = ["TLP1_04", "TLP2_02", "TLP3_09"]
    for i in range(0, 2):
        setTLPvalue(n[i])


if __name__ == '__main__':
    # print(dataList("one"))
    main("start")
