alfabeto = {
    'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j',
    'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q',
    'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x',
    'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c', ' ': ' ', ',': ','
}
arrayCriptografada = []
arrayDescriptografada = []
while True:
    escolha = int(input('Digite 1 se você quer criptografar sua Frase e 2 para descriptografar: '))
    
    if escolha == 1:
        frase = str(input('Digite sua frase: '))
        for char in frase.lower():
            if char in alfabeto:
                arrayCriptografada.append(alfabeto[char])
        cripto = ''.join(arrayCriptografada)
        print(f"Aqui sua mensagem criptografada: {cripto}")
        outraEscolha = (str(input('Deseja terminar aqui? (Sim/Não)')))
        if outraEscolha.lower() == 'sim':
            break
    elif escolha == 2:
        cripto  = str(input('Digite sua frase: '))
        for char in cripto.lower():
            if char in alfabeto.values():
                arrayDescriptografada.append(next(key for key, value in alfabeto.items() if value == char))
        descripto  = ''.join(arrayDescriptografada)
        print(f'Aqui sua frase descriptografada: {descripto}')
        break
    else:
        print('Escolha errada, lembre-se é entre 1 e 2')