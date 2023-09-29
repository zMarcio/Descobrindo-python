p = []
foda = []
foda2 = []
while True:
    n = int(input('Digite o numeros: '))
    p.append(n)
    print(p)
    if n == -1:
        p.remove(-1)
        tamanhoArray = len(p)
        teste = sum(p)
        pri = teste / tamanhoArray
        for papo in p:
            if papo > pri:
                foda.append(papo)
            if 7 > papo:
                foda2.append(papo)
        print('Tamanho 1- ',len(p),';', ' Ordem 2- ',p,';',' Ordem inversa 3- ',p[::-1],';',' Soma do array 4- ',teste,';',' Media 5- ',pri,';', ' Acima da media 6- ', foda,';', ' Abaixo do sete 7- ', foda2,';')
        break