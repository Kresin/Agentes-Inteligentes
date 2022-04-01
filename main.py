import numpy as np
import matplotlib.pyplot as plt
import random

# Matriz do mapa
# Legenda:
#   0 = Chão limpo
#   1 = Parede
#   2 = Sujeira
mapa = ([[1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1]])

# Gera um mapa 6X6 com quantidade de sujeira aleatória e com sujeiras em locais aleatórios
# Pode ser gerado no máximo 16 sujeiras, que é equivalente ao espaço transitável do aspirador(4X4)
# Duas sujeiras não podem ocupar a mesma posição
def geraMapaAleatorio():
    # Gera uma quantidade aleatória de sujeiras, podendo gerar no máximo até 16
    numeroSujeiras = random.randint(0, 16)
    posicoes = []
    i = 0
    # Gera uma lista de posições(X,Y) igual a quantidade de sujeiras geradas acima
    while i < numeroSujeiras:
        # Indica se a posição gerada é única
        novaPosicaoUnica = False
        # Enquanto a posição gerada não for única será gerada uma nova posição
        while not novaPosicaoUnica:
            # Gera valores aleatórios para as coordenas X e Y
            posicaoX = random.randint(1, 4)
            posicaoY = random.randint(1, 4)
            # Se a lista de posições estiver vazia, adiciona a posição direto na lista sem validar
            if not posicoes:
                posicoes.append([posicaoX, posicaoY])
                novaPosicaoUnica = True
            # Verifica se as coordenadas geradas são únicas
            else:
                # Variável que indica se a coordenada já existe
                posicaoRepetida = False
                # Para cada posição da lista de posições, é realizada uma comparação da posição a ser adicionada na lista
                # Quando for encontrada uma posição igual a verificação é interrompida
                for posicao in posicoes:
                    if (posicao[0] == posicaoX) and (posicao[1] == posicaoY):
                        # Sinaliza que encontrou uma posição repetida e encerra o loop
                        posicaoRepetida = True
                        break
                # Verifica se a etapa anterior não encontrou uma posição já existente na lista. Caso não tenha encontrado,
                # a posição gerada é adicionada na lista
                if not posicaoRepetida:
                    posicoes.append([posicaoX, posicaoY])
                    novaPosicaoUnica = True
        # Incrementa o valor de posições geradas
        i += 1
    print("Numero de sujeiras geradas:")
    print(numeroSujeiras)
    print("Posicoes geradas (x,y):")
    print(posicoes)
    # Preenche o mapa com as sugeiras geradas nas instruções anteriores
    for posicao in posicoes:
        mapa[posicao[0]][posicao[1]] = 2


# Função que exibe o ambiente na tela
def exibir(I):
    global posAPAx
    global posAPAy

    posAPAx = 1
    posAPAy = 2

    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

    plt.show(block=True)


# Função que aspira a sujeira na posicao do robô
def aspirar():
    mapa[posAPAx, posAPAy] = 0

# Verifica extensão do mapa
def mapearLimites(mapa):
    cols = len(mapa[0])
    rows = len(mapa)
    return cols -1, rows -1

def retornarAoInicio():
    if posAPAx != 1 and posAPAy != 1:
        while posAPAx > 1:
            andar("cima")
        while posAPAy > 1:
            andar("esquerda")
    else:
        print("Já está na posição inicial")

def andar(direcao):
    if direcao == "direita":
        posAPAy += 1

    elif direcao == "baixo":
        posAPAx += 1

    elif direcao == "esquerda":
        posAPAy -= 1

    elif direcao == "baixo":
        posAPAx -= 1

#A variável "percepcao" dentro dos parênteses é a entrada da função,
#isto é a posição em que o agente se encontra e o status da percepção (limpo ou sujo).
def agenteReativoSimples(percepcao):

    retornarAoInicio()

    posFinalX, posFinalY = mapearLimites()


    #Enquanto não estiver na posição final, percorre o mapa
    while posAPAx < posFinalX and posAPAy < posFinalY:
        while posAPAx

    if mapa[percepcao[0], percepcao[1]] == 2: #posicao com sujeira
        return aspirar()



exibir(mapa)
