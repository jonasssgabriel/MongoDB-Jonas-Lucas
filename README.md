📝 Sistema de Tarefas com Python + MongoDB Atlas

Aplicação simples de gerenciamento de tarefas desenvolvida em Python, utilizando o MongoDB Atlas como banco de dados.
O projeto implementa um CRUD completo com:

✔ Criar tarefas

✔ Listar tarefas

✔ Atualizar status

✔ Buscar por status

✔ Buscar por tags

✔ Adicionar comentários

✔ Deletar tarefas

A aplicação usa uma interface simples via terminal e possui código modular dividido em db.py (funções do banco) e main.py (menu principal).

📂 Estrutura do Projeto
MongoDB-Jonas-Lucas/
 ├── db.py           # Funções do CRUD e conexão com o MongoDB
 ├── main.py         # Menu principal da aplicação
 ├── README.md       # Documentação do projeto
 └── .vscode/        # Configurações do VS Code

🚀 Como rodar
1. Instale as dependências
pip install pymongo
pip install dnspython

2. Configure sua connection string no db.py
uri = "mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/"

3. Execute a aplicação:
python main.py

📌 Funcionalidades
✔ Criar Tarefa

Inclui título, descrição, status e múltiplas tags.

✔ Listar Tarefas

Mostra todas as tarefas armazenadas no banco.

✔ Buscar por Status

Ex.:

pendente
concluida
em_andamento

✔ Buscar por Tag

Busca mesmo com letras maiúsculas/minúsculas diferentes.

✔ Atualizar Status

Altera o status através do ID da tarefa.

✔ Comentários

Permite adicionar múltiplos comentários em uma tarefa.

✔ Deletar

Remove a tarefa permanentemente.

🧱 Modelo de Documento
{
  "titulo": "Fazer atividade",
  "descricao": "Entregar hoje",
  "data_criacao": "timestamp",
  "status": "pendente",
  "tags": ["estudos", "urgente"],
  "comentarios": [
    {
      "autor": "Jonas",
      "mensagem": "Começar agora",
      "data": "timestamp"
    }
  ]
}

👥 Contribuidores

Jonas Gabriel (@jonasssgabriel) – criador principal

Lucas (@LuckLeal) – colaborador e suporte geral

📄 Licença

Este projeto é livre para estudo e uso acadêmico.

📬 Contato

Github do autor: github.com/jonasssgabriel
