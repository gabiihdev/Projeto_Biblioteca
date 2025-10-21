import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

def criar_banco():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome CHAR(50) NOT NULL,
        pais_origem CHAR(30) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo CHAR(50) NOT NULL,
        ISBN CHAR(20) UNIQUE NOT NULL,
        genero CHAR(30) NOT NULL,
        data_publicacao DATE NOT NULL,
        qtd_paginas INTEGER NOT NULL,
        qtd_exemplares INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros_autores (
        id_livro INTEGER NOT NULL,
        id_autor INTEGER NOT NULL,
        PRIMARY KEY(id_livro, id_autor),
        FOREIGN KEY(id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE,
        FOREIGN KEY(id_autor) REFERENCES autores(id_autor) ON DELETE CASCADE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome CHAR(20) NOT NULL,
        sobrenome CHAR(20) NOT NULL,
        data_nascimento DATE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (
        id_livro INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        FOREIGN KEY(id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE
    )
    ''')

    # Criação de um trigger para verificar se os empréstimos dos usuários estão dentodentro do limite (5)

    cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS verificar_max_emprestimos
    BEFORE INSERT ON emprestimos
    FOR EACH ROW
    WHEN (SELECT COUNT(*) FROM emprestimos WHERE id_usuario = NEW.id_usuario AND data_devolucao IS NULL) >= 5
    BEGIN
        SELECT RAISE(ABORT, 'O usuário já atingiu o limite de 5 empréstimos.');
    END;
    ''')

    conn.commit()
    conn.close()
    
    print("Banco de dados 'biblioteca.db' criado com sucesso!!")

criar_banco()
