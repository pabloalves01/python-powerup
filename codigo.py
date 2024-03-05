# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.2


# pyautogui.click -> clica em algum lugar da tela
# pyautogui.write -> escreve um texto
# pyautogui.press -> pressiona uma tecla do teclado
#pyautogui.hotkey('ctrl', 'c') -> combinaçao de teclas

# abrir o navegador
# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo de cadastro até acabar

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = 'dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(2);

pyautogui.click(x=841, y=555)
pyautogui.write('pabloalveszimba@gmail.com')
pyautogui.press('tab')
pyautogui.write('password')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2);

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=993, y=393)

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[ linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']

    if not pandas.notna(obs):
            pyautogui.write(str(tabela.loc[linha, 'obs']))

    pyautogui.press('tab')
    pyautogui.press('enter')
    
# pyautogui.scroll(5000) -> Scroll para voltar pro Inicio da Tela









