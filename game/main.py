import psycopg2
import os
from psycopg2.extras import RealDictCursor
from config.database import get_connection, create_tables, populate_tables
from ascii_arts import name, bye
from math import floor

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def colmuns():
    return os.get_terminal_size().columns

def lines():
    return os.get_terminal_size().lines

def invalid():
    print(colmuns() * '-')
    print("Opção inválida!".center(colmuns()))
    print(colmuns() * '-')

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

def get_mobs_sala(cur, salaAtual):
    cur.execute("""
    SELECT * FROM instanciamonstro AS i
    JOIN monstro as min on i.idmonstro = min.idmonstro
    WHERE i.idsala = %s;"""
    ,(salaAtual,))

    mobs = cur.fetchall()

    if not mobs:
        return None

    return mobs
    
def get_lojas(cur, salaAtual):
    cur.execute(f"SELECT * FROM Loja WHERE idsala = %s;",(salaAtual,))
    lojas = cur.fetchall()

    if not lojas:
        return None
    
    return lojas

def status(cur, personagem_atual):
    sala_info = get_sala(cur, personagem_atual['idsala'])
    print(f"Você está na sala {sala_info['nomesala']}\n\n")

def mover(conn, cur, personagem_atual):
    sala_info = get_sala(cur, personagem_atual['idsala'])
    opcoes_mover = {}
    if sala_info['salanorte']:
        opcoes_mover['norte'] = 'Mover para o norte'
    if sala_info['salasul']:
        opcoes_mover['sul'] = 'Mover para o sul'
    if sala_info['salaleste']:
        opcoes_mover['leste'] = 'Mover para o leste'
    if sala_info['salaoeste']:
        opcoes_mover['oeste'] = 'Mover para o oeste'
    opcoes_mover['voltar'] = 'Voltar para o menu principal'

    print("Opções:\n")
    for k,v in opcoes_mover.items():
        if k == 'voltar':
            print(f"\n[{k}] - {v}\n")
        else:
            print(f"[{k}] - {v}")
        
    direcao = input("Digite a direção que deseja ir: ")
    if not direcao in opcoes_mover.keys():
        clear()
        invalid()
        mover(conn, cur, personagem_atual)
    elif direcao == 'voltar':
        clear()
        return
    else:
        print(100*"=")
        print("\n")
        mover_personagem(conn, cur, personagem_atual['idpersonagem'], sala_info[f'sala{direcao}'])
        clear()

def ver_inventario(cur, personagemId):
    cur.execute(f"SELECT * FROM inventario WHERE idpersonagem = %s;",(personagemId,))
    inventario = cur.fetchall()[0]
    print(colmuns()*"=")
    print(f"Capacidade: {inventario['capacidade']}")
    print(f"Espaço disponível: {inventario['espacodisponivel']}")
    print(f"Quantidade de ouro: {inventario['quantidadeouro']}")
    print(colmuns()*"=")
    opcoes = {
        "listar" : "Listar seus itens",
        "fechar" : "Fechar o inventário"
    }

    for k,v in opcoes.items():
        print(f"[{k}] - {v}")
    choice = input("Escolha uma das opções: ")

    if not choice in opcoes:
        clear()
        invalid()
        ver_inventario(cur,personagemId)
    # Tem que implementar a listagem de itens para permitir equipar
    elif choice == "fechar":
        clear()
        return

def ver_itens_loja(cur, idloja, personagemId):
    cur.execute("SELECT * FROM Catalogo JOIN Item ON Catalogo.idItem = Item.idItem JOIN instanciaitem ON instanciaitem.iditem = Item.iditem WHERE idloja = %s;", (idloja,))
    itens = cur.fetchall()

    if not itens:
        print("Nenhum item disponível nesta loja.")
        return

    print("Itens disponíveis na loja:\n")
    for i, item in enumerate(itens):
        print(f"[{i}] - {item['nomeitem']} - Preço: {item['precoitem']} - Quantidade: {item['quantidadeitem']}")

    opcoes = {str(i): item for i, item in enumerate(itens)}
    opcoes['voltar'] = 'Voltar para o menu principal'

    choice = input("Escolha o item que deseja comprar: ")

    if choice not in opcoes:
        clear()
        invalid()
        ver_itens_loja(cur, idloja)

    elif choice == 'voltar':
        clear()
        return
    else:
        item = opcoes[choice]
        clear()
        print(f"Você comprou {item['nomeitem']} por {item['precoitem']} ouro.")

        #diminuindo a quantidade da instanciaitem naquela loja e o ouro porem como faco para adicionar ao invetario essa instancia e ao mesmo tempo apenas diminuir a quantidade da loja
        cur.execute(f"UPDATE instanciaitem SET quantidadeitem = quantidadeitem - 1 WHERE iditem = %s;",(item['iditem'],))
        cur.execute(f"UPDATE inventario SET quantidadeouro = quantidadeouro - %s WHERE idpersonagem = %s;",(item['precoitem'],personagemId))
        return


def ver_lojas(lojas, cur, personagemId):
    opcoes = dict()
    for i, loja in enumerate(lojas):
        opcoes[str(i)] = loja['nomeloja']
    
    opcoes['voltar'] = 'Voltar para o menu principal'
    
    print("Lojas disponíveis: \n")
    
    for k,v in opcoes.items():
        if k == 'voltar':
            print(f"\n[{k}] - {v}\n")
        else:
            print(f"[{k}] - {v}")
    
    choice = input("Escolha a loja que deseja entrar: ")

    if not choice in opcoes:
        clear()
        invalid()
        ver_lojas(lojas)
    elif choice == 'voltar':
        clear()
        return
    else:
        clear()
        ver_itens_loja(cur, lojas[int(choice)]['idsala'], personagemId)
        return

def selecionar_monstro(mobs):
    opcoes = dict()
    for i, mob in enumerate(mobs):
        opcoes[str(i)] = mob['nomemonstro']
    
    opcoes['voltar'] = 'Voltar para o menu principal'

    print("Monstros na sala atual: \n")
    for k,v in opcoes.items():
        if k == 'voltar':
            print(f"\n[{k}] - {v}\n")
        else:
            print(f"[{k}] - {v}")
    
    choice = input("Escolha o monstro que deseja lutar: ")

    if not choice in opcoes:
        clear()
        invalid()
        selecionar_monstro(mobs)
    elif choice == 'voltar':
        clear()
        return
    else:
        clear()
        # chamada a função de luta do bruno 
        print("Implementação da luta")
        return

                
def iniciar_game(personagemId, conn, cur):
    clear()

    while True:
        cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = %s;",(personagemId,))
        personagem_atual = cur.fetchall()[0]

        cur.execute(f"SELECT * FROM personagem WHERE idPersonagem = %s;",(personagemId,))
        status(cur, personagem_atual)

        mobs = get_mobs_sala(cur, personagem_atual['idsala'])
        lojas = get_lojas(cur, personagem_atual['idsala'])

        opcoes = {}
        if mobs:
            opcoes['lutar'] = 'Lutar com um monstro'
        if lojas:
            opcoes['loja'] = 'Ir para uma loja'

        opcoes['inventario'] = 'Ver inventário'
        opcoes['mover'] = 'Mover para outra sala'
        opcoes['sair'] = 'Sair do jogo'

        print("Ações possíveis: \n")
        for k,v in opcoes.items():
            if k == 'sair':
                print(f"\n[{k}] - {v}\n")
            else:
                print(f"[{k}] - {v}")
        
        escolha = input("Digite a ação que deseja realizar: ")
        if not escolha in opcoes.keys():
            clear()
            invalid()
        elif escolha == 'sair':
            clear()
            sair()
        elif escolha == 'mover':
            clear()
            mover(conn, cur, personagem_atual)
        elif escolha == 'inventario':
            clear()
            ver_inventario(cur,personagemId)
        elif escolha == 'lutar':
            clear()
            selecionar_monstro(mobs)
        elif escolha == 'loja':
            clear()
            ver_lojas(lojas, cur, personagemId)

def login(conn, cur):
    clear()
    options = {
        '1': "Login",
        '2': "Cadastrar",
        '0': "Sair"
    }
    print(name.center(colmuns()))
    print("Seja bem-vindo ao Adventure Quest World!")
    while True:
        chosen_option = input("Escolha uma opção:\n[1] - Login\n[2] - Cadastrar\n[0] - Sair\n")
        if chosen_option not in options:
            clear()
            print(name)
            print("Seja bem-vindo ao Adventure Quest World!")
            invalid()
        
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
        idPersonagem, nomePersonagem, staminaAtualPersonagem, vidaAtualPersonagem, 
        staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, 
        ataqueMagico, idClasse, idSala, nivel, xpAtual
    ) VALUES (
        DEFAULT,
        %s,
        {valores_base['staminaBasePersonagem']},
        {valores_base['vidaBasePersonagem']},
        {valores_base['staminaBasePersonagem']},
        {valores_base['vidaBasePersonagem']},
        {valores_base['defensePersonagem']},
        {floor(valores_base['ataqueFisico'] * classe['mulfisico'])},
        {floor(valores_base['ataqueMagico'] * classe['mulmagico'])},
        %s,
        1,
        1,
        0
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
            invalid()
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
        
        escolha = input("Digite o número do save que deseja: ")
        if not escolha.isdigit() or int(escolha) < 0 or int(escolha) >= len(saves):
            clear()
            invalid()
        elif saves[int(escolha)] == None:
            clear()
            nome = input("Digite o nome do personagem: ")
            classe = selecionar_classe(cur)
            personagemId = criar_personagem(conn, cur, nome, classe)
            adicionar_save(conn, cur, userId, personagemId)

            return personagemId
        else:
            return saves[int(escolha)]['idpersonagem']            

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