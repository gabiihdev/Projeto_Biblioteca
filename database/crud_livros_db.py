from database.conectar_banco import *

def cadastrar_livro_db(titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("INSERT INTO livros (titulo, ISBN, genero, data_publicacao, qtd_paginas, qtd_exemplares) VALUES (?, ?, ?, ?, ?, ?)",
            (titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares))
        conn.commit()
        
    except Exception as e:
        print("\n>> ERRO AO CADASTRAR LIVRO: {e}")
        
    finally:
        desconectar(conn, cursor)


def listar_livros_db():
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT * FROM livros")
        return cursor.fetchall()

    except Exception as e:
        print(f"\n>> ERRO AO LISTAR LIVROS: {e}")

    finally:
        desconectar(conn, cursor)


def buscar_livro_db(livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        if livro.isdigit():
            cursor.execute("SELECT * FROM livros WHERE id_livro = ?", (int(livro),))
        else:
            cursor.execute("SELECT * FROM livros WHERE LOWER(titulo) = ?", (livro.lower(),))
            
        return cursor.fetchone()
    
    except Exception as e:
        print(F"\n>> ERRO AO BUSCAR LIVRO: {e}")

    finally:
        desconectar(conn, cursor)
    

def atualizar_livro_db(titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares, id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("UPDATE livros SET titulo = ?, isbn = ?, genero = ?, data_publicacao = ?, qtd_paginas = ?, qtd_exemplares = ? WHERE id_livro = ?",
            (titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares, id_livro))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO ATUALIZAR LIVRO: {e}")
        
    finally:
        desconectar(conn, cursor)


def deletar_livro_db(id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("DELETE FROM livros WHERE id_livro = ?", (id_livro,))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO DELETAR LIVRO: {e}")
    
    finally:
        desconectar(conn, cursor)


def verificar_livro(isbn, titulo, id_livro=None):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        if id_livro:
            cursor.execute("SELECT * FROM livros WHERE isbn = ? AND titulo = ? AND id_livro != ?", (isbn, titulo, id_livro))
        else:
            cursor.execute("SELECT * FROM livros WHERE isbn = ? AND titulo = ?", (isbn, titulo))
                
        return cursor.fetchone() is not None

    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DO LIVRO: {e}")
        
    finally:
        desconectar(conn, cursor)


def verificar_emprestimo_aberto(id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT * FROM emprestimos WHERE id_livro = ? AND data_devolucao IS NULL", (id_livro,))
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n")