from database.conectar_banco import *

def cadastrar_autor_db( nome, pais_origem):
    conn, cursor = conectar()
    if not conn or not cursor:
        return   
    
    try:
        cursor.execute("INSERT INTO autores (nome, pais_origem) VALUES (?, ?)", (nome, pais_origem))
        conn.commit()
    
    except Exception as e:
        print(f"\n>> ERRO AO CADASTRAR AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)


def verificar_autor(nome, pais_origem, id_autor=None):
    conn, cursor = conectar()
    if not conn or not cursor:
        return   
    
    try:
        if id_autor:
            cursor.execute("SELECT * FROM autores WHERE nome = ? AND pais_origem = ? AND id_autor != ?", (nome, pais_origem, id_autor))
        else:
            cursor.execute("SELECT * FROM autores WHERE nome = ? AND pais_origem = ?", (nome, pais_origem))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DO AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)


def listar_autores_db():
    conn, cursor = conectar()
    if not conn or not cursor:
        return      
    
    try:
        cursor.execute("""
            SELECT a.id_autor, a.nome, a.pais_origem, COUNT(la.id_livro) AS total_livros
            FROM autores a
            LEFT JOIN livros_autores la ON a.id_autor = la.id_autor
            GROUP BY a.id_autor, a.nome, a.pais_origem
            ORDER BY a.id_autor
        """)        
        return cursor.fetchall()
    
    except Exception as e:
        print(f"\n>> ERRO AO LISTAR AUTORES: {e}")
        
    finally:
        desconectar(conn, cursor)


def buscar_autor_db(autor):
    conn, cursor = conectar()
    if not conn or not cursor:
        return   
    
    try:
        if autor.isdigit():
            cursor.execute("""
                SELECT a.id_autor, a.nome, a.pais_origem, COUNT(la.id_livro) AS total_livros
                FROM autores a
                LEFT JOIN livros_autores la ON a.id_autor = la.id_autor
                WHERE a.id_autor = ?
                GROUP BY a.id_autor, a.nome, a.pais_origem
            """, (int(autor),))
        else:
            cursor.execute("""
                SELECT a.id_autor, a.nome, a.pais_origem, COUNT(la.id_livro) AS total_livros
                FROM autores a
                LEFT JOIN livros_autores la ON a.id_autor = la.id_autor
                WHERE LOWER(a.nome) = ?
                GROUP BY a.id_autor, a.nome, a.pais_origem
            """, (autor.lower(),))
        
        return cursor.fetchone()

    except Exception as e:
        print(f"\nERRO AO BUSCAR AUTOR: {e}")
    
    finally:
        desconectar(conn, cursor)


def atualizar_autor_db(nome, pais_origem, id_autor):
    conn, cursor = conectar()
    if not conn or not cursor:
        return
    
    try:
        cursor.execute("UPDATE autores SET nome = ?, pais_origem = ? WHERE id_autor = ?", (nome, pais_origem, id_autor))
        conn.commit()
    
    except Exception as e:
        print(f"\n>> ERRO AO EDITAR AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)


def remover_autor(id_autor):
    conn, cursor = conectar()
    if not conn or not cursor:
        return   
    
    try:
        cursor.execute("DELETE FROM autores WHERE id_autor = ?", (id_autor,))
        conn.commit()
    
    except Exception as e:
        print(f"\n>> ERRO AO DELETAR AUTOR: {e}")
        
    finally:
        desconectar(conn, cursor)