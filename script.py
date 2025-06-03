# automacao_produtos.py
import pyautogui
import time
import pandas as pd
import logging
import getpass
from tqdm import tqdm

# Configurações iniciais
time.sleep(2)  # Tempo para o usuário se preparar
pyautogui.PAUSE = 0.5
logging.basicConfig(filename='log.txt', level=logging.INFO)

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")
    time.sleep(3)

def fazer_login(email, senha):
    pyautogui.click(x=685, y=451)  # Campo email
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.click(x=955, y=638)  # Botão login
    time.sleep(3)

def cadastrar_produto(produto):
    pyautogui.click(x=653, y=294)  # Campo código
    pyautogui.write(str(produto["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["custo"]))
    pyautogui.press("tab")
    obs = produto.get("obs", "")
    if pd.notna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")  # Enviar
    pyautogui.scroll(5000)

def main():
    print("Iniciando automação...")
    email = input("Digite seu email: ")
    senha = getpass.getpass("Digite sua senha: ")

    abrir_navegador()
    fazer_login(email, senha)

    try:
        tabela = pd.read_csv("produtos.csv")
    except Exception as e:
        logging.error(f"Erro ao ler CSV: {e}")
        return

    for i in tqdm(tabela.index):
        try:
            cadastrar_produto(tabela.loc[i])
            logging.info(f"Produto {tabela.loc[i]['codigo']} cadastrado com sucesso")
        except Exception as e:
            logging.error(f"Erro ao cadastrar produto {i}: {e}")

    print("Cadastro finalizado.")

if __name__ == "__main__":
    main()