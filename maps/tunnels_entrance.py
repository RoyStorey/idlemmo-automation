import pyautogui
import time


def from_entrance_copper_vein():
    pyautogui.moveTo(855, 538, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_entrance_to_freefall_caverns():
    pyautogui.moveTo(120, 795, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_freefall_caverns_to_entrance():
    pyautogui.moveTo(1850, 770, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
