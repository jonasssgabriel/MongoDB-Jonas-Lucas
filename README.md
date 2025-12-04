# Sistema de Tarefas – Python + MongoDB Atlas

Aplicação simples de gerenciamento de tarefas construída em **Python**, utilizando **MongoDB Atlas** como banco de dados.  
O projeto conta com operações completas de CRUD, busca por status, busca por tags e suporte a comentários — tudo via terminal.

---

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefas por status
- Buscar tarefas por tag
- Atualizar status
- Adicionar comentários
- Deletar tarefas

---

## Estrutura do Projeto

```
MongoDB-Jonas-Lucas/
 ├── db.py        # Conexão e operações CRUD com o MongoDB
 ├── main.py      # Menu principal e interação com o usuário
 ├── README.md    # Documentação do projeto
 └── .vscode/     # Configurações do VS Code (opcional)
```

---

## Como Executar

### 1) Instale as dependências
```bash
pip install pymongo
pip install dnspython
```

### 2) Configure sua connection string em `db.py`
```python
uri = "mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/"
```

### 3) Execute o programa
```bash
python main.py
```

---

## Modelo de Documento (MongoDB)

```json
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
```

---

## Colaboradores

| Nome                  | GitHub                       |
|---------------------- |------------------------------|
| Jonas Gabriel         | https://github.com/jonasssgabriel |
| Lucas (LuckLeal)      | https://github.com/LuckLeal |

---

## Licença

Projeto desenvolvido para fins acadêmicos e estudo.  
Sinta-se livre para utilizar, modificar e melhorar.
