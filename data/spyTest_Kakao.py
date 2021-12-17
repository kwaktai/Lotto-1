import win32con
import win32gui
import win32api


def kakaobot():
    chattingroom = win32gui.FindWindow(None, "와이프♥")
    # chattingroom = win32gui.FindWindow(None, "반포모임골프방")
    print(chattingroom)
    chatEdit = win32gui.FindWindowEx(
        "0x000B11BE", None, "RICHEDIT50W", None)  # 채팅방안 메세지 입력창

    sendText(chatEdit, "kakao bot")


def sendText(hwnd, text):
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
    # win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)  # 엔터키


if __name__ == '__main__':
    kakaobot()
