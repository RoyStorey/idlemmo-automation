import pyautogui
import time


def from_entrance_to_valley_of_the_beans():
    pyautogui.moveTo(1708, 825, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_valley_of_the_beans_to_entrance():
    pyautogui.moveTo(548, 392, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(102, 560, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(256, 399, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(3)
