import pandas_datareader as pdr
import datetime as dt
from rsi import rsiData
# from rsi import rsiMin
# import matplotlib.pyplot as plt
# from def_ss import rsiMin_data


def makeRsi(tickerName):
    ticker = pdr.get_data_yahoo(
        tickerName, dt.datetime(2019, 1, 1), dt.datetime.now())
    delta = ticker['Close'].diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up/ema_down
    ticker['RSI'] = 100 - (100/(1 + rs))
    ticker = ticker.iloc[14:]
    ticker_rsi = ticker['RSI']
    return round(ticker_rsi[-1], 2)


def test_rsi():
    stock_rsi = {'KORU': 53.65, 'WANT': 54.03, 'GDXU': 43.9, 'TPOR': 43.17, 'PILL': 49.94, 'LABU': 51.47, 'NAIL': 60.21, 'TECL': 65.88, 'CURE': 67.67, 'DPST': 49.26, 'HIBL': 50.81, 'TNA': 49.72, 'DFEN': 47.63,
                 'FAS': 56.15, 'MIDU': 53.58, 'SOXL': 64.13, 'RETL': 47.27, 'UDOW': 54.74, 'FNGU': 56.6, 'WEBL': 51.66, 'UPRO': 61.02, 'TQQQ': 67.47, 'YINN': 36.95, 'BNKU': 53.39, 'DUSL': 50.07, 'UTSL': 64.18, 'DRN': 62.05}
    return stock_rsi


if __name__ == "__main__":
    makeRsi("BULZ")
    # # print(test_rsi().keys())
    # for i in test_rsi().values():
    #     print(i)
    # # makeRsi("TQQQ")
