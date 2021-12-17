import logging
import datetime


# def infer():
#     infer_logger = logging.getLogger("inference/infer")
#     # 다른 모듈에서도 logging을 import한 후 logger 이름을 설정하여 사용합니다.
#     infer_logger.error("inference good")

def accunt_info(user, type):
    # {"무메":[계좌순서,매수수량]]}
    acc_type = {"kwak": {"무매": [0, 0], "적립식": [1, 1], "거치식": [
        2, 7], "ava": [3, 0], "TLP2": [4, 0]}, "lee": {"무매": [0, 0], "적립식": [0, 1], "거치식": [2, 7]},
        "han": {"무매": [0, 0], "적립식": [0, 1], "거치식": [2, 7]}}
    # accuntInfo = accunt_info(user, type)
    accNum = acc_type[user][type][0]
    vr_qty = acc_type[user][type][1]
    return accNum, vr_qty


def __get_logger():
    __logger = logging.getLogger(__name__)
    # 로그의 출력 기준 설정
    __logger.setLevel(logging.INFO)

    # log 출력 형식
    formatter = logging.Formatter(
        '%(asctime)s:[%(name)s]:(%(levelname)s):= %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    __logger.addHandler(stream_handler)

    # log를 파일에 출력
    file_handler = logging.FileHandler('log\debug.log', 'a', 'utf-8')
    file_handler.setFormatter(formatter)
    __logger.addHandler(file_handler)
    return __logger
    # logging.debug('This is a formatted debug message')


if __name__ == "__main__":
    logger = __get_logger()
