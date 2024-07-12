import pyautogui
'''

Controls Library - PYAUTOGUI

This library will allow us to code im the basic inputs so the bot can play and learn

When Hold = False (default) the button will just be pressed not held.

When Hold = True then button will be held until the function is called again with hold = False

'''
pyautogui.FAILSAFE = True

def up(hold=False):
    pyautogui.keyDown('w')
    if hold == False:
        pyautogui.keyUp('w')

def down(hold=False):
    pyautogui.keyDown('s')
    if hold == False:
        pyautogui.keyUp('s')

def left(hold=False):
    pyautogui.keyDown('a')
    if hold == False:
        pyautogui.keyUp('a')

def right(hold=False):
    pyautogui.keyDown('d')
    if hold == False:
        pyautogui.keyUp('d')

def attack(hold=False):
    pyautogui.keyDown('c')
    if hold == False:
        pyautogui.keyUp('c')

def special(hold=False):
    pyautogui.keyDown('x')
    if hold == False:
        pyautogui.keyUp('x')

def sheild(hold=False):
    pyautogui.keyDown('q')
    if hold == False:
        pyautogui.keyUp('q')

def jump(hold=False):
    pyautogui.keyDown('z')
    if hold == False:
        pyautogui.keyUp('z')

def grab(hold=False):
    pyautogui.keyDown('t')
    if hold == False:
        pyautogui.keyUp('t')

