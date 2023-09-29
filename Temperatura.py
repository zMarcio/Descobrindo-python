

while True:
    print('Escolha de 1 a 3')
    escolha = input('Escolha a temperatura que quer converter, 1 para C, 2 para F e 3 para K: ')
    print('-------------------------------------------------------------')
    if escolha not in ('1','2','3'):
        print('Escolha invalida. Tente Novamente.')
        print('-------------------------------------------------------------')
        continue
    temperatura = float(input('Digite a temperatura agora: '))
    
    

    if escolha == '1':
        print('-------------------------------------------------------------')
        escolhaP = input('Escolha foi celsius, para qual temperatura você vai querer converter 2 para F e 3 para K: ')
        print('-------------------------------------------------------------')
        if escolhaP == '2':
            CelsiusFah = temperatura * 1.8 + 32 
            print('Sua temperatura em Fahrenheit: ', CelsiusFah)
            break
        elif escolhaP == '3':
            CelsiusKel = temperatura + 273.15
            print('Sua temperatura em Kelvin: ', CelsiusKel)
            break
        else:
            print('Escolha inválida. Tente novamente.')
            break
    if escolha == '2':
        print('-------------------------------------------------------------')
        escolhaP = input('Escolha foi Fahrenheit, para qual temperatura você vai querer converter 1 para C e 3 para K: ')
        print('-------------------------------------------------------------')
        if escolhaP == '1':
            FahrenheitCel = (temperatura - 32 ) / 1.8 
            print('Sua temperatura em Celsius: ', FahrenheitCel)
            break
        elif escolhaP == '3':
            FahrenheitKel = (temperatura - 32 ) * 5/9 + 273.15
            print('Sua temperatura em Kelvin: ', FahrenheitKel)
            break
        else:
            print('Escolha inválida. Tente novamente.')
            break
    if escolha == '3':
        print('-------------------------------------------------------------')
        escolhaP = input('Escolha foi Kelvin, para qual temperatura você vai querer converter 1 para C e 2 para F: ')
        print('-------------------------------------------------------------')
        if escolhaP == '1':
            KelvinCel = temperatura - 273.15
            print('Sua temperatura em Celsius: ', KelvinCel)
            break
        elif escolhaP == '2':
            KelvinFah = (temperatura - 273.15) * 9/5 + 32
            print('Sua temperatura em Fahrenheit: ', KelvinFah)
            break
        else:
            print('Escolha inválida. Tente novamente.')
            break
