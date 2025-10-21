# Projeto - Biblioteca

É uma aplicação de biblioteca utilizando Python, SQLite e web scraping. Permite cadastrar, listar, buscar, atualizar e deletar autores, livros, usuários e empréstimos, utilizando um banco SQLite local e dados coletados via web scraping.

---

## Estrutura do Projeto

```bash
projeto_biblioteca/
│
├─ database/ # funções que acessam o banco diretamente
│ ├─ conectar_banco.py
│ ├─ crud_autores_db.py
│ ├─ crud_emprestimos_db.py
│ ├─ crud_livros_autores_db.py
│ ├─ crud_livros_db.py
│ └─ crud_usuarios_db.py
│
├─ servicos/ # funções que interagem com o usuário e chamam o CRUD
│ ├─ crud_autores.py
│ ├─ crud_emprestimos.py
│ ├─ crud_livros_autores.py
│ ├─ crud_livros.py
│ └─ crud_usuarios.py
│
├─ utils/ # funções auxiliares
│ ├─ mensagens.py
│ └─ validacoes.py
│
├─ menus.py # menus e interação principal
├─ scraping.py # coleta dados da web e insere no banco
├─ criar_banco.py # cria o banco SQLite vazio
├─ requirements.txt # bibliotecas externas necessárias
└─ README.md # este arquivo

```
---

## Instalação das Dependências

1 . Crie um ambiente virtual (opcional, mas recomendado):

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

2 . Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

### Dependências principais:

- tabulate → exibir tabelas no terminal
- requests → web scraping
- beautifulsoup4 → web scraping
- pandas → manipulação de dados
- lxml → parser HTML/XML

O SQLite já vem com Python, não precisa instalar.

---

## Fluxo de Execução

1 . Criar o banco SQLite vazio:

```
python criar_banco.py
```

2 . Popular o banco com dados do web scraping:

```
python scraping.py
```

3 . Usar o CRUD via menus:

```
python menus.py
```

Internamente, todos os CRUDs já gerenciam a conexão com o banco (conectar_banco.py). Não é necessário conectar ou desconectar manualmente.

---

## Funcionalidades por CRUD

- Autores: cadastrar, listar, buscar, atualizar, deletar
- Livros: cadastrar, listar, buscar, atualizar, deletar
- Usuários: cadastrar, listar, buscar, atualizar, deletar
- Empréstimos: cadastrar, listar, buscar, atualizar, deletar, devoluções
- Livros-Autores: vincular livros a autores, buscar livros de autores

---

## Observações

- O arquivo biblioteca.db não está incluído; ele será gerado ao rodar os scripts.
- Projeto voltado para uso acadêmico e aprendizado.
- Para qualquer alteração ou adição de dados, utilize os CRUDs via menus.py.
- Estrutura modular facilita manutenção e expansão futura.

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---