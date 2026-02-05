## ✅ Task List

Aplicação web desenvolvida em **Django** para gerenciamento de tarefas, permitindo a criação, organização e acompanhamento de **to-dos** com suporte a **tags**, prazos e status de conclusão.

O projeto foi desenvolvido com foco em **CRUD completo**, **relacionamentos Many-to-Many**, **organização de dados** e boas práticas de desenvolvimento back-end.

---

## 🚀 Funcionalidades

- CRUD completo de tarefas
- CRUD de tags
- Associação de múltiplas tags a uma tarefa (Many-to-Many)
- Definição de:
  - data de criação
  - deadline da tarefa
- Marcação de tarefas como concluídas
- Ordenação automática:
  - tarefas pendentes primeiro
  - tarefas concluídas ao final da lista
- Páginas separadas para:
  - gerenciamento de tarefas
  - gerenciamento de tags

---

## 📦 Instalação e execução local

Clone o repositório:

```bash
git clone https://github.com/EduardoMoen/task-list/
cd task-list
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Aplique as migrations:

```bash
python manage.py migrate
```

Execute o servidor:

```bash
python manage.py runserver
```

## ⚙️ Variáveis de ambiente

Crie um arquivo .env na raiz do projeto.
Atualmente, o projeto utiliza apenas a variável DJANGO_SECRET_KEY.

---
