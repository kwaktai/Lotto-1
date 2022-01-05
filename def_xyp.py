import pyautogui as pya
import time
from slack_engin import *
# from def_loggin import __get_logger
# logger = __get_logger()


def find_target(img_file, g="True", c=0.8, timeout=5):
    start = time.time()
    target = None
    while target is None:
        target = pya.locateOnScreen(
            f"img/{img_file}.png", grayscale=g, confidence=c)
        # print(target)
        end = time.time()
        if end - start > timeout:
            break
    return target


def xyp_last(img_file, slt="click", g="True", c=0.8, timeout=5):
    target = find_target(img_file, g, c, timeout)
    if target:
        target_canter = pya.center(target)
        logger.info(target_canter)
        x_p, y_p = target_canter
        # x, y = x_p/2, y_p/2
        x, y = x_p, y_p
        s = str(slt)
        if s == "xy":
            return x, y
        elif s == "click":
            return pya.click(x=x, y=y), print(f"{img_file} : 클릭 성공")
            # print(f"{pngfile} : 처리 성공")
        elif s == "move":
            return pya.moveTo(x=x, y=y), print(f"{img_file} : 이동 성공")
        else:
            print("??")
    else:
        logger.debug(f'Error : {img_file}')


def xyp_findxy(img_file, slt="click", g="False", c=0.9, timeout=5):
    target = find_target(img_file, g, c, timeout)
    if target:
        target_canter = pya.center(target)
        # target_canter = pya.position(target)
        # print(target_canter)
        x, y = target_canter
        logger.debug(x, y)
        return x, y


def movingAndClick(x, y, c=1):
    pya.moveTo(x, y)
    time.sleep(0.5)
    pya.click(clicks=c)


if __name__ == "__main__":
    # slackSendMsg("Test 시작")
    # img = "save_excel"
    # xyp_last(img)
    # pya.rightClick()
    x, y = xyp_findxy("2152")
    print(x, y)
    #
