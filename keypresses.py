from pynput.keyboard import Key, Controller
import time
from random import randint

keyboard = Controller()

def rotate():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    delay()    
    return

def left():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    delay()
    return

def right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    delay()
    return

def down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    delay()
    return

def space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    delay()
    return

def switchScreens():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    return

def delay():
    delaytime = randint(10, 30)
    time.sleep(delaytime/100)
    return