from def_lotto import *
from slack_engin import *
from main_vr import vr_main
from def_kw import check_window, get_today_hoilday, startGlobal
from def_kw import kw_window_check_kwlogin
from def_ss import *

# for key, value in rsiResult().items():
#     slackSendMsg_rsi_check(f"{key}  : {value}")

if __name__ == '__main__':
    startGlobal()
    kw_Login("lee")
    pass
