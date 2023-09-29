# n = int(input('Digite um número: '))
# soma = 0
# teste = n + 1
# arrau = []

# if n == 1:
#     print(n)
# elif n == 2:
#     for p in range(teste, n ** 3, 2):
#         soma += p
#         if soma == n ** 3:
#             print('É perfeito')
#             break
# else:
#     teste1 = n + 4
#     for p in range(teste1, n ** 3, 2):
#         soma += p
#         arrau.append(soma)
#         if soma == n ** 3:
#             print(arrau)
#             print('É perfeito')
#             break
import random
opa = random.randint(1,100)
i = 0
while True:
    n = int(input('Digite um número: '))
    i = i + 1
    if n == opa :
        print('Acertou! Aqui o numero:', opa)
        print('Suas tentativa: ', i)
        break
    elif n > opa:
        print('Chute mais baixo')
    elif n < opa:
        print('Chute mais alto')