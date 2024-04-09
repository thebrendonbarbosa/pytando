"""Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party."""

nome_convidado = input('Quem você gostaria de convidar para a festa? ')
print(f'{nome_convidado} foi convidado(a) com sucesso!')
pergunta_convite = input('Deseja convidar mais alguém? [S] ou [N] ')

total_de_convidados_parcial = 1
total_de_convidados = total_de_convidados_parcial

while pergunta_convite == 'S':
    nome_convidado_extra = input('Quem você gostaria de convidar para a festa? ')
    print(f'{nome_convidado_extra} foi convidado com sucesso!')
    total_de_convidados += 1
    pergunta_convite = input('Deseja convidar mais alguém? [S] ou [N] ')

    continue

print(f'O total de convidados para a festa foi de {total_de_convidados} pessoas.')
