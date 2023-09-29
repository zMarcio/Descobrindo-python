import random


palavras = ["python"]

palavra = random.choice(palavras)
opa = input('escreva')
palavra_revelada = ['_' for _ in palavra] 
nova = list(palavra)

if opa in nova:
    for i,letra in enumerate(nova):
        if letra == opa:
            teste = palavra_revelada[i] = opa
            print(i, letra)



print(''.join(palavra_revelada))