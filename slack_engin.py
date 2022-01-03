import requests
from slacker import Slacker
# from def_loggin import __get_logger
# logger = __get_logger()


# slack_stock = "xoxb-1731659647985-1712312144294-6M3k1f68GwxxF9ty7685pd2i"
slack_stock = "xoxb-1731659647985-1712312144294-zBrPfRhePigo2foPVjLjjgEJ"
channelName = "#unlimited-purchase-vr"
slackTest = Slacker(slack_stock)


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


if __name__ == "__main__":
    slackSendMsg("?????")
    # slackSendMsg_rsi_check("성공")
    # slackSendFile("kwak", "거치식")
    pass
