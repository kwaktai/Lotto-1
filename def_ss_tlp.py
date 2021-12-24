import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from slack_engin import *
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


def tryBuy(pig):
    pigList = dataList(pig)
    checkWork = list(pigList.values())[0]  # 일하자? 쉬자? 존버
    stockName = list(pigList.values())[1]  # TQQQ TECL
    if checkWork == "일하자":
        pigName = list(pigList.keys())[0]
        print(pigName)
        for buy in range(2, 5):
            checkValue = list(pigList.values())[buy]
            if checkValue == "-":
                pass
            else:
                stockName = list(pigList.values())[1]
                buyPrice = float(list(pigList.keys())[buy])
                buyQty = int(checkValue)
                # print(buyPrice)
                # print(buyQty)
                # print(stockName)
            for sell in range(5, 8):
                checkValue = list(pigList.values())[sell]
                if checkValue == "-":
                    pass
                else:
                    sellPrice = float(list(pigList.keys())[sell])
                    sellQty = int(checkValue)
                    # print(sellPrice)
                    # print(sellQty)
        return stockName, buyQty, buyPrice, sellQty, sellPrice

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
        pass


if __name__ == '__main__':
    # pigDic = {}
    for pig in ["one", "two", "three"]:
        a = tryBuy(pig)
        print(a)
    # tryBuy()

    pass
