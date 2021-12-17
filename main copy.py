from def_lotto import *
from slack_engin import *
from main_vr import vr_main
from def_kw import check_window, get_today_hoilday,startGlobal
# from def_kw import kw_window_check_kwlogin
from def_kw import save_screenshot
from def_ss import *
import logging
import traceback
from def_loggin import __get_logger
logger = __get_logger()
logging.basicConfig(filename='log\debug.log',
                    level=logging.ERROR, format='%(asctime)s %(message)s')

logger = __get_logger()

# def globalHandleV():
#     HG_titleName = win32gui.FindWindow(None, "영웅문Global")
#     return HG_titleName

def main_copy():
    try:
        if get_today_hoilday() is True:
        # if get_today_hoilday() is False:
            # rsiResultList = rsiResult().items()
            # if not rsiResultList:           
            #     slackSendMsg_rsi_check("확인된 종목이 없습니다.")
            # else:
            #     for key, value in rsiResultList:
            #         slackSendMsg_rsi_check(f"{key}  : {value}%")
            user_name = ["kwak", "lee", "han"]  # 사용자 아이디
            for user in user_name:
                startGlobal()
                if user == "kwak":
                    slackSendMsg(f"{user}의 무한매수를 시작합니다.")
                    kw_Login_2(user)
                    sleepXm(0.1)
                    # globalHandle = globalHandleV()
                    # openLoto(user=user)
                    # sleepXm(1.2)
                    # closeLoto()
                    time.sleep(10)
                    save_screenshot(user)
                    time.sleep(10)
                    mess = check_message_lotto()
                    if mess == None:
                        slackSendMsg(f"{user}의 무한매수를 완료하였습니다.")
                    else:
                        slackSendMsg(mess)
                    slackSendMsg(f"{user}의 VR <적립식> 매수/매도가 시작 합니다.")
                    vr_main(type="적립식", user=user,start="test")
                    slackSendMsg(f"{user}의 VR <적립식> 매수/매도를 완료 했습니다.")
                    slackSendMsg(f"{user}의 VR <거치식> 매수/매도를 시작 합니다.")
                    vr_main(type="거치식", user=user,start="test")
                    slackSendMsg(f"{user}의 VR <거치식> 매수/매도를 완료 했습니다.")
                    kw_close()
                    slackSendMsg(f"{user}의 영운문(Global)를 종료합니다.")
                elif user == "lee":
                    pass
                    # startGlobal()
                    # kw_Login_2(user)
                    # sleepXm(0.5)
                    # slackSendMsg(f"{user}의 VR 매수/매도가 시작합니다.")
                    # vr_main(user=user,type="적립식")
                    # slackSendMsg(f"{user}의 VR 매수/매도를 완료합니다.")
                    # kw_close()
                    # slackSendMsg(f"{user}의 영운문(Global)를 종료합니다.")
                    # lee 기준으로 VR 구성해야함.
                elif user == "han":
                    pass
        else:
            slackSendMsg("주말 입니다.")
    except:
        logging.error(traceback.format_exc())
        slackSendMsg(f"{user} : 에러발생 확인바람.")
        # startGlobal()

if __name__ == '__main__':
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    main_copy()

