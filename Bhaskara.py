import math

print("Vamos Brinca de bhaskara")
A = int(input('Digite o A: '))
print('')
B = int(input('Digite o B: '))
print('')
C = int(input('Digite o C: '))
print('--------')

delta = (B**2) -(4*A*C)

if delta < 0 :
    print('essa equação não possui raíz reais')
elif delta == 0:
    print('AQUI DA DELTA 0')
    x1 = (-B + (math.sqrt(delta))) / (2 * A)
    print('X1 = ', x1)
else:
    x1 = (-B + (math.sqrt(delta))) / (2 * A)
    x2 = (-B - (math.sqrt(delta))) / (2 * A)
    print('X1 = ', x1)
    print('X2 = ', x2)

 
