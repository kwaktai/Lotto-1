# import logging
# import traceback
from def_kw import get_today_hoilday, save_screenshot, startGlobal
from def_lotto import kw_Login, openLoto, kw_close
import time
from main_vr import vr_main
from slack_engin import *

# logging.basicConfig(filename='log\debug.log',
#                     level=logging.ERROR, format='%(asctime)s %(message)s')


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
            # mess = check_message_lotto()
            # if mess == None:
            #     slackSendMsg(f"{user}의 무한매수를 완료하였습니다.")
            # else:
            #     slackSendMsg(mess)
            slackSendMsg(f"{user}의 VR 매수/매도가 시작합니다.")
            vr_main(user=user, type="적립식")
            slackSendMsg(f"{user}의 VR 매수/매도를 완료합니다.")
            kw_close()
            slackSendMsg(f"{user}의 영운문(Global)를 종료합니다.")
            startGlobal()
        else:
            slackSendMsg("주말 입니다.{user}")
            # lee 기준으로 VR 구성해야함.
    except:
        slackSendMsg(f"{user} : 에러발생 확인바람.")
        startGlobal()
