import random

print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")

escolhaUsu = int(input("Escolha um numero de 1 a 3: "))
teste = [2,1,3]
random.shuffle(teste)
goat,nada,carro = teste

print(f'Você escolheu a porta {escolhaUsu}, mas eu lhe informo que na porta {goat} há uma bode.')

opcao = int(input('Deseja trocar de porta(1 - Sim e 0 - Não): '))

if opcao == 1:
    portaDisponiveis = [1,2,3]
    portaDisponiveis.remove(escolhaUsu)    
    portaDisponiveis.remove(goat)
    escolhaUsu = portaDisponiveis[0]
    if escolhaUsu == carro:
        print('Você ganhou o CARRO!')
    if escolhaUsu == nada:
        print('Você não ganhou NADA!')
    if escolhaUsu == goat:
        print('Você ganhou o GOAT!')
elif opcao == 0:
    if escolhaUsu == carro:
        print('Você ganhou o CARRO!')
    if escolhaUsu == nada:
        print('Você não ganhou NADA!')
    if escolhaUsu == goat:
        print('Você ganhou o GOAT!')




for i in range(1,5):
    print(i)

# print(17000*100)