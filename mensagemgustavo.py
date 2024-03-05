import pyautogui
import time

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')

pyautogui.click(x=545, y=273)
pyautogui.write('Oi, a automação que enviou essa mensagem!')
pyautogui.press('tab')
time.sleep(2);
pyautogui.press('enter')


