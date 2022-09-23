import pyautogui

import time
import pyperclip
import os
import shutil

#abre o navegador
pyautogui.PAUSE = 1
pyautogui.press('winleft')

pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')

#abre o drive
link = 'https://drive.google.com/drive/folders/1KlpEd8rfJiWP237HW8zEhobL44vBE3DA'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(7)
