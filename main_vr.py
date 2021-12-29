from def_kw import *
from def_ss import *
from slack_engin import *
# import sys
# sys.path.append(["D:\TaiCloud\Documents\Project\Lotto"])
# import def_lotto

# 395134


def test_acc(user="kwak", type="거치식"):
    accuntInfo = accunt_info()
    print(accuntInfo[user][type][1])


def vr_main(stock="TQQQ", user="kwak", type="적립식", start="start"):
    accuntInfo = accunt_info(user, type)
    vr_type = accuntInfo[0]
    vr_qty = accuntInfo[1]
    slackSendMsg(f"{type} 거래를 시작합니다.")
    # kw_window_check_kwlogin()
    kw_window()
    logger.info("영운문창 활성화")
    time.sleep(1)
    pag.press("esc", 5)
    kw_secrch = kw_secrch_Edit()
    time.sleep(1)
    sendText(kw_secrch, "2102")  #
    time.sleep(3)
    input2102_check_accuntNumber(vr_type)
    time.sleep(0.5)
    input2102_buy_VR(stockname=stock, user=user,
                     qty=vr_qty, test=start, type=type)
    # "[855056] 매수증거금이 부족합니다. 매수가능(0)주"
    time.sleep(0.5)
    print("---------------")
    input2102_sell_VR(stockname=stock, user=user,
                      qty=vr_qty, test=start, type=type)
    time.sleep(0.5)
    check_message()
    print("메시지 이상없음")
    time.sleep(1)
    pag.press("esc", 5)
    save_screenshot(user, type)


if __name__ == '__main__':
    # vr_main(type="적립식",start="test")
    # pag.press("esc", 5)
    vr_main(user="kwak", type="적립식", start="start")
    # vr_main(user="kwak", type="거치식", start="start")
    # input2102_check_accuntNumber(1)
    # test_acc()
