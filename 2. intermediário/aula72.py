"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(mensagem, nome):
    return f'{mensagem}, {nome}!'


def executa(funcao, *args): #Função para executar outra função
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)