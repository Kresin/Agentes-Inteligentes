import random

#Matriz com o mapa
from matplotlib import pyplot as plt

mapa = ([[1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1]])

# Gera um mapa 6X6 com quantidade de sujeira aleatório e em localizações aleatórias
def geraMapaAleatorio():
    # Gera uma qunatidade aleatória de sujeiras, podendo gerar no máximo até 16
    numeroSujeiras = random.randint(0, 16)
    posicoes = []
    i = 0
    while i < numeroSujeiras:
        novaPosicaoUnica = False
        while not novaPosicaoUnica:
            posicaoX = random.randint(1, 4)
            posicaoY = random.randint(1, 4)
            if not posicoes:
                posicoes.append([posicaoX, posicaoY])
                novaPosicaoUnica = True
            else:
                posicaoRepetida = False
                for posicao in posicoes:
                    if (posicao[0] == posicaoX) and (posicao[1] == posicaoY):
                        posicaoRepetida = True
                        break
                if not posicaoRepetida:
                    posicoes.append([posicaoX, posicaoY])
                    novaPosicaoUnica = True
        i += 1
    print("Numero de sujeiras geradas:")
    print(numeroSujeiras)
    print("Posicoes geradas (x,y):")
    print(posicoes)
    for posicao in posicoes:
        mapa[posicao[0]][posicao[1]] = 2
    print("mapa gerado:")
    print(mapa)

# Função que exibe o ambiente na tela
def exibir(I):
    geraMapaAleatorio()
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

exibir(mapa)