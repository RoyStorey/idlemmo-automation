import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()


def from_copper_mine_to_town():
    pyautogui.moveTo(1860, 800, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_copper_mine_portal_to_town_chest():
    pyautogui.moveTo(650, 800, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def deposit_all_in_chest():
    pyautogui.moveTo(200, 400, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.press('esc')


def from_town_to_copper_mine():
    pyautogui.moveTo(100, 550, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def from_copper_mine_portal_to_copper_vein():
    pyautogui.moveTo(835, 550, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def deposit_copper_ore():
    from_copper_mine_to_town()
    time.sleep(5)
    from_copper_mine_portal_to_town_chest()
    time.sleep(5)
    deposit_all_in_chest()
    time.sleep(5)
    from_town_to_copper_mine()
    time.sleep(5)
    from_copper_mine_portal_to_copper_vein()


while 1 == 1:
    deposit_copper_ore()
