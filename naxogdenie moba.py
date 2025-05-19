from  pyautogui import*
from  time import*

kd_r = 0
kd_e = 0
kd_probel = 0



while True:
    try:
        result = locateOnScreen(r'e:\Games\Albion Fishbot\moba.png', confidence=0.69)
        if result:
            print("Найдено:", result)
            x, y = center(result)
            click(x , y , duration=0.2)

            for _ in range(2):
                press("q")
                sleep(0.9)
            if  kd_r == 0:
                press('r')
                kd_r = 14

            elif kd_r <= 14 and kd_r != 0 and kd_r != 2 and kd_r != 1:
                kd_r -= 3

            while True:
                pers_ikonka = locateOnScreen(r'e:\Games\Albion Fishbot\ikonka.png', confidence=0.9)    
                if pers_ikonka:
                    print('бой продолжаетца ')

                    for _ in range(2):
                        press("q")
                        sleep(0.9)
                    if  kd_e == 0:
                        press('e')
                        kd_e = 11
                        sleep(0.5)
                    elif  kd_r == 0:
                        press('r')
                        kd_r = 14
                        sleep(1)
                    elif kd_probel == 0:
                        press('space')
                        kd_probel = 36

                    if kd_r >= 3:
                        kd_r -= 3
                    elif kd_r >= 2:
                        kd_r -= 2
                    elif kd_r >= 1:
                        kd_r -= 1
                    print("R" ,kd_r)    

                    if kd_e >= 3:
                        kd_e -= 3
                    elif kd_e >= 2:
                        kd_e -= 2
                    elif kd_e >= 1:
                        kd_e -= 1
                    print("E" , kd_e)

                    if kd_probel >= 3:
                        kd_probel -= 3
                    elif kd_probel >= 2:
                        kd_probel -= 2
                    elif kd_probel >= 1:
                        kd_probel -= 1
                    print("space" , kd_probel)
                    
                else:
                    sleep(0.5)
                    print("Бой завершен")
                    break                  
        else:
            print("Не найдено")

    except:
        #print("Изображение не найдено")
        if kd_r > 0:
            kd_r -= 1
            print("R" , kd_r) 
        elif kd_e > 0:
            kd_e -= 1
            print("E" , kd_e)
        elif kd_probel >= 1:
            kd_probel -= 1
            print("space" , kd_probel)         
    sleep(1)
