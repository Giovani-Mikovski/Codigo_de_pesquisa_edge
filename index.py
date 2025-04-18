"CÓDIGO DE PESQUISA NO EDGE"

"""
PASSO 01: acessar o edge
PASSO 02: pesquisar - digitar e enter (10 vezes)
PASSO 03: clicar na "medalha" e em "exibr painel"
PASSO 04: fazer conjunto diário
PASSO 05: rolar e fazer mais atividades
"""

"Bibliotecas"
import pyautogui #Controla mouse e teclado
import time #Controla o tempo
import pandas as pd #Lê a tabela de termos de pesquisa
import random #Gera números aleatórios

pyautogui.PAUSE=0.5 #Espera o sistema iniciar

'PASSO 1: acessar o edge'
pyautogui.press("win")
time.sleep(3)
pyautogui.write("edge")
time.sleep(3)
pyautogui.press("enter")

'PASSO 2: pesquisar - digitar e enter (10 vezes)'
tabela_termos=pd.read_csv("termos_pesquisa.csv") #Lê os termos

Posicoes=[]
while len(Posicoes)<=15: #Faz 16 pesquisas para garantir que não repete
    posicao_termo=random.randint(1,149) #Gera um número aleatório entre 1 e 149 que será utilzado como index
    if posicao_termo in Posicoes: #Se o termo já foi pesquisado, passe
        pass
    else: #Se o termo não foi pesquisado, faça
        Posicoes.append(posicao_termo)
        termo=tabela_termos.loc[posicao_termo,"termos"] #Pega o termo do index definido acima
        time.sleep(1.5)
        pyautogui.write(str(termo)) #Escreve na pesquisa do edge
        pyautogui.press("enter")
        time.sleep(5)

'PASSO 03: clicar na "medalha" e em "exibr painel"'
#Quando tem o celular
pyautogui.click(x=1615, y=152, duration=2) #Clica na "medalha"

#Quando NÃO tem o celular
#pyautogui.click(x=1741, y=151, duration=2) #Clica na "medalha"
time.sleep(3)

pyautogui.click(x=1772, y=211, duration=1) #Clica em "Exibir painel"

'PASSO 04: fazer conjunto diário'
time.sleep(5)
pyautogui.scroll(-100) #Rola para chegar em conjunto diário

def conjunto_diario(px, py):
    pyautogui.click(px, py, duration=1) #Clica no quadrado
    time.sleep(5)
    pyautogui.hotkey("ctrl","w") #Fecha a guia
    time.sleep(3)

conjunto_diario(424,1023) #Clica no quadrado 1
conjunto_diario(1163,1009) #Clica no quadrado 2
conjunto_diario(1603,1012) #Clica no quadrado 3

'PASSO 05: rolar e fazer mais atividades'
time.sleep(3)
pyautogui.scroll(-1000) #Rola para chegar em mais atividades

def mais_atividades(px, py):
    pyautogui.click(px, py, duration=1) #Clica no quadrado
    time.sleep(5)
    pyautogui.hotkey("ctrl","w") #Fecha a guia
    time.sleep(3)

mais_atividades(304,361) #Clica no quadrado 0 0
mais_atividades(744,410) #Clica no quadrado 0 1
mais_atividades(1158,440) #Clica no quadrado 0 2
mais_atividades(1582,347) #Clica no quadrado 0 3 
mais_atividades(291,916) #Clica no quadrado 1 0
mais_atividades(740,911) #Clica no quadrado 1 1
mais_atividades(1169,890) #Clica no quadrado 1 2
mais_atividades(1609,925) #Clica no quadrado 1 3