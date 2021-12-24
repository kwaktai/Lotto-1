# from typing import Type, type_check_only
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from def_rsi import *
from rsi import rsiData
from slack_engin import *
import pyperclip
import time
import csv
from def_loggin import __get_logger, accunt_info

logger = __get_logger()
# "client_email": "gstopy@spreadsheettopython-320114.iam.gserviceaccount.com"

todayNow = datetime.today().strftime('%Y-%m-%d')

# --------------
scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'D:\TaiCloud\Documents\Project\stockRpawin_kw\jsop_Key\spreadsheettopython-320114-0340a7e3e1da.json'
# json_file_name = '/Users/taikwak/TaiCloud/Documents/Project/stockRpawin_kw\spreadsheettopython-320114-0340a7e3e1da.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)
gc = gspread.authorize(credentials)


spreadsheet_url = "https://docs.google.com/spreadsheets/d/1c6qnORby5wLx4EYCzDNIHfDUax90yKIQRwqaiFqy0FI/edit#gid=1309564982"
# spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1P4vYP_suaKcHG-H2HgqobFEqiiGfUpgep3eAOkVrRZI/edit#gid=1309564982'
# spreadsheet_url_test = 'https://docs.google.com/spreadsheets/d/1Ihb-0Fg8a9FaHnFADV0YBHBWlXqwpztYiGkSykBiFJE/edit#gid=0'
findrsishare_20210807_url = "https://docs.google.com/spreadsheets/d/10tIiJxGO5MsXIyeOYlMZXkzuAQe683ZiBUvYtMzWDvE/edit#gid=0"
spreadsheet_url_lee = "https://docs.google.com/spreadsheets/d/1ImrZF6aZ57rfsbpVVvY4GJiVLqszqxCSKXBM_qIJOdU/edit#gid=1309564982"

# -------------
doc = gc.open_by_url(spreadsheet_url)
doc_lee = gc.open_by_url(spreadsheet_url_lee)
worksheet_order = doc.worksheet('주문')  # 시트선택
worksheet_order_stationary = doc.worksheet('주문(거치식)')  # 시트선택
worksheet_order_lee = doc_lee.worksheet('주문')

doc_findrsishare = gc.open_by_url(findrsishare_20210807_url)
findrsishare_stock = doc_findrsishare.worksheet('Stock')
findrsishare_stockList = doc_findrsishare.worksheet('StockList')
findrsishare_total = doc_findrsishare.worksheet('TOTAL')
findrsishare_MyRevenue = doc_findrsishare.worksheet('MyRevenue')

# test 20211224-a
# test 20211224-C


def column_dataQTY():
    # column_data = []
    column_data = findrsishare_stockList.col_values(1)
    column_data.remove("")
    column_data_qty = len(column_data)
    return column_data, column_data_qty


def buy_values(user="kwak", type="적립식"):  # accumulative적립식  stationary거치식
    if user == "kwak" and type == "적립식":
        buy_valuelist = []
        buy_valuelist = worksheet_order.col_values(10)  # 열읽기
        buy_valuelist = buy_valuelist[9:19]
    elif user == "kwak" and type == "거치식":
        buy_valuelist = []
        buy_valuelist = worksheet_order_stationary.col_values(10)  # 열읽기
        buy_valuelist = buy_valuelist[9:19]
    elif user == "lee" and type == "적립식":
        buy_valuelist = []
        buy_valuelist = worksheet_order_lee.col_values(10)  # 열읽기
        buy_valuelist = buy_valuelist[9:19]
    # print(buy_valuelist)
    return buy_valuelist


def sell_values(user="kwak", type="적립식"):
    if user == "kwak" and type == "적립식":
        sell_Valuelist = []
        sell_Valuelist = worksheet_order.col_values(11)
        sell_Valuelist = sell_Valuelist[9:19]
    elif user == "kwak" and type == "거치식":
        sell_Valuelist = []
        sell_Valuelist = worksheet_order_stationary.col_values(11)  # 열읽기
        sell_Valuelist = sell_Valuelist[9:19]
    elif user == "lee" and type == "적립식":
        sell_Valuelist = []
        sell_Valuelist = worksheet_order_lee.col_values(11)
        sell_Valuelist = sell_Valuelist[9:19]
    return sell_Valuelist


def find_current_share_qty():
    range_list_stockname = findrsishare_stockList.col_values(1)
    range_list_stockqty = findrsishare_stockList.col_values(2)
    current_share_qty = {}
    for dic in range(len(range_list_stockname)):
        current_share_qty[range_list_stockname[dic]] = range_list_stockqty[dic]
    return current_share_qty


def rsiMin_data():
    range_list_stockname = findrsishare_stockList.col_values(1)
    range_list_rsiminValue = findrsishare_stockList.col_values(3)
    rsimin_list = {}
    for dic in range(len(range_list_stockname)):
        rsimin_list[range_list_stockname[dic]] = (range_list_rsiminValue[dic])
        # rsimin_list[range_list_stockname[dic]] = int(range_list_rsiminValue[dic])
    return rsimin_list


def save_stockQty_test():
    a = pyperclip.paste()
    findrsishare_stock.update_acell('A1', a)
    pass


def current_share_qty_test():
    rsi_dic_test = {'KORU': '0', 'WANT': '0', 'GDXU': '0', 'TPOR': '235', 'PILL': '0', 'LABU': '98', 'NAIL': '0', 'TECL': '0', 'CURE': '0', 'DPST': '40', 'HIBL': '0', 'TNA': '83', 'DFEN': '0',
                    'FAS': '0', 'MIDU': '0', 'SOXL': '23', 'RETL': '0', 'UDOW': '0', 'FNGU': '96', 'WEBL': '0', 'UPRO': '0', 'TQQQ': '13', 'YINN': '0', 'BNKU': '0', 'DUSL': '117', 'UTSL': '0', 'DRN': '0'}
    return rsi_dic_test


def find_rsi_targetSharelist():  # 현재 잔고가 없는것만 DEL
    rsi_targetSharelist = []
    a = find_current_share_qty()
    # a = current_share_qty_test()  # 테스트용
    # 0이 아닌것만 뺴야하는데, 지금은 0인것만 뺴라고 했다.
    a = dict({key: value for key, value in a.items() if value == "0"})
    for i in a.keys():
        rsi_targetSharelist.append(i)
    return rsi_targetSharelist


def tickerNow_rsi():
    try:
        current_shareLists = find_rsi_targetSharelist()
        # print(current_shareLists)
        targetList = {}
        BasicRsi = {}
        rsiMin_keys = rsiMin_data()
        # print(rsiMin_keys())
        # rsi 기준값 가져오기
        # rsiMin_keys = rsiData.rsiMin()  # rsi 기준값 가져오기
        for i in current_shareLists:
            targetList[i] = rsiMin_keys[i]
        for key in targetList:
            BasicRsi[key] = makeRsi(key)  # 현재
        return BasicRsi, targetList
    except:
        return BasicRsi, targetList


def tickerNow_rsi_test():
    a = ({'KORU': 47.96, 'WANT': 50.63, 'GDXU': 37.1, 'PILL': 46.76, 'NAIL': 57.17, 'TECL': 64.85, 'CURE': 66.7, 'HIBL': 53.56, 'DFEN': 50.98, 'FAS': 62.78, 'MIDU': 55.35, 'RETL': 48.04, 'UDOW': 57.14, 'WEBL': 46.79, 'UPRO': 62.11, 'YINN': 35.11, 'BNKU': 60.74,
          'UTSL': 63.96, 'DRN': 61.14}, {'KORU': 35, 'WANT': 55, 'GDXU': 35, 'PILL': 45, 'NAIL': 50, 'TECL': 60, 'CURE': 45, 'HIBL': 55, 'DFEN': 45, 'FAS': 45, 'MIDU': 45, 'RETL': 50, 'UDOW': 50, 'WEBL': 60, 'UPRO': 55, 'YINN': 35, 'BNKU': 35, 'UTSL': 35, 'DRN': 40})
    BasicRsi = a[0]
    targetList = a[1]
    return BasicRsi, targetList


def tickerNow_rsi_test2():
    current_shareLists = ['KORU', 'GDXU', 'YINN', 'UTSL', 'DPST', 'TPOR', 'DRN', 'PILL', 'CURE',
                          'FAS', 'MIDU', 'LABU', 'NAIL', 'RETL', 'UDOW', 'WANT', 'HIBL', 'UPRO', 'TECL', 'WEBL', 'TQQQ']
    targetList = {}
    BasicRsi = {}
    rsiMin_keys = {'KORU': '35', 'GDXU': '35', 'YINN': '35', 'BNKU': '35', 'UTSL': '35', 'DPST': '35', 'TPOR': '40', 'DRN': '40', 'DFEN': '40', 'DUSL': '40', 'PILL': '45', 'CURE': '45', 'FAS': '45', 'MIDU': '45',
                   'LABU': '45', 'NAIL': '50', 'TNA': '50', 'RETL': '50', 'UDOW': '50', 'WANT': '55', 'HIBL': '55', 'UPRO': '55', 'FNGU': '55', 'TECL': '60', 'WEBL': '60', 'TQQQ': '60', 'SOXL': '65', 'BULZ': '65'}
    for i in current_shareLists:
        targetList[i] = rsiMin_keys[i]
        print(i, targetList[i])
    for key in targetList:
        BasicRsi[key] = makeRsi(key)  # 현재
        print(key, BasicRsi[key])


def rsiResult():
    BasicRsi, targetList = tickerNow_rsi()
    stockList = []
    RsiResultEnd = {}
    for i in BasicRsi.keys():
        stockList.append(i)
    for k in stockList:
        v = int(targetList[k]) - int(BasicRsi[k])
        per = round(v/int(BasicRsi[k])*100, 2)
        if v < 1:
            pass
        else:
            # RsiResultEnd[i] = v
            RsiResultEnd[k] = per
            # print(per)
    return RsiResultEnd


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)


def mystockdata(user, type_1, acc):
    next_row = next_available_row(findrsishare_stock)
    # accuntInfo = accunt_info(user, type_1)
    # accNum = accuntInfo[0]
    sh1 = findrsishare_stock
    save_text = f"D:\\TaiCloud\\Documents\\Project\\Lotto\stockFile\\{user}_mystockdata_{type_1}_{acc}.tsv"
    f = open(save_text, 'r', encoding='utf-8')
    rdr = csv.reader(f, delimiter='\t')
    r = list(rdr)
    try:
        _column = [(1, "C"), (2, "D"), (3, "E"), (4, "F"), (5, "G"), (6, "H"), (7, "I"), (8, "J"), (9, "K"), (10, "L"), (11, "M"),
                   (12, "N"), (13, "O"), (14, "P"), (15, "Q"), (16, "R"), (17, "S"), (18, "T"), (19, "U"), (20, "V"), (21, "W")]
        next_row = int(next_row) - 1
        time.sleep(1)
        for _r in range(1, 20):
            time.sleep(1)
            sh1.update_acell(f"A{str(next_row + _r)}", todayNow)
            sh1.update_acell(f"B{str(next_row + _r)}", type_1)
            for _c, _l in _column:
                if _c == 8:
                    time.sleep(1)
                    sh1.update_acell(f"{_l}{str(next_row + _r)}",
                                     r[_r][_c])  # A1에 값쓰기
                else:
                    time.sleep(0.8)
                    sh1.update_acell(f"{_l}{str(next_row + _r)}",
                                     r[_r][_c])  # A1에 값쓰기

    except IndexError:
        sh1.update_acell(f"A{str(next_row + _r)}", "")
        sh1.update_acell(f"B{str(next_row + _r)}", "")
        logger.info(slackSendMsg(f"{user}의 {type_1} 업데이트 완료"))
        pass


def myDepositValue(user, type, acc):
    try:
        sh = findrsishare_total
        save_text = f"D:\\TaiCloud\\Documents\\Project\\Lotto\\stockFile\\{user}_MyDeposit_{type}_{acc}.tsv"
        f = open(save_text, 'r', encoding='utf-8')
        rdr = csv.reader(f, delimiter='\t')
        r = list(rdr)
        p = r[3][1]
        p = p.replace(",", "")
        updateLocation = {"kwak": {"무매": ["A21"], "ava1": ["B21"], "ava2": [
            "C21"], "ava3": ["D21"], "TLP1": ["E21"], "TLP2": ["F21"], "TLP3": ["G21"]}}
        sh.update_acell(updateLocation[user][type][0], p)
        return p
    except:
        pass


def MyRevenueData(user, type_1, acc):
    next_row = next_available_row(findrsishare_MyRevenue)
    sh1 = findrsishare_MyRevenue
    load_text = f"D:\\TaiCloud\\Documents\\Project\\Lotto\stockFile\\{user}_MyRevenue_{type_1}_{acc}.tsv"
    f = open(load_text, 'r', encoding='utf-8')
    rdr = csv.reader(f, delimiter='\t')
    r = list(rdr)
    # print(r)
    try:
        _column = [(0, "B"), (1, "C"), (2, "D"), (3, "E"), (4, "F"),
                   (5, "G"), (6, "H"), (7, "I"), (8, "J"), (9, "K"), (10, "L"), (11, "M")]
        next_row = int(next_row) - 1
        time.sleep(1)
        for _r in range(1, 11):
            time.sleep(1)
            sh1.update_acell(f"A{str(next_row + _r)}", type_1)
            for _c, _l in _column:
                if _c == 8:
                    time.sleep(1)
                    sh1.update_acell(f"{_l}{str(next_row + _r)}",
                                     r[_r][_c])  # A1에 값쓰기
                else:
                    time.sleep(0.8)
                    sh1.update_acell(f"{_l}{str(next_row + _r)}",
                                     r[_r][_c])  # A1에 값쓰기
    except IndexError:
        sh1.update_acell(f"A{str(next_row + _r)}", "")
        sh1.update_acell(f"B{str(next_row + _r)}", "")
        logger.info(slackSendMsg(f"{user}의 {type_1} 업데이트 완료"))
        pass


if __name__ == '__main__':
    # MyRevenueData("kwak", "무매")
    # print(todayNow)
    # myDepositValue_test("kwak", "ava")
    print(myDepositValue("kwak", "무매", "45"))
    # updateLocation = {"kwak": {"무매": ["B8"], "ava": ["I7"]}}
    # updateLocation = {"kwak": {"무매": ["B8"], "ava": ["I7"]}}
    # sh = findrsishare_total
    # a = updateLocation["kwak"]["무매"][0]
    # print(a)
    # sh.update_acell(updateLocation["kwak"]["ava"][0], p)
    # mystockdata()
    # myDepositValue()
    # buy_values(type="거치식")
    # print(tickerNow_rsi())
    # print(buy_values(user="lee"))
    # mystockdata()
    pass
