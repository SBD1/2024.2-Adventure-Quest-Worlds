import psycopg2
import os
from config.database import get_connection, create_tables
from ascii_arts import name, bye

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
            print(bye)
            exit()
        
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
    print(f"Id de usuário {userId}")

if __name__ == "__main__":
    main()