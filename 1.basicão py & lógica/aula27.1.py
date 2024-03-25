"""

EXERCÍCIO

Peça ao usuário para digitar seu nome;
Peça ao usuário para digitar sua idade;
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome};
        Seu nome invertido é {nome invertido};
        Seu nome contém (ou não) espaços;
        Seu nome tem {n} letras;
        A primeira letra do seu nome é;
        A ultima letra do seu nome é;
Se nada for digitado em nome ou idade:
    exiba: "desculpe, você deixou os campos vazios."

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
idade_int = int(idade)
primeira_letra = nome[0]
ultima_letra = nome[-1]
qt_letras = len(nome)


if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome inverido é {nome_invertido}')
    print(f'Sua idade é {idade_int}.')
    if ' ' in nome:
        print(f'Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços!')
    print(f'Seu nome tem {qt_letras} letras.')
    print(f'A primeira letra do seu nome é {primeira_letra}.')
    print(f'A ultima letra do seu nome é {ultima_letra}.')
else:
    print('Desculpe, você deixou os campos vazios.')