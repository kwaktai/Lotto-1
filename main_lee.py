import logging
import traceback
from def_kw import get_today_hoilday, save_screenshot, startGlobal
from def_lotto import *
from def_ss import *
from main_vr import vr_main
from slack_engin import *

logging.basicConfig(filename='log\debug.log',
                    level=logging.ERROR, format='%(asctime)s %(message)s')


def user_name():
    pass


if __name__ == '__main__':
    try:
        if get_today_hoilday() is True:
            user = "lee"
            startGlobal()
            kw_Login(user)
            time.sleep(10)
            openLoto(user=user)
            # time.sleep(30)
            # closeLoto()
            save_screenshot(user)
            time.sleep(10)
            mess = check_message_lotto()
            if mess == None:
                slackSendMsg(f"{user}의 무한매수를 완료하였습니다.")
            else:
                slackSendMsg(mess)
            slackSendMsg(f"{user}의 VR 매수/매도가 시작합니다.")
            vr_main(user=user, type="적립식")
            slackSendMsg(f"{user}의 VR 매수/매도를 완료합니다.")
            kw_close()
            slackSendMsg(f"{user}의 영운문(Global)를 종료합니다.")
        else:
            slackSendMsg("주말 입니다.{user}")
            # lee 기준으로 VR 구성해야함.
    except:
        slackSendMsg(f"{user} : 에러발생 확인바람.")
        logging.error(traceback.format_exc())

# -----------------------
# if __name__ == '__main__':
#     try:
#         if get_today_hoilday() is True:
#             rsiResultList = rsiResult().items()
#             if not rsiResultList:
#                 slackSendMsg_rsi_check("확인된 종목이 없습니다.")
#             else:
#                 for key, value in rsiResultList:
#                     slackSendMsg_rsi_check(f"{key}  : {value}%")

#             if check_window("영웅문Global Login") == 0:
#                 pass
#             else:
#                 kw_window_check_kwlogin()
#                 time.sleep(0.2)
#                 # print("이상함")
#                 pag.hotkey('alt', 'f4')
#                 time.sleep(5)
#             slackSendMsg("무한매수를 시작합니다.")
#             if i == "kwak":
#                 kw_Login_2(i)
#                 sleepXm(0.5)
#                 openLoto(1)
#                 sleepXm(1)
#                 closeLoto()
#                 time.sleep(10)
#                 mess = check_message_lotto()
#                 if mess == None:
#                     slackSendMsg("무한매수를 완료하였습니다.")
#                 else:
#                     slackSendMsg(mess)
#                 slackSendMsg("VR 매수/매도가 시작합니다.")
#                 vr_main(type="적립식")
#                 slackSendMsg("VR 매수/매도를 완료합니다.")
#                 kw_close()
#                 slackSendMsg("영운문(Global)를 종료합니다.")
#         else:
#             slackSendMsg("주말 입니다.")
#     except:
#         logging.error(traceback.format_exc())
