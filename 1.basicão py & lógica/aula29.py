"""
Constantes = 'variáveis' que não vão mudar 
Muitas condições no mesmo if (ruim)
    <-- Contagem de complexidade (ruim) -afastado da margem (blocos dentro de blocos)

"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 # posição do carro na estrada [km]


# Letra Maiuscula significa que o valor não muda durante a execução do programa
RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # posição do radar1 na estrada [km]
RADAR_RANGE = 1  # (raio de visao )a distancia onde o radar pega

range_radar1_frente = LOCAL_1 + RADAR_RANGE
range_radar1_tras = LOCAL_1 - RADAR_RANGE

velocidade_carro_passou_no_radar_1 = velocidade > RADAR_1

carro_passou_no_radar_1 = local_carro>= range_radar1_tras and \
    local_carro <= range_radar1_frente

carro_multado_radar_1 = carro_passou_no_radar_1 and velocidade_carro_passou_no_radar_1

if velocidade_carro_passou_no_radar_1:
    print('Velocidade que o carro passou no radar') 

if carro_passou_no_radar_1:
    print('O carro passou no radar 1')

if carro_multado_radar_1:
    print('O carro foi multado no radar 1')