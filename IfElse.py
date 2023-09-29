opa = float(input('Digite sua altura: '))
apo = int(input('Digite seu sexo, 0 para Masculino e 1 para Feminino: '))

if apo == 0:
    resultado = (72.7 * opa) - 58
    print('Aqui o %.2f' % resultado)
else:
    resultado = (62.1 * opa) - 44.7
    print('Aqui o %.2f' % resultado)