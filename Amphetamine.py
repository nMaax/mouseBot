import pyautogui as pag
import random
import time

# Program to create a bot for the mouse pointer
#
# If you want to close it you have 3 options:
#   1. Moving the pointer on the UPPER-RIGHT corner, it will panic stop pyautogui
#   2. Do Ctrl+Tab to find the console window and then Ctrl+C to close the script
#   3. Spam Alt+F4

refresh_rate = 0

while (refresh_rate < 1 or refresh_rate > 30):
    refresh_rate = int(input("At what refresh rate (seconds) should the pointer update?\nMin value of 1, Max value of 30\n>"))



while True:
    
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    
    pag.moveTo(x,y,0.5)
    
    time.sleep(2)
