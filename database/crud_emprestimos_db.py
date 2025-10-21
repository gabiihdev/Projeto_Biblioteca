from database.conectar_banco import *

def realizar_emprestimo_db(id_usuario, id_livro, data_emprestimo):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (?, ?, ?)", 
                    (id_usuario, id_livro, data_emprestimo))
        
        cursor.execute("UPDATE livros SET qtd_exemplares = qtd_exemplares - 1 WHERE id_livro = ?", (id_livro,))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO REALIZAR EMPRÉSTIMO: {e}")
        
    finally:
        desconectar(conn, cursor)


def encerrar_emprestimo_db(id_usuario, id_livro, data_devolucao):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("""
            UPDATE emprestimos 
            SET data_devolucao = ? 
            WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NULL
        """, (data_devolucao, id_usuario, id_livro))

        cursor.execute("UPDATE livros SET qtd_exemplares = qtd_exemplares + 1 WHERE id_livro = ?", (id_livro,))
        conn.commit()
        
    except Exception as e:
        print(f"\nERRO AO ENCERRAR EMPRÉSTIMO: {e}")
        
    finally:
        desconectar(conn, cursor)


def listar_todos_emprestimos():
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("""
            SELECT e.id_livro, l.titulo, e.id_usuario, u.nome, u.sobrenome, e.data_emprestimo, e.data_devolucao
            FROM emprestimos e
            JOIN livros l ON e.id_livro = l.id_livro
            JOIN usuarios u ON e.id_usuario = u.id_usuario
        """)
        
        return cursor.fetchall()
    
    except Exception as e:
        print(f"\n>> ERRO AO LISTAR EMPRÉSTIMOS: {e}")
        
    finally:
        desconectar(conn, cursor)


def atualizar_emprestimos_db(novo_id_usuario, novo_id_livro, nova_data_emprestimo, nova_data_devolucao, id_usuario, id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("""
            UPDATE emprestimos
            SET id_usuario = ?, id_livro = ?, data_emprestimo = ?, data_devolucao = ?
            WHERE id_usuario = ? AND id_livro = ?
        """, (novo_id_usuario, novo_id_livro, nova_data_emprestimo, nova_data_devolucao, id_usuario, id_livro))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO ATUALIZAR EMPRÉSTIMOS: {e}")
        
    finally:
        desconectar(conn, cursor)


def deletar_emprestimos_db(id_usuario, id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("DELETE FROM emprestimos WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NOT NULL", (id_usuario, id_livro))
        conn.commit()
    
    except Exception as e:
        print(f"\n>> ERRO AO DELETAR EMPRÉSTIMO: {e}")
        
    finally:
        desconectar(conn, cursor)  
    
        
def verificar_usuario(id_usuario):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT 1 FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DO USUÁRIO: {e}")

    finally:
        desconectar(conn, cursor)


def verificar_livro(id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT * FROM livros WHERE id_livro = ?", (id_livro,))
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DO LIVRO: {e}")


def verificar_emprestimo(id_usuario, id_livro, emprestimo_aberto=False):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        if emprestimo_aberto:
            cursor.execute("SELECT * FROM emprestimos WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NULL", (id_usuario, id_livro))
        else:
            cursor.execute("SELECT * FROM emprestimos WHERE id_usuario = ? AND id_livro = ?", (id_usuario, id_livro))
        
        emprestimo = cursor.fetchone()
        return emprestimo if emprestimo else None

    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EXISTÊNCIA DO EMPRÉSTIMO: {e}")
        
    finally:
        desconectar(conn, cursor)
        

def verificar_qtd_exemplares(id_livro):
    conn, cursor = conectar()
    if not conn and not cursor:
        return
    
    try:
        cursor.execute("SELECT qtd_exemplares FROM livros WHERE id_livro = ?", (id_livro,))
        qtd_exemplares = cursor.fetchone()
        return qtd_exemplares[0] if qtd_exemplares else 0
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR QUANTIDADE DE EXEMPLARES: {e}")
        
    finally:
        desconectar(conn, cursor)