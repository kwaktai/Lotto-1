Run , Notpad.exe
WinWait , Calculator
WinGetText , text	; Use the window found by WinWait.
MsgBox , The text is : `n%text%