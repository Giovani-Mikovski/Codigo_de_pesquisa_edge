
"""
PASSO 01: acessar o edge
PASSO 02: digitar e enter (10 vezes)
PASSO 03: clicar na "medalha" e em "exibr painel"
PASSO 04: fazer conjunto diário
PASSO 05:
PASSO 06:
"""

import pyautogui #Controla mouse e teclado
import time #Controla o tempo
'''
pyautogui.PAUSE=0.5 #Espera o sistema iniciar

'PASSO 1: acessar o edge'
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

'PASSO 2: digitar e enter (10 vezes)'
for i in range(10):
    pyautogui.write("abc")
    pyautogui.press("enter")
    time.sleep(3)

'PASSO 03: clicar na "medalha" e em "exibr painel"'
pyautogui.click(x=1745, y=146) #Clicar na "medalha"
time.sleep(3)

pyautogui.click(x=1777, y=208) #Clicar em "Exibir painel"
time.sleep(10)
'''
'PASSO 04: fazer conjunto diário'
time.sleep(10)

pyautogui.click(x=563, y=912) #Clica no quadrado 1
time.sleep(5)
pyautogui.hotkey('ctrl','w') # Fecha a guia
time.sleep(3)

pyautogui.click(x=1163, y=936) #Clica no quadrado 2
time.sleep(5)
pyautogui.hotkey('ctrl','w') # Fecha a guia
time.sleep(3)

pyautogui.click(x=1593, y=923) #Clica no quadrado 3
time.sleep(5)
pyautogui.hotkey('ctrl','w') # Fecha a guia
time.sleep(3)
