import psycopg2
import os
from psycopg2.extras import RealDictCursor
from config.database import get_connection, create_tables, populate_tables
from ascii_arts import name, bye
from math import floor

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def selecionar_save(userId):
    print(userId)

def criar_conta(username, password, conn, cur):
    cur.execute(f"SELECT * FROM usuario WHERE login = %s AND senha = %s",(username,password))
    existe_usuario = cur.fetchall()
    if existe_usuario:
        return None
    cur.execute(f"INSERT INTO usuario (login, senha) VALUES (%s, %s) RETURNING idusuario;",(username,password))
    userId = cur.fetchone()
    conn.commit()
    return userId
    

def validar_login(username, password, cur):
    cur.execute(f"SELECT * FROM usuario WHERE login = %s AND senha = %s",(username,password))
    user = cur.fetchall()
    if user:
        return user[0]
    return None
    
def sair():
    print(bye)
    exit()
        
def mover_personagem(conn, cur, personagemId, direcao):
    cur.execute(f"UPDATE personagem SET idSala = %s WHERE idPersonagem = %s;",(direcao, personagemId))
    conn.commit()

def get_sala(cur, salaAtual):
    cur.execute(f"SELECT * FROM sala WHERE idSala = %s;",(salaAtual,))
    sala = cur.fetchall()[0]
    return sala
        
def iniciar_game(personagemId, conn, cur):
    clear()

    cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = %s;",(personagemId,))
    personagem_atual = cur.fetchall()[0]

    while True:
        clear()
        cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = %s;",(personagemId,))
        personagem_atual = cur.fetchall()[0]
        sala_info = get_sala(cur, personagem_atual['idsala'])
        print(f"Você está na sala {sala_info['nomesala']}\n\n")
        opcoes = {}
        if sala_info['salanorte']:
            opcoes['norte'] = 'Mover para o norte'
        if sala_info['salasul']:
            opcoes['sul'] = 'Mover para o sul'
        if sala_info['salaleste']:
            opcoes['leste'] = 'Mover para o leste'
        if sala_info['salaoeste']:
            opcoes['oeste'] = 'Mover para o oeste'
        
        
        print("Opções:")
        for k,v in opcoes.items():
            print(f"[{k}] - {v}")
        
        print("[0] - Sair do jogo")
        
        direcao = input("Digite a direção que deseja ir: ")
        if direcao == '0':
            sair()
        
        mover_personagem(conn, cur, personagemId, sala_info[f'sala{direcao}'])

def login(conn, cur):
    clear()
    options = {
        '1': "Login",
        '2': "Cadastrar",
        '0': "Sair"
    }
    print(name)
    print("Seja bem-vindo ao Adventure Quest World!")
    while True:
        chosen_option = input("Escolha uma opção:\n[1] - Login\n[2] - Cadastrar\n[0] - Sair\n")
        if chosen_option not in options:
            clear()
            print(name)
            print("Seja bem-vindo ao Adventure Quest World!")
            print(100* '-')
            print("Opção inválida!")
            print(100* '-')
        
        elif chosen_option == '0':
            sair()
        
        elif chosen_option == '2':
            username = input("Digite o seu username: ")
            password = input("Digite sua senha: ")
            userId = criar_conta(username,password,conn,cur)
            if userId:
                return userId['idusuario']
        else:
            username = input("Digite o seu username: ")
            password = input("Digite sua senha: ")
            userId = validar_login(username,password, cur)
            if userId:
                return userId['idusuario']
            else:
                clear()
                print(name)
                print("Seja bem-vindo ao Adventure Quest World!")
                print(100* '-')
                print("Usuário ou senha incorretos.")
                print(100* '-')

def criar_inventario(conn, cur, personagemId):
    default_schema = {
        'capacidade': 30,
        'espacodisponivel': 30,
        'quantidadeouro': 0
    }
    sql_query = f"""
    INSERT INTO inventario (capacidade, espacodisponivel, quantidadeouro, idpersonagem)
    VALUES (%s, %s, %s, %s);
    """
    cur.execute(sql_query, (default_schema['capacidade'], default_schema['espacodisponivel'], default_schema['quantidadeouro'], personagemId))
    conn.commit()

def criar_personagem(conn, cur, nome, classe):
    valores_base = {
        'staminaBasePersonagem': 100,
        'vidaBasePersonagem': 100,
        'defensePersonagem': 40,
        'ataqueFisico': 50,
        'ataqueMagico': 30
    }
    sql_insert = f"""
    INSERT INTO Personagem (
        nomePersonagem, staminaAtualPersonagem, vidaAtualPersonagem, 
        staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, 
        ataqueMagico, idClasse, idSala
    ) VALUES (
        %s,
        {valores_base['staminaBasePersonagem']},
        {valores_base['vidaBasePersonagem']},
        {valores_base['staminaBasePersonagem']},
        {valores_base['vidaBasePersonagem']},
        {valores_base['defensePersonagem']},
        {floor(valores_base['ataqueFisico'] * classe['mulfisico'])},
        {floor(valores_base['ataqueMagico'] * classe['mulmagico'])},
        %s,
        1
    ) RETURNING idPersonagem;
    """
    cur.execute(sql_insert,(nome,classe['idclasse']))
    idPersonagem = cur.fetchone()['idpersonagem']  
    conn.commit()
    criar_inventario(conn, cur, idPersonagem)

    return idPersonagem

def adicionar_save(conn, cur, userId, personagemId):
    cur.execute(f"INSERT INTO save (idusuario, idpersonagem) VALUES ({userId}, {personagemId});")
    conn.commit()

def selecionar_classe(cur):
    cur.execute("SELECT * FROM classe;")
    classes = cur.fetchall()
    while True:
        print("Escolha uma classe:")
        for i, classe in enumerate(classes):
            print(f"[{i}] - {classe['nomeclasse']}")

        escolha = input("Digite o número da classe que deseja: ")
        escolha = int(escolha) if escolha.isdigit() else -1
        
        if escolha < 0 or escolha >= len(classes):
            clear()
            print(100* '-')
            print("Opção inválida!")
            print(100* '-')
        else:
            return classes[escolha]

def selecionar_save(userId, cur, conn):
    clear()
    cur.execute(f"""
                SELECT s.idpersonagem, p.nomepersonagem FROM save AS s
                JOIN personagem as p ON s.idpersonagem = p.idpersonagem
                WHERE idusuario = %s;""",(userId,))
    saves = cur.fetchall()

    while len(saves) < 3:
        saves.append(None)
    
    while True:
        print("Escolha um save:")
        for i, save in enumerate(saves):
            if not save:
                print(f"[{i}] - === NOVO SAVE ===")
            else:
                print(f"[{i}] - {save['nomepersonagem']}")
        
        escolha = int(input("Digite o número do save que deseja: "))
        if escolha < 0 or escolha >= len(saves):
            clear()
            print("Opção inválida!")
        elif saves[escolha] == None:
            clear()
            nome = input("Digite o nome do personagem: ")
            classe = selecionar_classe(cur)
            personagemId = criar_personagem(conn, cur, nome, classe)
            adicionar_save(conn, cur, userId, personagemId)

            return personagemId
        else:
            return saves[escolha]['idpersonagem']            

def main():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    user = login(conn,cur)
    save = selecionar_save(user, cur, conn)
    iniciar_game(save, conn, cur)
    

if __name__ == "__main__":
    create_tables()
    populate_tables()
    main()