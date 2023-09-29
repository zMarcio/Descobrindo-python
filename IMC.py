import numpy as np



def calcDeAlgo(peso: float, idade:int, nome:str, altura:float):
    imc = peso // (altura ** 2)
    if imc <= 18.5:
        return print('Desnutrido, ein pai', imc)
    if 18.6 <= imc <= 24.9:
        return print('WOOOWW!!!! Look at him!! Quem você pensa que é com esse double bíceps??!! Chris Bumstead??! O CBUM??!! Eu acho que não, ein pai', imc)
    if 25.0 <= imc <= 29.9:
        return print('Tá rolisso cuidado irmao ele num é bola de boliche não, ein pai', imc)
    if 30.0 <= imc <= 34.9:
        return print('Calma irmão o bolo num é só pá tu não, paia ein pai', imc)
    else:
        return print('Bora vira fit, ein pai', imc)

o = np.random.rand(1000)
oo = np.random.randint(0,1000,1)

p = np.random.randint(40,150,1000)
pp = np.random.randint(0,1000,1)

i = np.random.randint(1,2,1)

numSorteadoPeso = o[oo[0]] + p[pp[0]] 

numSorteadoAltura = o[1] + i[0]

calcDeAlgo(numSorteadoPeso, 15, 'Adenilson', numSorteadoAltura)