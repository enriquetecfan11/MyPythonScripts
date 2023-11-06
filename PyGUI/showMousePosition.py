import pyautogui, sys
print('Press Ctrl-C to quit.')

while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
    if keyboard.is_pressed('q'):
        print('\n')
        break
    elif keyboard.is_pressed('p'):
        print('\n')
        print(pyautogui.position())
        break
