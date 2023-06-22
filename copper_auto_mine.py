import pyautogui
import time
from .paths import (from_copper_mine_to_town,
                    from_copper_mine_portal_to_town_chest,
                    deposit_all_in_chest,
                    from_town_to_copper_mine,
                    from_copper_mine_portal_to_copper_vein)


screenWidth, screenHeight = pyautogui.size()


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
    time.sleep(7200)
