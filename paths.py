import pyautogui


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
