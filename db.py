from pymongo import MongoClient
from datetime import datetime

# Conexão com o Atlas
uri = "mongodb+srv://jonasgabriel433_db_user:Jonas123!@cluster0.r1x9qoe.mongodb.net/"
client = MongoClient(uri)

# Banco e coleção
db = client["todo_app"]
tarefas = db["tarefas"]

# Criar nova tarefa
def criar_tarefa(titulo, descricao, status, tags):
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data_criacao": datetime.now(),
        "status": status.lower(),
        "tags": [t.strip().lower() for t in tags],  # tags limpas e minúsculas
        "comentarios": []
    }
    return tarefas.insert_one(nova_tarefa)

# Listar tarefas
def listar_tarefas():
    return list(tarefas.find())

# Buscar por status
def buscar_por_status(status):
    return list(tarefas.find({"status": status.lower()}))

# Buscar por tag
def buscar_por_tag(tag):
    return list(tarefas.find({"tags": tag.lower()}))

# Atualizar status
def atualizar_status(id_tarefa, novo_status):
    return tarefas.update_one(
        {"_id": id_tarefa},
        {"$set": {"status": novo_status.lower()}}
    )

# Adicionar comentário
def adicionar_comentario(id_tarefa, autor, mensagem):
    comentario = {
        "autor": autor,
        "mensagem": mensagem,
        "data": datetime.now()
    }
    return tarefas.update_one(
        {"_id": id_tarefa},
        {"$push": {"comentarios": comentario}}
    )

# Deletar tarefa
def deletar_tarefa(id_tarefa):
    return tarefas.delete_one({"_id": id_tarefa})

# Exibir tarefa formatada
def mostrar_tarefa(t):
    print("\n-----------------------------")
    print(f"ID: {t['_id']}")
    print(f"Título: {t['titulo']}")
    print(f"Descrição: {t['descricao']}")
    print(f"Status: {t['status']}")
    print(f"Tags: {', '.join(t['tags'])}")
    print(f"Data de criação: {t['data_criacao']}")

    if t["comentarios"]:
        print("Comentários:")
        for c in t["comentarios"]:
            print(f"  - {c['autor']}: {c['mensagem']} ({c['data']})")
    else:
        print("Comentários: Nenhum")

    print("-----------------------------")
