a = ((((((12*3) + 4) //10)*5)- 2))

print(a)

x = int(input('Digita um numero (x):'))
y = int(input('Digita um numero (y):'))

print('Sua equação: ', x + y)
print('Sua equação: ', x - y)
print('Sua equação: ', x * y)
print('Sua equação: ', x / y)
print('Sua equação: ', x // y)
print('Sua equação: ', x % y)


# 1L para ser 6M
print('Lembre-se que um falão de 18L é R$80 e um de 4L é R$25')
tintas = int(input('Digite os Metros que você precisa, lembre-se que 1L é igual a 6M: '))
# 1l = 6m
# 18L = R$80.00 e 4L = R$ 25.00
if tintas < 108:
    divisaoTintas = tintas / 24
    print('Aqui quantos litros você precisa: ' ,divisaoTintas,'aqui quanto irá ficar', divisaoTintas*25)
elif tintas >= 108:
    divisaoTintas = tintas / 108
    print('Aqui quantos litros você precisa: ',divisaoTintas,'aqui quanto irá ficar',divisaoTintas*80)

