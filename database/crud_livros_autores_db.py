from database.conectar_banco import *

def vincular_livro_autor_db(id_livro, id_autor):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("INSERT INTO livros_autores (id_livro, id_autor) VALUES (?, ?)", (id_livro, id_autor))
        conn.commit()
    
    except Exception as e:
        print(f"\n>> ERRO AO VINCULAR LIVRO A AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)


def buscar_livro_autor_db(autor):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        if autor.isdigit():
            cursor.execute("""
                SELECT l.id_livro, l.titulo, l.isbn, l.data_publicacao, l.genero, l.qtd_paginas, l.qtd_exemplares, a.nome AS autor
                FROM livros l
                JOIN livros_autores la ON l.id_livro = la.id_livro
                JOIN autores a ON a.id_autor = la.id_autor
                WHERE a.id_autor = ?
            """, (int(autor),))
            
        else:
            cursor.execute("""
                SELECT l.id_livro, l.titulo, l.isbn, l.data_publicacao, l.genero, l.qtd_paginas, l.qtd_exemplares, a.nome AS autor
                FROM livros l
                JOIN livros_autores la ON l.id_livro = la.id_livro
                JOIN autores a ON a.id_autor = la.id_autor
                WHERE a.nome = ?
            """, (autor,))

        return cursor.fetchall()
    
    except Exception as e:
        print(f"\n>> ERRO AO BUSCAR LIVRO DE AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)


def verificar_livro(id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT titulo FROM livros WHERE id_livro = ?", (id_livro,))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DE LIVRO: {e}")
        
    finally:
        desconectar(conn, cursor)


def verificar_autor(id_autor):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT nome FROM autores WHERE id_autor = ?", (id_autor,))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DE AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)
        

def verificar_vinculo(id_livro, id_autor):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT * FROM livros_autores WHERE id_livro = ? AND id_autor = ?", (id_livro, id_autor))
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR VÍNCULO ENTRE LIVRO E AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)