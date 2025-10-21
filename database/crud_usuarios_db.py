from database.conectar_banco import *

def cadastrar_usuario_db(nome, sobrenome, data_nascimento):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        cursor.execute("INSERT INTO usuarios (nome, sobrenome, data_nascimento) VALUES (?, ?, ?)",(nome, sobrenome, data_nascimento))
        conn.commit()

    except Exception as e:
        print(f"\n>> ERRO AO CADASTRAR USUÁRIO: {e}")
        
    finally:
        desconectar(conn, cursor)
    

def listar_usuarios_db():
    conn, cursor = conectar()
    if not conn:
        return
    
    try:   
        cursor.execute("""
            SELECT u.id_usuario, u.nome, u.sobrenome, u.data_nascimento, COUNT(e.id_livro) AS total_emprestimos
            FROM usuarios u
            LEFT JOIN emprestimos e ON u.id_usuario = e.id_usuario
            GROUP BY u.id_usuario, u.nome, u.sobrenome, u.data_nascimento
            ORDER BY u.id_usuario
        """)
        
        return cursor.fetchall()
    
    except Exception as e:
        print(f"\>> ERRO AO LISTAR USUÁRIOS: {e}")
        
    finally:
        desconectar(conn, cursor)


def buscar_usuario_db(usuario):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        if usuario.isdigit():
            cursor.execute("""
                SELECT u.id_usuario, u.nome, u.sobrenome, u.data_nascimento, COUNT(e.id_livro) AS total_emprestimos
                FROM usuarios u
                LEFT JOIN emprestimos e ON u.id_usuario = e.id_usuario
                WHERE u.id_usuario = ?
                GROUP BY u.id_usuario, u.nome, u.sobrenome, u.data_nascimento
            """, (int(usuario),))
        else:
            partes = usuario.split()
                
            if len(partes) >= 2:
                nome = partes[0]
                sobrenome = " ".join(partes[1:])
                cursor.execute("""
                    SELECT u.id_usuario, u.nome, u.sobrenome, u.data_nascimento, COUNT(e.id_livro) AS total_emprestimos
                    FROM usuarios u
                    LEFT JOIN emprestimos e ON u.id_usuario = e.id_usuario
                    WHERE u.nome = ? AND u.sobrenome = ?
                    GROUP BY u.id_usuario, u.nome, u.sobrenome, u.data_nascimento
                """, (nome, sobrenome))
            else:
                print("\n>> Informe o nome e o sobrenome.")
     
        return cursor.fetchone()

    except Exception as e:
        print(f"\n>> ERRO AO BUSCAR USUÁRIO: {e}")
        
    finally:
        desconectar(conn, cursor)


def atualizar_usuario_db(nome, sobrenome, data_nascimento, id_usuario):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        cursor.execute("UPDATE usuarios SET nome = ?, sobrenome = ?, data_nascimento = ? WHERE id_usuario = ?",
            (nome, sobrenome, data_nascimento, id_usuario))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO ATUALIZAR USUÁRIO: {e}")


def remover_usuario(id_usuario):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        conn.commit()
        
    except Exception as e:
        print(f"\n>> ERRO AO DELETAR USUÁRIO: {e}")
        
    finally:
        desconectar(conn, cursor)


def verificar_usuario(nome, sobrenome, data_nascimento, id_usuario=None):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        if id_usuario:
            cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND sobrenome = ? AND data_nascimento = ? AND id_usuario != ?",
                        (nome, sobrenome, data_nascimento, id_usuario))
        else:
            cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND sobrenome = ? AND data_nascimento = ?", (nome, sobrenome, data_nascimento))
            
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n>> ERRO AO VERFICAR EXISTÊNCIA DE USUÁRIO: {e}")

    finally:
        desconectar(conn, cursor)


def verificar_emprestimo_aberto(id_usuario):
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        cursor.execute("SELECT * FROM emprestimos WHERE id_usuario = ? AND data_devolucao IS NULL", (id_usuario,))
        return cursor.fetchone() is not None
    
    except Exception as e:
        print(f"\n>> ERRO AO VERIFICAR EMPRÉSTIMO ABERTO: {e}")
        
    finally:
        desconectar(conn, cursor)