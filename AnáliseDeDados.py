import pyautogui

import time
import pyperclip
import os
import shutil

# #abre o navegador
# pyautogui.PAUSE = 1
# pyautogui.press('winleft')
#
# pyautogui.write('chrome')
# pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 't')
#
# #abre o drive
# link = 'https://drive.google.com/drive/folders/1KlpEd8rfJiWP237HW8zEhobL44vBE3DA'
# pyperclip.copy(link)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')
# time.sleep(7)
#
# #faz download da base de dados
# pyautogui.click(x=387, y=382, button='right')
# pyautogui.click(x=530, y=844)
# time.sleep(10)

#Coleta ultimo arquivo que foi feito download
origem = r'C:\Users\jonat\Downloads'
destino = r'C:\Users\jonat\Documents\Meus Projetos\Python\Projeto 1 Automação de Análise de Dados\Analise-de-Dados\Histórico Base de Dados'
lista = os.listdir(origem)              #lista os arquivos
list_arq_dat = []                       #lista vazia para receber apenas a data e o arquivo
for arquivo in lista:
    data = os.path.getctime(f"{origem}/{arquivo}")
    list_arq_dat.append((data, arquivo))
list_arq_dat.sort(reverse=True)
ultimo_arq = list_arq_dat[0]            #primeiro índice da lista de arquivos
print(ultimo_arq[1])                   #segundo índice sobre a linha coletada na lista de arquivos

#move arquivo para outra pasta para manter um backup/log

lista2 = os.listdir(destino)
print(lista2)
for cont, arch in enumerate(lista2):
    if 'Vendas - Dez.xlsx' in lista2:
        os.rename(r'C:\Users\jonat\Downloads\Vendas - Dez.xlsx', r'C:\Users\jonat\Documents\Meus Projetos\Python\Projeto 1 Automação de Análise de Dados\Analise-de-Dados\Histórico Base de Dados/Vendas - Dez - Copy'+str(cont)+'.xlsx')
    # else:
    #     shutil.move(f'{origem}/{ultimo_arq[1]}', destino)
