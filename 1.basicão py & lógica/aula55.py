
"""
Introdução ao desempacotamento
"""

netos = ['Abia','Karol','Kelly']

# restos cria uma outra lista com os valores q n foram selecionados
filho_nilda, *resto = netos
_,filho_marcia,*__= netos
_,_,filho_junior,*_ = netos
print(filho_nilda)
print(filho_marcia)
print(filho_junior)