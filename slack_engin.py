import requests
from slacker import Slacker
from passdoc import pw
from def_loggin import __get_logger, logging
logger = __get_logger()
logging.basicConfig(level=logging.INFO)

slack_stock = pw.slackT()


channelName = "#unlimited-purchase-vr"
# channelName = "#stock"
slackTest = Slacker(slack_stock)
# channelList = slackTest.channels.list()
# print(channelList)


def slackSendMsg(text):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer "+slack_stock},
                  data={"channel": channelName, "text": text}
                  )
    return print((f"message : {text}"))


def slackSendFile(img, type=""):
    try:
        slackTest.files.upload(f"img/{img}_{type}.png", channels=channelName)
    except:
        # logger.info("파일 없습니다.")
        pass


def slackSendMsg_rsi_check(text):
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer "+slack_stock},
                  data={"channel": "#rsi-check", "text": text}
                  )
    return print((f"channel #rsi-check: {text}"))


logger.debug("debug")
logger.info("info")

if __name__ == "__main__":
    slackSendMsg("?????")
    slackSendMsg_rsi_check("성공")
    # slackSendFile("kwak", "거치식")
    pass
