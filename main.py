from bson import ObjectId
from db import *

# Loop do menu
while True:
    print("\n========= LISTA DE TAREFAS =========")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Buscar por status")
    print("4 - Buscar por tag")
    print("5 - Atualizar status")
    print("6 - Adicionar comentário")
    print("7 - Deletar tarefa")
    print("0 - Sair")
    print("====================================")

    op = input("Escolha: ")

    # Criar tarefa
    if op == "1":
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        status = input("Status (pendente/em_andamento/concluida): ").lower()
        tags = [t.strip().lower() for t in input("Tags separadas por vírgula: ").split(",")]
        criar_tarefa(titulo, descricao, status, tags)
        print("\n✔ Tarefa criada!")

    # Listar tarefas
    elif op == "2":
        lista = listar_tarefas()
        if not lista:
            print("\nNenhuma tarefa.")
        for t in lista:
            mostrar_tarefa(t)

    # Buscar por status
    elif op == "3":
        status = input("Status: ").lower()
        resultados = buscar_por_status(status)
        if not resultados:
            print("\nNada encontrado.")
        for t in resultados:
            mostrar_tarefa(t)

    # Buscar por tag
    elif op == "4":
        tag = input("Tag: ").strip().lower()
        resultados = buscar_por_tag(tag)
        if not resultados:
            print("\nNada encontrado.")
        for t in resultados:
            mostrar_tarefa(t)

    # Atualizar status
    elif op == "5":
        id_tarefa = ObjectId(input("ID: "))
        novo_status = input("Novo status: ").lower()
        atualizar_status(id_tarefa, novo_status)
        print("\n✔ Status atualizado!")

    # Adicionar comentário
    elif op == "6":
        id_tarefa = ObjectId(input("ID: "))
        autor = input("Autor: ")
        msg = input("Mensagem: ")
        adicionar_comentario(id_tarefa, autor, msg)
        print("\n✔ Comentário adicionado!")

    # Deletar tarefa
    elif op == "7":
        id_tarefa = ObjectId(input("ID: "))
        deletar_tarefa(id_tarefa)
        print("\n✔ Tarefa deletada!")

    # Sair
    elif op == "0":
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida.")
