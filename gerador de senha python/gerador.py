import string
import secrets
import sys
import time

while True:
    for i in range(len('Bem vindo ao gerador de senhas!')):
        print('Bem vindo ao gerador de senhas!'[i], end = '', flush = True)
        time.sleep(0.05)

    for i in range(len('Este programa irá gerar uma senha aleatória para você!')):
        print('\nEste programa irá gerar uma senha aleatória para você!'[i], end = '', flush = True)
        time.sleep(0.05)

    for i in range(len('Agora me informe seu nome: ')):
        print('\nAgora me informe seu nome: '[i], end = '', flush = True)
        time.sleep(0.05)
    nome = str(input()).strip().capitalize()

    while True:
        try:
            for i in range(len('Agora me informe quantos caracteres que você deseja na senha: ')):
                print('Agora me informe quantos caracteres que você deseja na senha: '[i], end = '', flush = True)
                time.sleep(0.03)
            qtd_char = int(input(''))

            if qtd_char > 100:
                raise ValueError('Utilize apenas números inteiros menores ou iguais a 100')

            if qtd_char <= 0:
                raise ValueError('Utilize apenas números inteiros maiores que 0')
            break

        except ValueError as erro:
            print(f'Erro: {erro}')

        

    for i in range(len(f'Muito prazer {nome}! iremos começar com {qtd_char} caracteres')):
        print(f'\nMuito prazer {nome}! iremos começar com {qtd_char} caracteres'[i], end = '', flush = True)
        time.sleep(0.03)

    caracteres = ''
    senha = ''

    while True:
        try:

            while True:
                try:
                    usar_maiusculas = str(input('\nDeseja utilizar letras maiúsculas? [s/n] ')).strip().lower()
                    if usar_maiusculas not in 'sn':
                        raise ValueError('Apenas utilize s ou n')
                    break
                except ValueError as erro:
                    print(f'Erro: {erro}')
            while True:
                try:
                    usar_minusculas = str(input('Deseja utilizar letras minusculas? [s/n] ')).strip().lower()
                    if usar_minusculas not in 'sn':
                        raise ValueError('Apenas utilize s ou n')
                    break
                except ValueError as erro:
                    print(f'Erro: {erro}')

            while True:
                try: 
                    usar_numeros = str(input('Deseja utilizar números? [s/n] ')).strip().lower()
                    if usar_numeros not in 'sn':
                        raise ValueError('Apenas utilize s ou n')
                    break
                except ValueError as erro:
                    print(f'Erro: {erro}')

            if usar_maiusculas == 's':
                usar_maiusculas = True
            else:
                usar_maiusculas = False

            if usar_minusculas == 's':
                usar_minusculas = True      
            else:
                usar_minusculas = False

            if usar_numeros == 's':
                usar_numeros = True 
            else:
                usar_numeros = False

            if not usar_maiusculas and not usar_minusculas and not usar_numeros:
                raise ValueError('Você deve escolher ao menos um tipo de caractere para utilizar')
            break

        except ValueError as erro:
            print(f'Erro: {erro}')


    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits


    for i in range(qtd_char):
        senha += secrets.choice(caracteres)

    print('\033[34mGerando senha\033[0m', end = '')

    for i in range(3):
        print('.', end = '', flush = True)
        time.sleep(0.8)

    print(f'\n{nome}, sua senha é: \n')
    print(f'\033[32m{senha}\033[0m\n')

    while True:
        try:
            reiniciar = str(input('Deseja reiniciar? [s/n]')).strip().lower()
            if reiniciar == 's':
                break
            elif reiniciar == 'n':
                print('Encerrando', end = '', flush = True)
                for i in range(3):
                    print('.', end = '', flush = True)
                    time.sleep(0.8)
                print('\nPrograma encerrado')
                sys.exit()
            else:
                raise ValueError('Utilize apenas s ou n')
        except ValueError as erro:
            print(f'Erro: {erro}')
