
from slack_engin import *
import subprocess
import time


def startLotto():
    logger.info("Lotto AV1 Start!")
    slackSendMsg("Lotto AV1 Start!")
    subprocess.Popen(
        r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -av1=0")
    time.sleep(30)
    logger.info("Lotto AV2 Start!")
    slackSendMsg("Lotto AV2 Start!")
    subprocess.Popen(
        r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -av2=0")
    time.sleep(30)
    logger.info("Lotto AV3 Start!")
    slackSendMsg("Lotto AV3 Start!")
    subprocess.Popen(
        r"D:\TaiCloud\Documents\Project\Lotto\Lotto\Run.exe -av4=0")


if __name__ == '__main__':
    startLotto()
    try:
        # winActivate('iLabAuto')
        # checkLottoOpen()
        # openLoto("kwak")
        # startAvatar()
        # startAvatar()
        # checkLottoOpen()
        # # winActivate("iLabAuto",0,0)
        # pass
        # kw_Login()
        # x,y = winActivate("iLabAuto",0,0)
        # print(pag.position())
        # x1,y1 = pag.position()
        # pag.moveTo(x1+307,y1+737)
        # pag.click()
        # pag.click(x+307,y+736)
        # openLoto("han",0)
        # closeLoto()

        # kw_Login_2("han")
        # close_Loto()
        # checkLoto()
        # closeLoto()
        # sleep5m()
        # kw_close()
        # today_nowDate()
        # a = check_message()
        # print(a)
        # if a == None:
        #     print("무한매수를 완료하였습니다.")
        # else:
        #     print(a)
        # sleep5m(1)
        # try:
        #     kw_window()
        # except:
        #     print('Hello Error!')
        # kw_Login_2()
        # ;
        # kw_close()
        pass
    except:
        # logging.error(traceback.format_exc())
        pass
