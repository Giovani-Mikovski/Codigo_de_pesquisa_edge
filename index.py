"""
PASSO 01: acessar o edge
PASSO 02: digitar e enter (10 vezes)
PASSO 03: 
PASSO 04: 
PASSO 05:
PASSO 06:
"""

import pyautogui #Controla mouse e teclado
import time #Controla o tempo

pyautogui.PAUSE=0.5 #Espera o sistema iniciar

'PASSO 1: acessar o edge'
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

'PASSO 2: digitar e enter'
for i in range(10):
    pyautogui.write("abc")
    pyautogui.press("enter")
    time.sleep(3)

#asf