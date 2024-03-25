"""
Flag (Banderira) - Marca um local
None - Nenhum valor
IS - Verifica se é o mesmo objeto (TIPO, VALO E ID)
IS NOT - Verifica se não é o mesmo objeto
ID - Retorna o identificador do objeto

"""


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça alguma coisa')
else:
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')   
else:
    print('Passou no if')
