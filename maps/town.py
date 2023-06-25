import pyautogui
import time


def to_spore_meadows():
    pyautogui.moveTo(1850, 750, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def to_tunnels_entrance():
    pyautogui.moveTo(118, 542, duration=.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def to_storage_chest():
    pyautogui.moveTo(650, 800, duration=.2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def deposit_all_in_chest():
    pyautogui.moveTo(200, 400, duration=.2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.press('esc')


def to_anvil():
    pyautogui.moveTo(375, 800, duration=.2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
