from database import carregar_dados, guardar_dados_no_json
import os
from datetime import datetime

# Funções para auxilio

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(titulo):
    print("=" * 50)
    print(titulo.center(50))
    print("=" * 50)

# Sistema de login

def tem_usuarios():
    dados = carregar_dados()
    return bool(dados)

def criar_login(login, senha):
    dados = carregar_dados()
    
    if login in dados:
        return False
    
    dados[login] = {
        "senha": senha,
        "tarefas": [],
        "pontos": 0
    }
    guardar_dados_no_json(dados)
    
    return True

def logar(login, senha):
    dados = carregar_dados()

    return login in dados and dados[login]["senha"] == senha

def redefinir_senha(login, nova_senha):
    dados = carregar_dados()
    
    if login not in dados:
        return False
    
    dados[login]["senha"] = nova_senha
    guardar_dados_no_json(dados)
    
    return True
    
# Adicionar função para excluir conta junto de todas as tarefas (N sei se vai no automatico, vou descobrir)
def excluir_usuario(login):
    dados = carregar_dados()
    
    if login in dados:
        del dados[login]
        guardar_dados_no_json(dados)
        return True

# Função de tarefas

def adicionar_tarefa(login, descricao, dificuldade, data_limite):
    dados = carregar_dados()
    
    if login not in dados:
        return False

    valores = {
        "1": 5,
        "2": 10,
        "3": 20
    }
    if dificuldade not in valores:
        return False
    
    nova_tarefa = {
        "descricao": descricao,
        "concluida": False,
        "dificuldade": dificuldade,
        "valor": valores[dificuldade],
        "criada_em": datetime.now().strftime("%d/%m/%Y"),
        "data_limite": data_limite
    }
    
    dados[login]["tarefas"].append(nova_tarefa)
    guardar_dados_no_json(dados)
    
    return True

def listar_tarefas(login):
    dados = carregar_dados()
    
    if login not in dados:
        return []
    
    return dados[login]["tarefas"]

def excluir_tarefa(login, posicao):
    dados = carregar_dados()
    
    if login not in dados:
        return False
    
    tarefas = dados[login]["tarefas"]
    
    if 0 <= posicao < len(tarefas):
        del tarefas[posicao]
        guardar_dados_no_json(dados)
        return True

    return False

def marcar_concluida(login, posicao):
    dados = carregar_dados()
    
    if login not in dados:
        return False
    
    tarefas = dados[login]["tarefas"]
    
    if 0 <= posicao < len(tarefas):
        if tarefas[posicao]["concluida"] == True:
            return False
        
        tarefas[posicao]["concluida"] = True
        pontos = tarefas[posicao].get("valor", 0)
        dados[login]["pontos"] = dados[login].get("pontos", 0) + pontos
        guardar_dados_no_json(dados)
        return True

    return False