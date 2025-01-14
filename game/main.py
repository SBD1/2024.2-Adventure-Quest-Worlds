import psycopg2
import os
from psycopg2.extras import RealDictCursor
from config.database import get_connection, create_tables, populate_tables
from ascii_arts import name, bye

def clear():
    os.system('clear')

def selecionar_save(userId):
    print(userId)

def criar_conta(username, password):
    return 1

def validar_login(username, password):
    while True:
        if username == 'admin' and password == 'admin':
            return 1
        else:
            return None
def sair():
    print(bye)
    exit()
        
def mover_personagem(conn, cur, personagemId, direcao):
    cur.execute(f"UPDATE personagem SET idSala = {direcao} WHERE idPersonagem = {personagemId};")
    conn.commit()

def get_sala(cur, salaAtual):
    cur.execute(f"SELECT * FROM sala WHERE idSala = {salaAtual};")
    sala = cur.fetchall()[0]
    return sala
        
def iniciar_game(personagemId):
    clear()

    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = {personagemId};")
    personagem_atual = cur.fetchall()[0]

    while True:
        clear()
        cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = {personagemId};")
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

def login():
    os.system('clear')
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
            os.system('clear')
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
            userId = criar_conta(username,password)
            if userId:
                return userId
        else:
            username = input("Digite o seu username: ")
            password = input("Digite sua senha: ")
            userId = validar_login(username,password)
            if userId:
                return userId
            else:
                os.system('clear')
                print(name)
                print("Seja bem-vindo ao Adventure Quest World!")
                print(100* '-')
                print("Usuário ou senha incorretos.")
                print(100* '-')


def main():
    userId = login()
    iniciar_game(1)
    

if __name__ == "__main__":
    main()