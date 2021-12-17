import win32con
import win32gui
import win32api
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import time
import datetime
import pandas as pd
from pywinauto.application import Application
import def_xyp as dx

def close_kw():
    hWndMsgBox = win32gui.FindWindow("#32770", None)
    hWndButton1 = win32gui.FindWindowEx(hWndMsgBox, None, "Button", None)
    win32gui.SendMessage(hWndButton1, win32con.WM_LBUTTONDOWN, 0, 0)
    win32gui.SendMessage(hWndButton1, win32con.WM_LBUTTONUP, 0, 0)

user_name = ["kwak","lee"]

if __name__ == '__main__':
    for i  in user_name:
        print(i)