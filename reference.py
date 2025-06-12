import pyautogui
import time

# Wait for you to manually focus the Chrome window
time.sleep(5)

# Simulate Ctrl + S
pyautogui.hotkey('ctrl', 's')

# Wait for the save dialog to appear
time.sleep(2)

# Enter file name (optional)
pyautogui.write('C:Users/laptop/Desktop/web3/Web_Scraper/web.html')

# Press Enter to save
pyautogui.press('enter')


