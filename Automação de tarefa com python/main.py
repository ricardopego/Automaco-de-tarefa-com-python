# PASSO A PASSO
# pg.write()  escrever texto
# pg.press()  apertar tecla do teclado ou mouse
# pg.click()  clicar em algum lugar da tela
# pg.hotkey('alt','tab')  combinação de teclas
# Link: https://dlp.hastagtreinamentos.com/python/intensivao/login

# Passo 1: Entrar no sistema da empresa
import pyautogui
import time

def main():
    start_time = time.time()  # Captura o tempo inicial

    #pyautogui.PAUSE = 0.3 # tempo de espera em cada um dos comandos

    # Abrir o navegador chorme
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('chorme')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)

    # Entar no site
    
    pyautogui.hotkey('ctrl','l')
    pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('win','up')
    time.sleep(1)

    # Passo 2: Fazer login
    # Selecionar e-mail
    pyautogui.click(x=580, y=497)
    time.sleep(0.5)
    # Escrever no e-mail
    pyautogui.write('ricardinho.pego07@gmail.com')
    time.sleep(0.5)
    # Escrever senha
    pyautogui.press('tab')
    pyautogui.write('12345678')
    time.sleep(0.5)

    # Clicar no botão de login
    pyautogui.click(x=791, y=693)

    # Passo 3: Importar a base de produtos para cadastrar
    import pandas as pd

    tabela = pd.read_csv('produtos.csv')
    print(tabela)

    # Passo 4: Cadastrar produtos
    for linha in tabela.index:  # Paaso 5: Repetir o processo de cadastro até o fim. Por isso usar o for aqui, assim serão cadastrados produtos da primeira linha até a ultima.
        print(linha)

        # Clicar no campo de código
        pyautogui.click(x=1005, y=350)

        # Pegar da tabela o valor que eu quero preencher
        codigo = tabela.loc[linha, 'codigo']

        # Preencher campo
        pyautogui.write(str(codigo))

        # passar para o próximo campo
        pyautogui.press('tab') 

        # Preencher campo
        pyautogui.write(str(tabela.loc[linha,'marca']))
        pyautogui.press('tab')
        pyautogui.write(str(tabela.loc[linha,'tipo']))
        pyautogui.press('tab')
        pyautogui.write(str(tabela.loc[linha,'categoria']))
        pyautogui.press('tab')
        pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
        pyautogui.press('tab')
        pyautogui.write(str(tabela.loc[linha,'custo']))
        pyautogui.press('tab')

        obs = tabela.loc[linha,'obs']
        if not pd.isna(obs):
            pyautogui.write(str(tabela.loc[linha,'obs']))
        else:
            pyautogui.press('tab')

        # Clicar em logar
        pyautogui.press('enter')

        # Dar scrool no mouse para cima
        time.sleep(0.5)
        pyautogui.scroll(5000)
        time.sleep(0.5)

        end_time = time.time()  # Captura o tempo final
        elapsed_time = (end_time - start_time)/60  # Calcula o tempo decorrido
        segundos = end_time - start_time
        print(f"O programa executou em {elapsed_time:.2f} minutos.")

if __name__ == "__main__":
    main()
