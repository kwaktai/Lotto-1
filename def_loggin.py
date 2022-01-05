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

# def __get_logger(name=None):
#     # 1 logger instance를 만든다.
#     logger = logging.getLogger(name)

#     # 2 logger의 level을 가장 낮은 수준인 DEBUG로 설정해둔다.
#     logger.setLevel(logging.DEBUG)

#     # 3 formatter 지정
#     formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#     # 4 handler instance 생성
#     console = logging.StreamHandler()
#     file_handler = logging.FileHandler(filename="test.log")

#     # 5 handler 별로 다른 level 설정
#     console.setLevel(logging.INFO)
#     file_handler.setLevel(logging.DEBUG)

#     # 6 handler 출력 format 지정
#     console.setFormatter(formatter)
#     file_handler.setFormatter(formatter)

#     # 7 logger에 handler 추가
#     logger.addHandler(console)
#     logger.addHandler(file_handler)

#     return logger


# logger = __get_logger()
# logger.info("info")

# if __name__ == "__main__":
#     logger = __get_logger()
