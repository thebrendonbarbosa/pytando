"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 2

def escopo():
    global x #altera o valor de x para fora do alcance de escopo
    x = 11

    def outra_funcao():
        global x
        x = 13
        y = 1
        print(f"x e y [outra_funcao]: {x,y}")
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)