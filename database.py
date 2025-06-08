import json
import os

def obter_caminho_do_arquivo():
    # Para pegar o nome do computador do usuário
    nome_do_computador = os.path.expanduser("~")
    # Endereço da pasta 
    caminho_da_pasta = os.path.join(nome_do_computador, "Desktop", "Projeto Final")
    # Serve para criar a pasta caso ela não exista, eu espero
    os.makedirs(caminho_da_pasta, exist_ok = True)
    nome_do_arquivo = "dados.json"
    # Endereço do arquivo 
    caminho_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)
    
    return caminho_do_arquivo

def guardar_dados_no_json(dados):
    caminho = obter_caminho_do_arquivo()
    with open(caminho, "w") as arquivo:
        json.dump(dados, arquivo, indent = 2)

def carregar_dados():
    caminho = obter_caminho_do_arquivo()
    if os.path.exists(caminho):
        with open(caminho, "r") as arquivo:
            return json.load(arquivo)
    dados = {}
    return dados
