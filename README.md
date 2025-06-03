# Projeto de Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web utilizando Python e a biblioteca PyAutoGUI. Ideal para processos repetitivos que envolvem preenchimento de formulários baseados em uma planilha CSV.

## Funcionalidades
- Abertura automática do navegador
- Login no sistema de cadastro
- Leitura de dados via `pandas` de um arquivo `produtos.csv`
- Cadastro automático linha a linha utilizando PyAutoGUI
- Log de progresso e erros

## Requisitos
- Python 3.8+
- Google Chrome
- Sistema operacional Windows

## Instalação
```bash
pip install -r requirements.txt
```

## Execução
Coloque o arquivo `produtos.csv` na mesma pasta e execute:
```bash
python automacao_produtos.py
```

## Observações
- As coordenadas de clique podem precisar ser ajustadas com o script `pegar_posicao.py`.
- Os dados de login devem ser informados via terminal.

## Autor
Projeto baseado em materiais da Hashtag Programacao (https://hashtagtreinamentos.com)


pegar_posicao.py
----------------
import time
import pyautogui

print("Você tem 5 segundos para posicionar o mouse...")
time.sleep(5)
print("Posição atual do mouse:", pyautogui.position())
pyautogui.scroll(200)


produtos.csv (exemplo)
-----------------------
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Marca A,Tipo X,Categoria 1,10.5,5.2,Produto em promoção
002,Marca B,Tipo Y,Categoria 2,12.0,6.0,
003,Marca C,Tipo Z,Categoria 1,8.75,4.1,Estoque limitado
"""



