from datetime import datetime
from back import (
    tem_usuarios, criar_login, logar, redefinir_senha, excluir_usuario,
    adicionar_tarefa, listar_tarefas, excluir_tarefa, marcar_concluida,
    limpar_tela, cabecalho
)
from database import carregar_dados

def menu_principal():
    while True:
        limpar_tela()
        cabecalho("Sistema de Tarefas")
        print("1. Login")
        print("2. Criar conta")
        print("3. Redefinir senha")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            login = input("Login: ")
            senha = input("Senha: ")
            if logar(login, senha):
                menu_usuario(login)
            else:
                print("Login ou senha incorretos.")
                input("Pressione Enter para continuar...")

        elif opcao == "2":
            login = input("Novo login: ")
            senha = input("Nova senha: ")
            if criar_login(login, senha):
                print("Conta criada com sucesso.")
            else:
                print("Este login já existe.")
            input("Pressione Enter para continuar...")

        elif opcao == "3":
            login = input("Login: ")
            nova_senha = input("Nova senha: ")
            if redefinir_senha(login, nova_senha):
                print("Senha redefinida com sucesso.")
            else:
                print("Usuário não encontrado.")
            input("Pressione Enter para continuar...")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def menu_usuario(login):
    while True:
        limpar_tela()
        dados = carregar_dados()
        tarefas = listar_tarefas(login)
        pontos = dados[login].get("pontos", 0)


        cabecalho(f"Bem-vindo, {login} | Pontos acumulados: {pontos}")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Excluir tarefa")
        print("5. Excluir minha conta")
        print("6. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            print("Dificuldade: 1 (Fácil), 2 (Média), 3 (Difícil)")
            dificuldade = input("Escolha a dificuldade: ")
            data_limite = input("Data limite (dd/mm/aaaa): ")
            if adicionar_tarefa(login, descricao, dificuldade, data_limite):
                print("Tarefa adicionada com sucesso.")
            else:
                print("Erro ao adicionar tarefa.")
            input("Pressione Enter para continuar...")

        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                for i, tarefa in enumerate(tarefas):
                    status = "✅ Concluída" if tarefa["concluida"] else "⏳ Pendente"
                    print(f"{i}. {tarefa['descricao']} | {status} | Dificuldade: {tarefa['dificuldade']} | Valor: {tarefa['valor']} pts | Limite: {tarefa['data_limite']}")
            input("Pressione Enter para continuar...")

        elif opcao == "3":
            posicao = int(input("Digite o número da tarefa a marcar como concluída: "))
            if marcar_concluida(login, posicao):
                print("Tarefa marcada como concluída.")
            else:
                print("Tarefa não encontrada.")
            input("Pressione Enter para continuar...")

        elif opcao == "4":
            posicao = int(input("Digite o número da tarefa a excluir: "))
            if excluir_tarefa(login, posicao):
                print("Tarefa excluída com sucesso.")
            else:
                print("Erro ao excluir tarefa.")
            input("Pressione Enter para continuar...")

        elif opcao == "5":
            confirmar = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
            if confirmar == "s":
                if excluir_usuario(login):
                    print("Conta excluída com sucesso.")
                    input("Pressione Enter para voltar ao menu principal...")
                    break
                else:
                    print("Erro ao excluir conta.")
            input("Pressione Enter para continuar...")

        elif opcao == "6":
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()