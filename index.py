import pyautogui
import time

time.sleep(3)

quantidade_blocos = 30  
velocidade = 0.5 


pyautogui.keyDown('shift')
pyautogui.keyDown('a')
pyautogui.keyDown('s')

for i in range(quantidade_blocos):
    pyautogui.click(button='right')  
    time.sleep(velocidade)


pyautogui.keyUp('a')
pyautogui.keyUp('s')

time.sleep(2)
pyautogui.keyUp('shift')
pyautogui.click(button='right')

print("Ponte finalizada!")
