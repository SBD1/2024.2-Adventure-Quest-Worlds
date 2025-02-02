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
    cur.execute(
        f"SELECT * FROM usuario WHERE login = %s AND senha = %s", (username, password))
    existe_usuario = cur.fetchall()
    if existe_usuario:
        return None
    cur.execute(
        f"INSERT INTO usuario (login, senha) VALUES (%s, %s) RETURNING idusuario;", (username, password))
    userId = cur.fetchone()
    conn.commit()
    return userId


def validar_login(username, password, cur):
    cur.execute(
        f"SELECT * FROM usuario WHERE login = %s AND senha = %s", (username, password))
    user = cur.fetchall()
    if user:
        return user[0]
    return None


def sair():
    print(bye)
    exit()


def mover_personagem(conn, cur, personagemId, direcao):
    cur.execute(f"UPDATE personagem SET idSala = %s WHERE idPersonagem = %s;",
                (direcao, personagemId))
    conn.commit()


def get_sala(cur, salaAtual):
    cur.execute(f"SELECT * FROM sala WHERE idSala = %s;", (salaAtual,))
    sala = cur.fetchall()[0]
    return sala


def check_batalha(cur, conn, idPersonagem):
    cur.execute(
        """
        SELECT
            --retorna o que não é nulo
            COALESCE(minion.nomeMonstro, boss.nomeMonstro) AS nomeMonstro,
            i.idinstanciamonstro
        FROM Personagem p
        JOIN instanciaMonstro i
            ON p.idSala = i.idSala
        LEFT JOIN Minion minion
            ON i.idMonstro = minion.idMonstro
        LEFT JOIN Boss boss
            ON i.idMonstro = boss.idMonstro
        WHERE p.idPersonagem = %s;
        """,
        (idPersonagem,),
    )
    local = cur.fetchone()

    if not local:
        return None

    return local


def iniciar_game(personagemId, conn, cur):
    clear()

    cur.execute(
        f"SELECT * FROM personagem WHERE idPersonagem = %s;", (personagemId,))
    personagem_atual = cur.fetchall()[0]

    while True:
        clear()
        cur.execute(
            f"SELECT * FROM personagem WHERE idPersonagem = %s;", (personagemId,))
        personagem_atual = cur.fetchall()[0]
        sala_info = get_sala(cur, personagem_atual['idsala'])
        batalha_info = check_batalha(cur, conn, idPersonagem=personagemId)
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
        if batalha_info:
            opcoes['lutar'] = 'Inicar batalha com {}'.format(
                batalha_info['nomemonstro'])

        print("Opções:")
        for k, v in opcoes.items():
            print(f"[{k}] - {v}")

        print("[0] - Sair do jogo")

        direcao = input("Digite a direção que deseja ir: ")
        if direcao == '0':
            sair()
        elif direcao == 'lutar':
            clear()
            start_batalha(cur, conn, personagemId,
                          batalha_info['idinstanciamonstro'])
            return None

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
        chosen_option = input(
            "Escolha uma opção:\n[1] - Login\n[2] - Cadastrar\n[0] - Sair\n")
        if chosen_option not in options:
            clear()
            print(name)
            print("Seja bem-vindo ao Adventure Quest World!")
            print(100 * '-')
            print("Opção inválida!")
            print(100 * '-')

        elif chosen_option == '0':
            sair()

        elif chosen_option == '2':
            username = input("Digite o seu username: ")
            password = input("Digite sua senha: ")
            userId = criar_conta(username, password, conn, cur)
            if userId:
                return userId['idusuario']
        else:
            username = input("Digite o seu username: ")
            password = input("Digite sua senha: ")
            userId = validar_login(username, password, cur)
            if userId:
                return userId['idusuario']
            else:
                clear()
                print(name)
                print("Seja bem-vindo ao Adventure Quest World!")
                print(100 * '-')
                print("Usuário ou senha incorretos.")
                print(100 * '-')


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
    cur.execute(sql_query, (default_schema['capacidade'],
                default_schema['espacodisponivel'], default_schema['quantidadeouro'], personagemId))
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
    cur.execute(sql_insert, (nome, classe['idclasse']))
    idPersonagem = cur.fetchone()['idpersonagem']
    conn.commit()
    criar_inventario(conn, cur, idPersonagem)

    return idPersonagem


def adicionar_save(conn, cur, userId, personagemId):
    cur.execute(
        f"INSERT INTO save (idusuario, idpersonagem) VALUES ({userId}, {personagemId});")
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
            print(100 * '-')
            print("Opção inválida!")
            print(100 * '-')
        else:
            return classes[escolha]


def selecionar_save(userId, cur, conn):
    clear()
    cur.execute("""
                SELECT s.idpersonagem, p.nomepersonagem FROM save AS s
                JOIN personagem as p ON s.idpersonagem = p.idpersonagem
                WHERE idusuario = %s;
                """,
                (userId,))
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


def get_status_personagem(cur, idPersonagem):
    cur.execute(
        """
        SELECT staminaAtualPersonagem, vidaAtualPersonagem, defensePersonagem, ataqueFisico, ataqueMagico, idClasse, vidabasepersonagem, staminabasepersonagem
        FROM Personagem
        WHERE idPersonagem = %s
        """,
        (idPersonagem,),
    )

    jogador_stats = cur.fetchone()

    if not jogador_stats:
        print("Jogador não encontrado")
        return None

    return jogador_stats


def get_status_instancia(cur, idMonstro):
    cur.execute(
        """
        SELECT
            i.vidaAtual AS vidaAtualInstancia,
            COALESCE(minion.vidaMonstro, boss.vidaMonstro)  AS vidaMonstro,
            COALESCE(minion.danoMonstro, boss.danoMonstro)  AS danoMonstro,
            COALESCE(minion.defMonstro,  boss.defMonstro)   AS defMonstro,
            boss.mulBoss
        FROM instanciaMonstro i
        LEFT JOIN Minion minion
            ON i.idMonstro = minion.idMonstro
        LEFT JOIN Boss boss
            ON i.idMonstro = boss.idMonstro
        WHERE i.idMonstro = %s;
        """,
        (idMonstro,),
    )

    instancia_monstro = cur.fetchone()

    if not instancia_monstro:
        print("Jogador não encontrado")
        return None

    return instancia_monstro


def get_multiplicador_classe(cur, idPersonagem):
    cur.execute(
        """
        SELECT c.mulFisico, c.mulMagico
        FROM Classe c
        JOIN Personagem p ON c.idClasse = p.idClasse  
        WHERE idPersonagem = %s
        """,
        (idPersonagem,),
    )

    jogador_class_stats = cur.fetchone()

    if not jogador_class_stats:
        print("Jogador não encontrado")
        return None

    return jogador_class_stats


# Ainda não foi implementado
def get_multiplicador_item(cur, idPersonagem):
    pass


def get_personagem_forca(cur, idPersonagem):

    # Colentando informações do banco
    jogador_stats = get_status_personagem(cur, idPersonagem)

    ataqueFisico = jogador_stats['ataquefisico']
    ataqueMagico = jogador_stats['ataquemagico']

    jogador_mul = get_multiplicador_classe(cur, idPersonagem)

    mulFisico = jogador_mul['mulfisico']
    mulMagico = jogador_mul['mulmagico']

    ataque_fisico_total = ataqueFisico * mulFisico
    ataque_magico_total = ataqueMagico * mulMagico

    return floor(ataque_fisico_total), floor(ataque_magico_total)


def get_habilidades(cur, idClasse):
    cur.execute(
        """
        SELECT nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown 
        FROM Habilidade
        WHERE idClasse = %s
        """,
        (idClasse,),
    )

    jogador_habilidades = cur.fetchall()

    if not jogador_habilidades:
        print("Jogador não encontrado")
        return None

    return jogador_habilidades


def update_personagem_vida_stamina(conn, cur, idPersonagem, newVida, newStamina):
    cur.execute(
        """
        UPDATE Personagem
        SET vidaAtualPersonagem = %s,
            staminaAtualPersonagem = %s
        WHERE idPersonagem = %s;
        """,
        (newVida, newStamina, idPersonagem,),
    )
    conn.commit()


def update_monstro_void(conn, cur, idInstanciaMonstro):
    cur.execute(
        """
        UPDATE instanciaMonstro
        SET idSala = 0
        WHERE idInstanciaMonstro = %s;
        """, 
        (idInstanciaMonstro,),
    )
    conn.commit()


def update_monstro_status(conn, cur, idInstanciaMonstro):
    cur.execute(
        """
        UPDATE instanciaMonstro AS i
        SET vidaAtual = COALESCE(minion.vidaMonstro, boss.vidaMonstro)
        FROM Monstro m
        LEFT JOIN Minion minion ON m.idMonstro = minion.idMonstro
        LEFT JOIN Boss boss     ON m.idMonstro = boss.idMonstro
        WHERE i.idMonstro = m.idMonstro AND i.idInstanciaMonstro = %s;
        """,
        (idInstanciaMonstro,),
    )
    conn.commit()



def update_vida_stamina(conn, cur, idPersonagem):
    cur.execute(
        """
        UPDATE Personagem
        SET idSala = 1,
            vidaAtualPersonagem = vidaBasePersonagem,
            staminaAtualPersonagem = staminaBasePersonagem
        WHERE idPersonagem = %s;
        """,
        (idPersonagem,),
    )
    conn.commit()


def update_instancia_monstro_hp(conn, cur, idInstanciaMonstro, newVida):
    cur.execute(
        """
        UPDATE instanciaMonstro
        SET vidaAtual = %s
        WHERE idInstanciaMonstro = %s;
        """,
        (newVida, idInstanciaMonstro,),
    )
    conn.commit()



def start_batalha(cur, conn, idPersonagem, idInstancia):

    # coletando informações
    ataque_fisico_total, ataque_magico_total = get_personagem_forca(
        cur, idPersonagem)
    personagem = get_status_personagem(cur, idPersonagem)

    personagem_vida_atual = personagem['vidaatualpersonagem']
    personagem_stamina = personagem['staminaatualpersonagem']
    personagem_defesa = personagem['defensepersonagem']
    personagem_classe = personagem['idclasse']
    personagem_vida_base = personagem['vidabasepersonagem']
    personagem_stamina_base = personagem['staminabasepersonagem']

    habilidades = get_habilidades(cur, personagem_classe)

    # adicionando a opção de passar
    opcoes = {
        0: {
            "nomeHabilidade": "Pass",
            "danoFisico": 0,
            "danoMagico": 0,
            "custoStamina": 0,
            "custoCooldown": 0
        }
    }

    # adicionando habilidades ao dicionário de opções
    for i, hab in enumerate(habilidades, start=1):
        opcoes[f'{i}'] = {
            "nomeHabilidade": hab["nomehabilidade"],
            "danoFisico": hab["danofisico"],
            "danoMagico": hab["danomagico"],
            "custoStamina": hab["custostamina"],
            "custoCooldown": hab["custocooldown"],
        }

    monstro = get_status_instancia(cur, idInstancia)

    monstro_vida_atual = monstro['vidaatualinstancia']
    monstro_dano = monstro['danomonstro']
    monstro_defesa = monstro['defmonstro']

    recuperacao_stamina_round = 20
    round_num = 0
    log = {}
    while personagem_vida_atual > 0 and monstro_vida_atual > 0:
        print(f"Round atual: {round_num}")
        print("-" * 100)
        print(f"Vida do jogador: {personagem_vida_atual}")
        print(f"Stamina Atual:  {personagem_stamina}")
        print("-" * 100)
        print(f"Vida do monstro:  {monstro_vida_atual}")
        print("-" * 100)
        print(log)
        print("-" * 100)

        round_log = {
            "Dano Recebido": 0,
            "Dano Causado": 0,
            "Stamina Recuperada": 0,
        }

        print("Opções de ataque:")
        for key, habilidade_data in opcoes.items():
            print(
                f"[{key}] {habilidade_data['nomeHabilidade']} "
                f"(Físico: {habilidade_data['danoFisico']}, "
                f"Magico: {habilidade_data['danoMagico']}, "
                f"CustoStamina: {habilidade_data['custoStamina']}, "
                f"Cooldown: {habilidade_data['custoCooldown']})"
            )

        escolha = input("Escolha a habilidade (0 para passar a vez): ").strip()

        if escolha == '0':
            clear()
            round_log['Dano Causado'] = 0
        elif escolha not in opcoes:
            clear()
            print("=========Opção inválida!=========")
            continue
        else:
            clear()
            habilidade_escolhida = opcoes[escolha]
            if personagem_stamina < habilidade_escolhida['custoStamina']:
                print("Stamina insuficiente")
                input("Enter para continuar...")
                round_log['Dano Causado'] = 0
                continue
            else:
                quantidade_dano = (
                    ataque_fisico_total + habilidade_escolhida['danoFisico']) - monstro_defesa
                monstro_vida_atual -= quantidade_dano
                personagem_stamina -= habilidade_escolhida['custoStamina']
                round_log['Dano Causado'] = quantidade_dano

        # Dano recebido após rodada
        personagem_vida_atual -= monstro_dano - personagem_defesa
        round_log['Dano Recebido'] = monstro_dano - personagem_defesa

        # verifica stamina
        if personagem_stamina + recuperacao_stamina_round > personagem_stamina_base:
            recuperacao_stamina_round = personagem_stamina_base - personagem_stamina
            round_log['Stamina Recuperada'] = recuperacao_stamina_round
        else:
            personagem_stamina += recuperacao_stamina_round
            round_log['Stamina Recuperada'] = recuperacao_stamina_round
        log[round_num] = round_log

        round_num += 1

    if monstro_vida_atual <= 0:
        print("Você venceu!")
        update_personagem_vida_stamina(conn, cur, idPersonagem, personagem_vida_atual, personagem_stamina)
        update_monstro_void(conn, cur, idInstancia)
        update_monstro_status(conn, cur, idInstancia)
        iniciar_game(idPersonagem, conn, cur)
    elif personagem_vida_atual <= 0:
        print("Você perdeu!")
        update_vida_stamina(conn, cur, idPersonagem)
        update_instancia_monstro_hp(conn, cur, idInstancia, monstro_vida_atual)
        iniciar_game(idPersonagem, conn, cur)
    else:
        print("Batalha encerrada sem resultado claro.")


def main():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    user = login(conn, cur)
    save = selecionar_save(user, cur, conn)
    iniciar_game(save, conn, cur)


if __name__ == "__main__":
    create_tables()
    populate_tables()
    main()
