import pyautogui
import time
import pyperclip
import os
import shutil
import pandas as pd

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

#faz download da base de dados
pyautogui.click(x=387, y=382, button='right')
pyautogui.click(x=530, y=844)
time.sleep(10)

#Faz a leitura da nossa base de dados
db = pd.read_excel(r'C:\Users\jonat\Downloads\Vendas - Dez.xlsx')
print(db)


#Calcula Faturamento e Quantidade de Produtos
faturamento = db['Valor Final'].sum()
qtde_produtos = db['Quantidade'].sum()
print(faturamento, qtde_produtos)


#abrindo o gmail em nova aba
pyautogui.hotkey('ctrl', 't')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
time.sleep(5)

#Criando um novo e-mail
pyautogui.click(x=78, y=161)
pyautogui.write('jdeveloperanalyst@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = 'Relatório de Vendas de Ontem'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f'''
Prezados, bom dia!

O faturamento de ontem foi de: R${faturamento:,.2f}.
A quantidade de produtos foi de: {qtde_produtos:,}

Abs
Jonatas Silva'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.press('enter')


#Coleta ultimo arquivo que foi feito download (pasta de origem)
origem = r'C:\Users\jonat\Downloads'
destino = r'C:\Users\jonat\Documents\Meus Projetos\Python\Projeto 1 Automação de Análise de Dados\Analise-de-Dados\Histórico Base de Dados'
lista = os.listdir(origem)  # lista os arquivos
list_arq_dat = []  # lista vazia para receber apenas a data e o arquivo
for arquivo in lista:
    data = os.path.getctime(f"{origem}/{arquivo}")
    list_arq_dat.append((data, arquivo))
list_arq_dat.sort(reverse=True)
ultimo_arq = list_arq_dat[0]  #primeiro índice da lista de arquivos
print(ultimo_arq[1])  #segundo índice sobre a linha coletada na lista de arquivos

#Mostra todos os arquivos sobre a pasta historico base de dados (pasta destino)
lista2 = os.listdir(destino)
print(lista2)

#Move arquivo para outra pasta para manter um backup/log
if 'Vendas - Dez.xlsx' not in lista2:
    shutil.move(f"{origem}/{ultimo_arq[1]}", destino)
else:
    cont = 0
    for linha in lista2:
        if 'Vendas' in linha:
            cont += 1
    shutil.move(f"{origem}/{ultimo_arq[1]}", f'{destino}/Vendas - Dez({cont}).xlsx')
