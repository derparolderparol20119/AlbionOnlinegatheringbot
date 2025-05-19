from pyautogui import *
from time import *
from threading import*

kd_r = 0
kd_e = 0
kd_probel = 0
kd_f = 0

def cooldown_timer():
    global kd_r, kd_e, kd_probel , kd_f
    while True:
        sleep(1)
        if kd_r > 0:
            kd_r -= 1
        if kd_e > 0:
            kd_e -= 1
        if kd_probel > 0:
            kd_probel -= 1
        if kd_f > 0:
            kd_f -=1
def skil_set_q(kol):
    for _ in range(kol):
        press("q")
        sleep(0.9)
def coldawn_print():
    while True:
        print("R", kd_r , "E" , kd_e ,"space" , kd_probel , "F" , kd_f) 
        sleep(3)       

Thread(target=coldawn_print, daemon=True).start()    
Thread(target=cooldown_timer, daemon=True).start()

while True:
    try:
        result = locateOnScreen(r'e:\Games\Albion Fishbot\moba.png', confidence=0.68)
        if result:
            print("Найдено:", result)
            x, y = center(result)
            click(x , y , duration=0.1)
            sleep(0.1)
            while True:
                pers_ikonka = locateOnScreen(r'e:\Games\Albion Fishbot\ikonka.png', confidence=0.95)
                if pers_ikonka:
                    print("бой")
                    if  kd_f == 0:
                        press('f')
                        kd_f = 11
                    skil_set_q(1)
                    if  kd_e == 0:
                        press('e')
                        kd_e = 11
                        sleep(0.5)
                    elif kd_probel == 0:
                        press('space')
                        kd_probel = 36    
                    elif kd_r == 0:
                        press('r')
                        kd_r = 14
                        sleep(1)
                    skil_set_q(3)
                else:
                    break
    except:
        sleep(1)