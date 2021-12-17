from def_lotto import *
from slack_engin import *
from def_kw import kw_secrch_Edit, kw_window, sendText, save_stockQty, saveMyDeposit, startGlobal, activeWindow, popUp_2150_SelectAccount, saveMyRevenue
import def_ss
import logging
import traceback
from def_loggin import __get_logger, accunt_info
logger = __get_logger()


def infoList(user):
    userInfo = {"kwak": {"무매": "45",  "ava1": "24",
                         "ava2": "23", "ava3": "62", "TLP1": "04", "TLP2": "02", "TLP3": "09"}}
    # userInfo = {"kwak": {"무매": "45", "적립식": "49", "거치식": "53", "ava1": "24",
    #                      "ava2": "23", "ava3": "62", "TLP1": "04", "TLP2": "02", "TLP3": "09"}}
    listKey = list(userInfo[user])
    listValue = list(userInfo[user].values())
    return listKey, listValue


def saveStock(user):
    listKey = infoList(user)[0]
    listValue = infoList(user)[1]
    for i in range(len(listKey)):
        print(listKey[i], listValue[i])
        save_stockQty(user, listKey[i], listValue[i])
        saveMyDeposit(user, listKey[i], listValue[i])
        saveMyRevenue(user, listKey[i], listValue[i])
        slackSendMsg("나의 보유 주식 정보를 업데이트합니다.")
        def_ss.mystockdata(user, listKey[i], listValue[i])
        def_ss.myDepositValue(user, listKey[i], listValue[i])
        def_ss.MyRevenueData(user, listKey[i], listValue[i])
        slackSendMsg("보유 주식 정보를 업데이트 완료 하였습니다.")


def main():
    user_name = ["kwak", "lee", "han"]
    # kwak 무매
    try:
        startGlobal()
        slackSendMsg("키움증권 글로벌앱의 업데이트 위해 사전 실행합니다.")
        kw_Login()
        time.sleep(10)
        pag.press("esc", 5)
        saveStock('kwak')
        kw_close()
        # checkLottoOpen()
        closeLoto()
        try:
            activeWindow("영웅문Global")
        except:
            text = str(today_nowDate()) + " : 업데이트 후 정상 종료 하였습니다."
            slackSendMsg(text)
        else:
            slackSendMsg("아직 종료 되지 않았습니다. 체크 바랍니다.")
            kw_close()
        rsiResultList = def_ss.rsiResult().items()
        if not rsiResultList:
            slackSendMsg_rsi_check("확인된 종목이 없습니다.")
        else:
            for key, value in rsiResultList:
                slackSendMsg_rsi_check(f"{key}  : {value}%")
        slackSendMsg("업데이트를 완료 하였습니다. 종료합니다.")
    except:
        # logging.error(traceback.format_exc())
        slackSendMsg("update실행 중 에러발생 확인바람.")
        startGlobal()


if __name__ == "__main__":
    main()
    # saveStock('kwak')
    # saveStock("kwak")
    # saveMyRevenue("kwak", "TLP2", 4)
    # save_stockQty("kwak", "TLP2", 4)
    # saveMyDeposit("kwak", "TLP2", 4)
    # def_ss.mystockdata("kwak", "TLP2")
    # def_ss.myDepositValue("kwak", "TLP2")
    # def_ss.mystockdata("kwak", "ava")
    # popUp_2150_SelectAccount(0)
    # save_stockQty("kwak", "무매")
    # saveMyDeposit("kwak", "무매")
    # popUp_2150_SelectAccount(3)
    # time.sleep(1)

    # save_stockQty("kwak", "ava")
    # saveMyDeposit("kwak", "ava")
    # popUp_2150_SelectAccount(3)
    # time.sleep(1)
    # save_stockQty("kwak", "ava")
    # saveMyDeposit("kwak", "ava")
