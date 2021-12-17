import logging


# def infer():
#     infer_logger = logging.getLogger("inference/infer")
#     # 다른 모듈에서도 logging을 import한 후 logger 이름을 설정하여 사용합니다.
#     infer_logger.error("inference good")


def __get_logger():
    __logger = logging.getLogger('logger')
    # 로그 포멧 정의
    formatter = logging.Formatter(
        'BATCH##AWSBATCH##%(levelname)s##%(asctime)s##%(message)s >> @@file::%(filename)s@@line::%(lineno)s')
    # 스트림 핸들러 정의
    stream_handler = logging.StreamHandler()
    # 각 핸들러에 포멧 지정
    stream_handler.setFormatter(formatter)
    # 로거 인스턴스에 핸들러 삽입
    __logger.addHandler(stream_handler)
    # 로그 레벨 정의
    __logger.setLevel(logging.DEBUG)
    return __logger

logger = __get_logger()
logger.info("data")