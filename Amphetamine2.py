import pyautogui as pag
import random
import time

MOUSE_REFRESH_RATE = 2 
PAGE_ARROW_REFRESH_RATE = 10 #* 60
BROWSER_WAITING_TIME = 5 #15

def main(refreshPage = True, rightArrow = True, mouse = True):    
    
    i = 0;
    
    while True:
    
        if(i == PAGE_ARROW_REFRESH_RATE/MOUSE_REFRESH_RATE):
            refreshVideoPlayer()
            i = 0
        
        moveMouseRandomly()
        
        i = i + 1
        print('Iteration: '+str(i))
        time.sleep(MOUSE_REFRESH_RATE)
    
def moveMouseRandomly(active = True):
    if active :
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 0.5)
    
def refreshVideoPlayer(active = True):
    if active:
        pag.hotkey('ctrl', 'r')
        time.sleep(BROWSER_WAITING_TIME)
        pag.scroll(-800)
        pag.click(200, 500)
        time.sleep(BROWSER_WAITING_TIME)
        rightArrow()

def rightArrow(times = 3, active = True):
    if active:
        for i in range(times):
            pag.press('right')
            time.sleep(0.5)
        
main()