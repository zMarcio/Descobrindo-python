import random

desenho_forca = [
    """
    +---+
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
    |   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   /    |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
    """
]

palavras = [
    "Real Madrid",
    "Barcelona",
    "Manchester United",
    "Bayern de Munique",
    "Liverpool",
    "Juventus",
    "Paris Saint-Germain",
    "Chelsea",
    "AC Milan",
    "Borussia Dortmund",
    "Inter de Milão",
    "Manchester City",
    "Fortaleza",
    "São Paulo FC",
    "Palmeiras",
    "Corinthians",
    "Boca Juniors",
    "River Plate",
    "Ajax",
    "Atlético de Madrid"
]

def iniciarJogo():
    palavra = escolhasPalavras()
    palavra_revelada = ['_' if letra != ' ' else ' ' for letra in palavra]
    seguraletras = list(palavra)
    letrasErradas = []
    i = 0
    print('Lembre-se você necessita colocar letra maiscula, por exp: CR Belouizdad, você terá que colocar C, R e o B em letra maiscula se não irá indetificar como erro')
    while True:
        letraPalavra = input('Digite sua letra ou palavra: ')
        if verificaInput(letraPalavra):
            if letraPalavra in seguraletras:
                for indice, letra in enumerate(palavra):
                    if letra == letraPalavra:
                        palavra_revelada[indice] = letraPalavra
                        print(desenho_forca[i])
                        print(''.join(palavra_revelada))
                        if ''.join(palavra_revelada) == palavra:
                            print(desenho_forca[i])
                            print(palavra)
                            print('VocÊ ganhou')
                            break

            if len(letraPalavra) > 1 and letraPalavra == palavra:
                print(desenho_forca[i])
                print(palavra)
                print('VocÊ ganhou')
                break

            if len(letraPalavra) > 1 and letraPalavra != palavra:
                print(desenho_forca[i])
                print(f"Aqui a palavra: {palavra}")
                print('Você errou')
                break

            elif len(letraPalavra) == 1 and letraPalavra not in seguraletras:
                i += 1
                print(desenho_forca[i])
                letrasErradas.append(letraPalavra)
                print(f'Você errou, aqui sua letra {letraPalavra}')
                print(''.join(palavra_revelada))
                if i >= 6:
                    print(f'Você perdeu')
                    print(f'aqui a palavra: {palavra}')
                    break

def escolhasPalavras():
    palavraAleatoria = random.choice(palavras)
    return palavraAleatoria

def verificaInput(i):
    alfabeto = {
        'a': ['a', 'á'],
        'b': ['b'],
        'c': ['c', 'ç'],
        'd': ['d'],
        'e': ['e', 'é'],
        'f': ['f'],
        'g': ['g'],
        'h': ['h'],
        'i': ['i', 'í'],
        'j': ['j'],
        'k': ['k'],
        'l': ['l'],
        'm': ['m'],
        'n': ['n'],
        'o': ['o', 'ó'],
        'p': ['p'],
        'q': ['q'],
        'r': ['r'],
        's': ['s'],
        't': ['t'],
        'u': ['u', 'ú'],
        'v': ['v'],
        'w': ['w'],
        'x': ['x'],
        'y': ['y'],
        'z': ['z']
    }

    letra = i.lower()  

    if letra in alfabeto:
        return letra  # Retorne a letra minúscula
    else:
        return f'Digitou algo errado, aqui o que você digitou: {i}'

iniciarJogo()
