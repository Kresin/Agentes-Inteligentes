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

# Coordenadas x e y do agente
posicaoAgenteEixoX = 1
posicaoAgenteEixoY = 1

# Lista com as direções que o aspirador deve seguir para percorrer o mapa.
# Direções: 1 = direita; 2 = esquerda; 3 = acima; 4 = abaixo
caminho = (1, 1, 1, 4, 2, 2, 2, 4, 1, 1, 1, 4, 2, 2, 2, 3)

# Indica quantos passos o agente já deu. Usado para controlar quando o aspirador deve voltar ao início.
passos = 0

# Indica quantos pontos o agente obteve ao longo da execução. Quanto menor a quantidade melhor.
pontos = 0

# Gera um mapa 6X6 com quantidade de sujeira aleatória e com sujeiras em locais aleatórios
# Pode ser gerado no máximo 16 sujeiras, que é equivalente ao espaço transitável do aspirador(4X4)
# Duas sujeiras não podem ocupar a mesma posição
def gerarMapaAleatorio():
    # Gera uma quantidade aleatória de sujeiras, podendo gerar no máximo até 16 e no mínimo 1
    numeroSujeiras = random.randint(1, 16)
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
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY

    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posicaoAgenteEixoX], [posicaoAgenteEixoY], marker='o', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()

# Função que aspira a sujeira na posição do robô
def aspirar():
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    global pontos
    pontos += 1
    mapa[posicaoAgenteEixoY][posicaoAgenteEixoX] = 0

# Move o agente para a direita no mapa
def andarParaDireita():
    global pontos
    pontos += 1
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    posicaoAgenteEixoX += 1
    plt.plot([posicaoAgenteEixoX], [posicaoAgenteEixoY], marker='o', color='r', ls='')

# Move o agente para a esquerda no mapa
def andarParaEsquerda():
    global pontos
    pontos += 1
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    posicaoAgenteEixoX -= 1
    plt.plot([posicaoAgenteEixoX], [posicaoAgenteEixoY], marker='o', color='r', ls='')

# Move o agente para cima no mapa
def andarParaCima():
    global pontos
    pontos += 1
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    posicaoAgenteEixoY -= 1
    plt.plot([posicaoAgenteEixoX], [posicaoAgenteEixoY], marker='o', color='r', ls='')

# Move o agente para baixo no mapa
def andarParaBaixo():
    global pontos
    pontos += 1
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    posicaoAgenteEixoY += 1
    plt.plot([posicaoAgenteEixoX], [posicaoAgenteEixoY], marker='o', color='r', ls='')

# A variável "percepcao" dentro dos parênteses é a entrada da função,
# isto é a posição em que o agente se encontra e o status da percepção (limpo ou sujo).
def agenteObjetivo(percepcao, objObtido):
    global passos
    if percepcao[0] == "SUJO":
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: aspirar")
        return aspirar()
    if percepcao[1] == 1:
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: direita")
        passos += 1
        return andarParaDireita()
    if percepcao[1] == 2:
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: esquerda")
        passos += 1
        return andarParaEsquerda()
    if percepcao[1] == 3:
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: acima")
        passos += 1
        return andarParaCima()
    if percepcao[1] == 4:
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: abaixo")
        passos += 1
        return andarParaBaixo()
    if objObtido == 0:
        print("Estado da percepção: " + percepcao[0] + " Ação escolhida: Não operar")

# Verifica o valor da coordenada atual na matriz. Caso o valor seja diferente de zero, significa que a posição está suja
def obterPercepcao():
    global posicaoAgenteEixoX
    global posicaoAgenteEixoY
    if mapa[posicaoAgenteEixoY][posicaoAgenteEixoX] == 0:
        return "LIMPO"
    else:
        return "SUJO"

# Verifica se existe alguma sujeira na sala, caso tenha é retornado 1
def checkObj(sala):
    for row in sala:
        for element in row:
            if element == 2:
                return 1
    return 0

# Métoto principal do programa. Responsável por exibir o mapa e chmara os métodos que movem o agente
def main():
    global passos
    gerarMapaAleatorio()
    exibir(mapa)
    print("Mapa gerado:")
    for i in mapa:
        print('\t'.join(map(str, i)))
    while True:
        exibir(mapa)
        percepcao = (obterPercepcao(), caminho[passos])
        agenteObjetivo(percepcao, checkObj(mapa))
        if checkObj(mapa) == 0:
            print("Ponto: " + str(pontos))
            return

# Executar o arquivo na linha abaixo
main()

# Responda: É possível ter todo o espaço limpo efetivamente? Justifique sua resposta.
# Resposta: Sim. O algoritmo acima consegue limpar todo o ambiente de maneira efetiva, porém ele possui a mesma limitação
# do algoritmo anterior, ou seja, funciona apenas em um mundo 4x4. Outro defeito do algoritmo é que ele possui um caminho
# fixo para ser realizado, então se a sala tiver apenas uma sujeira na última posição da sala o agente terá uma pontuação
# muito mais alta do que se ele possuir um algoritmo de busca para ir diretamente até o local sujo.