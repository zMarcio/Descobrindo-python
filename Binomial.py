# def fatorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fatorial(num - 1)
    
# # resultado2 = fatorial(5)
# # print(resultado2)

# def binomialCoeficiente(n, k):
#     if k > n:
#         return 0

#     coeficiente = fatorial(n)
#     return coeficiente

# n = int(input('Digite o valor de n: '))
# k = int(input('Digite o valor de k: '))

# resultado = binomialCoeficiente(n, k)
# print("O coeficiente binomial C(", n, ",", k, ") é:", resultado)
# 1


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    fat = 1
    while(n > 1):
        fat = fat * n
        n = n - 1
    return fat     

def binomialCoeficiente(n, k):
    if k > n:
        return 0

    coeficiente = fatorial(n) // (fatorial(k) * fatorial(n-k))
    return coeficiente

resultado = binomialCoeficiente(10, 6)
print(resultado)