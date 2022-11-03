import pyautogui as pag
import random
import time

# pyautogui doc: https://pyautogui.readthedocs.io/en/latest/index.html

MOUSE_REFRESH_RATE = 2 
BROWSER_WAITING_TIME = 5 #15

def main():  

    print('\n╔══════════════════════════╗')
    print('║✨ WELCOME TO NIGHT OWL ✨║')
    print('╚══════════════════════════╝')
    
    print('\nThis script is gonna control the inputs of you pc\nin order to make it look that you are actually watching the OWL')
    print('\nIf at any time you want to interrupt this script\nmove the mouse on the UPPER RIGHT corner of your monitor and hold it there for some seconds')
    print('Try to hold it even tho the program is trying to move it,\nafter a few seconds the program will panic-end and evrything will return to normal')
    
    print('\nEventually you can always combine Alt+Tab (to open this terminal) and then Ctrl+C to force end the script')
    print('Or, if you will ever need, spam Alt+F4')
    
    #print('\nBefore starting be sure to have the owl window already opened in background,\nright after starting this script open the owl tab and leave it in the front')
    #print('The script will firslty refresh the page and then will start, control that everything works at the start so you wont worry about it later :)')
    
    input('\nIs everything clear?\n[No = Ctrl + C, otherwise the input is irrilevant and the script will start]\n > ')
    
    page_arrow_refresh_rate = int(input('Set the refresh rate of the video player (in minutes - minimum of 1)):\n> '))
    page_arrow_refresh_rate = page_arrow_refresh_rate * 60
    
    i = page_arrow_refresh_rate/MOUSE_REFRESH_RATE;
    time.sleep(3)
    
    while True:
    
        if(i == page_arrow_refresh_rate/MOUSE_REFRESH_RATE):
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
    
def refreshVideoPlayer(active = True, rightArrow = False, clicks = 3):
    if active:
        pag.hotkey('ctrl', 'r')
        time.sleep(BROWSER_WAITING_TIME)
        pag.scroll(-800)
        pag.click(200, 500)
        time.sleep(BROWSER_WAITING_TIME)
        if(rightArrow):
            rightArrow(clicks)

def rightArrow(times = 3, active = True):
    if active:
        for i in range(times):
            pag.press('right')
            time.sleep(0.5)
        
main()