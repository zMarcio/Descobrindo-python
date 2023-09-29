import random



print('---------------------------------------------------------')
while True:
    print('Por Favor escreva do jeito que está na mensagem abaixo!')
    escolha = input('Escolha entre Pedra, Papel e Tesoura: ')
    escolhas = ['Pedra','Papel','Tesoura']
    escolhasMaquina = random.choice(['Pedra','Papel','Tesoura'])
    if escolha in escolhas:
        print('A sua escolha: ', escolha)
        print('---------------------------------------------------------')
        print('A escolha da máquina: ',escolhasMaquina)
        if escolhasMaquina == escolha:
            print('---------------------------------------------------------')
            print('Empatou')
            print('---------------------------------------------------------')
        elif escolha == 'Tesoura' and escolhasMaquina == 'Papel':
            print('---------------------------------------------------------')
            print('Você ganhou!!!')
            print('---------------------------------------------------------')
        elif escolha == 'Tesoura' and escolhasMaquina == 'Pedra':
            print('---------------------------------------------------------')
            print('Você perdeu!!!')
            print('---------------------------------------------------------')
        elif escolha == 'Pedra' and escolhasMaquina == 'Tesoura':
            print('---------------------------------------------------------')
            print('Você ganhou!!!')
            print('---------------------------------------------------------')
        elif escolha == 'Pedra' and escolhasMaquina == 'Papel':
            print('---------------------------------------------------------')
            print('Você perdeu!!!')
            print('---------------------------------------------------------')
        elif escolha == 'Papel' and escolhasMaquina == 'Pedra':
            print('---------------------------------------------------------')
            print('Você ganhou!!!')
            print('---------------------------------------------------------')
        elif escolha == 'Papel' and escolhasMaquina == 'Tesoura':
            print('---------------------------------------------------------')
            print('Você perdeu!!!')
            print('---------------------------------------------------------')
        break
    else:
        print('---------------------------------------------------------')
        print('Opa você digitou errado aqui o que digitou ', escolha)