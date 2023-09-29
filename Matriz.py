import random

def criarMatriz():
    matriz = [[0] * 4 for _ in range(4)]
    return matriz

def embaralhar(matriz):
    guardaNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    random.shuffle(guardaNum)
    indice = 0
    for i in range(0, 4):
        for j in range(0, 4):
            matriz[i][j] = guardaNum[indice]
            indice += 1
            if indice >= len(guardaNum):
                break

def exibirMatriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def encontrarPosicaoVazia(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                return i, j

def moverPeca(matriz, direcao):
    i, j = encontrarPosicaoVazia(matriz)
    if direcao == 'cima' and i > 0:
        matriz[i][j], matriz[i - 1][j] = matriz[i - 1][j], matriz[i][j]
    elif direcao == "baixo" and i < 3:
        matriz[i][j], matriz[i + 1][j] = matriz[i + 1][j], matriz[i][j]
    elif direcao == 'esquerda' and j > 0:
        matriz[i][j], matriz[i][j - 1] = matriz[i][j - 1], matriz[i][j]
    elif direcao == 'direita' and j < 3:
        matriz[i][j], matriz[i][j + 1] = matriz[i][j + 1], matriz[i][j]

def verificarVencedor(matriz):
    numerosCorretos = list(range(1, 16))
    numerosMatriz = [numero for linha in matriz for numero in linha]
    return numerosMatriz == numerosCorretos

def jogar():
    matriz = criarMatriz()
    embaralhar(matriz)
    while True:
        exibirMatriz(matriz)
        movimento = input("Digite o movimento (cima, baixo, esquerda, direita), ou 0 para cancelar a partida: ").lower()
        if movimento in ["cima", "baixo", "esquerda", "direita"]:
            moverPeca(matriz, movimento)
            if verificarVencedor(matriz):
                print('Parabéns você venceu')
                break
            else:
                print('Movimento inválido')
        if movimento == '0':
            print(f'Obrigado por tentar')
            break

if __name__ == "__main__":
    jogar()
