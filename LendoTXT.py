
a = []


arquivos = open('py/usuario.txt', 'r')

linhas = arquivos.readline()


for linha in arquivos.readline():
    print(linha)
    a.append(linha.strip())
arquivos.close()

print(a)
