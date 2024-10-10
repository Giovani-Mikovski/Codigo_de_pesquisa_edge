import pyautogui
import time

"""
PARTE 2: nível 2

PASSO 01: acessar o start
PASSO 02: clicar no rewards
PASSO 03: coletar bônus de check-in diário
PASSO 04: 
PASSO 05: 
PASSO 06: 
PASSO 07:
"""

'PASSO 01: acessar o start'
pyautogui.press("win")
time.sleep(3)
pyautogui.write("bluestacks")
time.sleep(3)
pyautogui.press("enter")

time.sleep(60)

pyautogui.click(287,440) #Clica em meus jogos
time.sleep(3)
pyautogui.click(502,397) #Clica no start
time.sleep(100)

'PASSO 02: clicar no rewards'
pyautogui.click(750,183) #Clica na área do rewards
time.sleep(5)

'PASSO 03: coletar bônus de check-in diário'
def checkin(px, py):
    pyautogui.click(px, py) #Clica no dia x
    time.sleep(3)

checkin(722,360) #Clica no dia 1
checkin(800,361) #Clica no dia 2
checkin(880,356) #Clica no dia 3
checkin(956,362) #Clica no dia 4
checkin(1034,358) #Clica no dia 5
checkin(1111,361) #Clica no dia 6
checkin(1199,360) #Clica no dia 7



