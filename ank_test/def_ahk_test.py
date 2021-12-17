from ahk import AHK

ahk = AHK()

# ahk.run_script('Run Notepad')  # Open notepad
# win = ahk.find_window(title=b'Untitled - Notepad')  # Find the opened window
# win = ahk.find_window(title='영웅문Global')  # Find the opened window
# print(win)

# a = ahk.find_windows_by_title('영웅문1Global', exact=True)
# print(a)


def always_on_top(win):
    return win.always_on_top


# find_windows(always_on_top)

# Blocks until mouse finishes moving (the default)
ahk.mouse_move(x=100, y=100, blocking=True)
# Moves the mouse to x, y taking 'speed' seconds to move
ahk.mouse_move(x=150, y=150, speed=10, blocking=True)
print(ahk.mouse_position)  # (150, 150)
