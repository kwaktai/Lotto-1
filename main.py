import traceback
from def_lotto import *
from slack_engin import *
from main_vr import vr_main
from def_kw import check_window, get_today_hoilday, startGlobal
# from def_kw import kw_window_check_kwlogin
from def_kw import save_screenshot
from def_lotto import closeLotto
from def_ss import *
# import logging
from def_loggin import __get_logger
logger = __get_logger()

# logging.basicConfig(filename='log\debug.log',
#                     level=logging.ERROR, format='%(asctime)s %(message)s')


def user_name():
    pass


if __name__ == '__main__':
    try:
        if get_today_hoilday() is True:
            user_name = ["kwak", "lee", "han"]  # 사용자 아이디
            # rsiResultList = rsiResult().items()
            # if not rsiResultList:
            #     slackSendMsg_rsi_check("확인된 종목이 없습니다.")
            # else:
            #     for key, value in rsiResultList:
            #         slackSendMsg_rsi_check(f"{key}  : {value}%")
            for user in user_name:
                startGlobal()
                if user == "kwak":
                    slackSendMsg(f"{user}의 무한매수를 시작합니다.")
                    kw_Login(user)
                    time.sleep(10)
                    openLoto(user=user)
                    # time.sleep(30)
                    closeLotto()
                    # save_screenshot(user)
                    # time.sleep(10)
                    # mess = check_message_lotto()
                    # if mess == None:
                    #     slackSendMsg(f"{user}의 무한매수를 완료하였습니다.")
                    # else:
                    #     slackSendMsg(mess)
                    slackSendMsg(f"{user}의 VR <적립식> 매수/매도가 시작 합니다.")
                    vr_main(type="적립식", user=user)
                    slackSendMsg(f"{user}의 VR <적립식> 매수/매도를 완료 했습니다.")
                    slackSendMsg(f"{user}의 VR <거치식> 매수/매도를 시작 합니다.")
                    vr_main(type="거치식", user=user)
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
        # logging.error(traceback.format_exc())
        slackSendMsg(f"kwak: 에러발생 확인바람.")
        startGlobal()
