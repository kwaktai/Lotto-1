import logging
from inference import infer


def main():
    logging.debug("without logger name")
    # 로거이름을 설정하지 않고 로깅을 하면 root로 표기됩니다.
    # 위와 같은 사용은 지양합니다.!
    main_logger = logging.getLogger("main/main")
    var = "to log"
    main_logger.error("how %s %s", var, "variable")
    # %s를 활용하여 variable을 로그에 삽입 할 수 있습니다.
    infer()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s:%(name)s:%(asctime)s] %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # 위의 로깅 Config은 글로벌하게 한번만 하기를 기대합니다.
    main()
