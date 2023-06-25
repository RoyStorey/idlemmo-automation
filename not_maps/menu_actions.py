import pyautogui


def press_claim_button():
    pyautogui.moveTo(1150, 625, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(150, 925)
    pyautogui.mouseDown()
    i = 0
    while i < 15:
        pyautogui.moveRel(1700, -50, duration=.15)
        pyautogui.moveRel(-1700, 0, duration=.15)
        i += 1
    pyautogui.moveRel(1700, -50, duration=.5)
    pyautogui.mouseUp()


def toggle_map():
    pyautogui.press('m')


def toggle_auto_attack():
    pyautogui.moveTo(910, 1010, duration=2, tween=pyautogui.easeInOutQuad)


def press_player_select():
    pyautogui.moveTo(1740, 1000, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def press_select_player():
    pyautogui.moveTo(1050, 800, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def switch_to_player_x(player_number):
    press_player_select()
    if (player_number == 1):
        pyautogui.moveTo(600, 400, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        press_select_player()
        press_claim_button()
    if (player_number == 2):
        pyautogui.moveTo(1000, 400, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        press_select_player()
        press_claim_button()
    if (player_number == 3):
        pyautogui.moveTo(1400, 400, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        press_select_player()
        press_claim_button()
