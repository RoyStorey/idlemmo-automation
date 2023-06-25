import pyautogui
import time


def from_entrance_to_froggy_fields():
    pyautogui.moveTo(1850, 675, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_valley_of_the_beans_to_entrance():
    pyautogui.moveTo(125, 675, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
