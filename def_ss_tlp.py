import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from slack_engin import *
# from def_kw import setAccNum
import def_ui
import time
import csv
import def_kw
# import pyautogui as pag

# test 20211224-B


def startTlpMain(test):
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
# spreadsheet_TLP = "https://docs.google.com/spreadsheets/d/1b6da8QlPW0EWs-__vbd7gc_mZCoCH_DPDiYYbEogmD4/edit#gid=981824825" V2.1버전
spreadsheet_TLP = "https://docs.google.com/spreadsheets/d/1Kg1lw7c9lsyqEtl9owEUi7KYlN6y3plx4bTJ0QKs89E/edit#gid=0"

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
        logger.debug(r)
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
        worksheet_TLP.update_acell('E30', myValue)
        worksheet_TLP.update_acell('D30', myQty)
    elif acc == "TLP2_02":
        worksheet_TLP.update_acell('H30', myValue)
        worksheet_TLP.update_acell('G30', myQty)
    elif acc == "TLP3_09":
        worksheet_TLP.update_acell('K30', myValue)
        worksheet_TLP.update_acell('J30', myQty)
    pass


def getDataList(pig):
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


def setEmptyTrade(checkWork, pig, user, test, pigAcc, pigList, pigName):
    if pigName == "첫째":
        type = "TLP1"
    elif pigName == "둘쩨":
        type = "TLP2"
    elif pigName == "셋째":
        type = "TLP3"
    # pigList = getDataList(pig)
    if checkWork == "일하자":
        valuesAvg = list(pigList.keys())[7]
        print(valuesAvg)
        if valuesAvg == "-" or valuesAvg == "0" or valuesAvg == 0:
            stockName = list(pigList.values())[1]
            buyPrice = str(round(float(list(pigList.keys())[7][2:])*1.15, 2))
            buyQty = str(int(list(pigList.values())[7]))
            print(stockName, buyPrice, buyQty)
            def_ui.setAccNum(pigAcc, "2102")
            time.sleep(0.5)
            def_ui.set2102_Buy(stockName, user, buyQty,
                               buyPrice, test, "AFTER지정", pigAcc)
            def_ui.setAccNum(pigAcc, "2150")
            def_kw.screen_xy()
            def_kw.csv_save("mystockdata", user, type, pigAcc)
        else:
            pass
    pass


def setTLP(pig, test):
    try:
        user = "kwak"
        pigList = getDataList(pig)
        print(pigList)
        # pigList = pig_test()
        checkWork = list(pigList.values())[0]  # 일하자? 쉬자? 존버?
        pigAcc = pigList['acc']  # 계좌번호
        stockName = list(pigList.values())[1]  # TQQQ TECL
        def_ui.setAccNum(pigAcc, "2102")
        if checkWork == "일하자":
            pigName = list(pigList.keys())[0]
            setEmptyTrade(checkWork, pig, user, test,
                          pigAcc, pigList, pigName)
            # list(pigList.keys())[10] 평단 체크
            logger.info(f"{pigName} : 계좌번호({pigAcc})")
            for buy in range(2, 5):
                logger.info(f"매수 거래 항목 : {buy}")
                checkValue = list(pigList.values())[buy]
                if checkValue == "-" or checkValue == "0" or checkValue == 0:
                    logger.info("해당 항목 거래 없음.")
                    pass
                else:
                    stockName = list(pigList.values())[1]
                    buyPrice = str(float(list(pigList.keys())[buy][2:]))
                    buyQty = str(int(checkValue))
                    print(checkValue, stockName, buyPrice, buyQty)
                    def_ui.set2102_Buy(stockName, user, buyQty,
                                       buyPrice, test, "LOC", pigAcc)
            for sell in range(5, 8):
                logger.info(f"매도 거래 항목 : {buy}")
                checkValueSell = list(pigList.values())[sell]
                if checkValueSell == "-" or checkValueSell == "0" or checkValueSell == 0:
                    logger.info("해당 항목 거래 없음.")
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
                if checkValueSell == "-" or checkValueSell == "0" or checkValueSell == 0:
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
        print(f"{pig}에러")


def setSheet():
    n = ["TLP1_04", "TLP2_02", "TLP3_09"]
    for i in range(0, 2):
        setTLPvalue(n[i])


if __name__ == '__main__':
    # print(list(getDataList("two").keys())[10])
    # setEmptyTrade("three")
    # setTLPvalue("TLP1_04")
    # print(dataList("one"))
    startTlpMain("start")
    pass
