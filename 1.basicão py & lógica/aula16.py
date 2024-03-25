#if / elif    / else
#se / se não se/ se não

entrada = input('Você desejar ENTRAR ou SAIR do sistema? ')

if entrada == 'ENTRAR':
    print('Bem vindo! Você entrou no sistema!')
elif entrada == "SAIR":
    print('Você saiu do sistema.')
else:
    print('Resposta incorreta! Responda somente ENTRAR ou SAIR.')
    