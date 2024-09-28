
"""
PASSO 01: acessar o edge
PASSO 02: pesquisa - digitar e enter (10 vezes)
PASSO 03: clicar na "medalha" e em "exibr painel"
PASSO 04: fazer conjunto diário
PASSO 05: rolar e fazer mais atividades
PASSO 06: fechar edge
PASSO 07: exibir notificação na tela
"""

import pyautogui #Controla mouse e teclado
import time #Controla o tempo
import pandas as pd #Lê a tabela de termos de pesquisa
import random #Gera números aleatórios
from winotify import Notification #Notificação 

pyautogui.PAUSE=0.5 #Espera o sistema iniciar

'PASSO 1: acessar o edge'
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

'PASSO 2: pesquisa - digitar e enter (10 vezes)'
tabela_termos=pd.read_csv("termos_pesquisa.csv") #Lê os termos

for i in range(10):
    posicao_termo=random.randint(1,49) #Gera um número aleatório entre 1 e 5 que será utilzado como index
    termo=tabela_termos.loc[posicao_termo,"termos"] #Pega o termo do index definido acima
    pyautogui.write(str(termo)) #Escreve na pesquisa do edge
    pyautogui.press("enter")
    time.sleep(5)

'PASSO 03: clicar na "medalha" e em "exibr painel"'
pyautogui.click(x=1745, y=146) #Clicar na "medalha"
time.sleep(3)

pyautogui.click(x=1777, y=208) #Clicar em "Exibir painel"

'PASSO 04: fazer conjunto diário'
time.sleep(10)
def conjunto_diario(px, py):
    pyautogui.click(px, py) #Clica no quadrado
    time.sleep(5)
    pyautogui.hotkey("ctrl","w") # Fecha a guia
    time.sleep(3)

conjunto_diario(563,912) #Clica no quadrado 1
conjunto_diario(1163,936) #Clica no quadrado 2
conjunto_diario(1593,923) #Clica no quadrado 3

'PASSO 05: rolar e fazer mais atividades'
time.sleep(5)
pyautogui.scroll(-1100) # Rola para chegar em mais atividades

def mais_atividades(px, py):
    pyautogui.click(px, py) #Clica no quadrado
    time.sleep(5)
    pyautogui.hotkey("ctrl","w") # Fecha a guia
    time.sleep(3)

mais_atividades(304,361) #Clica no quadrado 0 0
mais_atividades(744,410) #Clica no quadrado 0 1
mais_atividades(1169,305) #Clica no quadrado 0 2
mais_atividades(1582,347) #Clica no quadrado 0 3 
mais_atividades(289,795) #Clica no quadrado 1 0
mais_atividades(714,818) #Clica no quadrado 1 1
mais_atividades(1155,780) #Clica no quadrado 1 2
mais_atividades(1568,791) #Clica no quadrado 1 3

'PASSO 06: fechar edge'
pyautogui.hotkey("alt","f4") #Fecha o edge

'PASSO 07: exibir notificação na tela'
noticacao=Notification(app_id="Pesquisa no edge", title="Código de pesquisa no edge concluído", msg="Pesquisa automática para pontuação no edge executada com sucesso", duration="long", icon=r"C:\Users\giova\OneDrive\Área de Trabalho\Programação\Codigo_edge\img\icon_py.png") #Descrição das características das notificações

noticacao.show() #Mostra a notificação