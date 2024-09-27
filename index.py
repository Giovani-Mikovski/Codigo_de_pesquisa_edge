
"""
PASSO 01: acessar o edge
PASSO 02: digitar e enter (10 vezes)
PASSO 03: clicar na "medalha" e em "exibr painel"
PASSO 04: fazer conjunto diário
PASSO 05: rolar e fazer mais atividades
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

'PASSO 04: fazer conjunto diário'
time.sleep(10)

pyautogui.click(x=563, y=912) #Clica no quadrado 1
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=1163, y=936) #Clica no quadrado 2
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=1593, y=923) #Clica no quadrado 3
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)
'''
'PASSO 05: rolar e fazer mais atividades'
time.sleep(10)
pyautogui.scroll(-1100) # Rola para chegar em mais atividades

pyautogui.click(x=304, y=361) #Clica no quadrado 0 0
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=744, y=410) #Clica no quadrado 0 1
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=1169, y=305) #Clica no quadrado 0 2
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=289, y=795) #Clica no quadrado 1 0
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=714, y=818) #Clica no quadrado 1 1
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=1155, y=780) #Clica no quadrado 1 2
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)

pyautogui.click(x=1568, y=791) #Clica no quadrado 1 3
time.sleep(5)
pyautogui.hotkey("ctrl","w") # Fecha a guia
time.sleep(3)