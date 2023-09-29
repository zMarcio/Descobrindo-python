# dicionario = { "dor":"ai", "felicidade" : "ui", "opa":"q isso", "susto":"FODA-SE"}

# print(dicionario)

# del dicionario["dor"]

# print(dicionario)

# dicionario["opa"] = "Ai amor!"

# print(dicionario)

# print("opa" in dicionario)

# list(dicionario)


# print(dicionario.keys())
# print (dicionario.values())
# print(dicionario.items())

# digitaSouN = int(input('Digite 0 para adicionar um novo contato e 1 para fechar.'))
# nome = str(input("Digite seu nome: "))
# telefone = int(input('Digite o telefone: '))
# endereco = str(input('Digite o endereço: '))
# email = str(input('Digite seu Email: '))

# dicionario = {
#     "Nome",
#     "Telefone",
#     "Endereço",
#     "Email"
# }
contatos = []
while True:
    digitaSouN = int(input('Digite 0 para adicionar um novo contato e 1 para fechar.'))
    if digitaSouN == 0:
        nome = input("Digite seu nome: ")
        telefone = input('Digite o telefone: ')
        endereco = input('Digite o endereço: ')
        email = input('Digite seu Email: ')

        dicionario = {
            "Nome": nome,
            "Telefone": telefone,
            "Endereço": endereco,
            "Email": email
        }

        contatos.append(dicionario)
    elif digitaSouN == 1:
        print('Aqui seus contatos:')
        for contato in contatos:
            print('Nome:', contato["Nome"], ';', 'Telefone:', contato["Telefone"], ';', 'Endereço:', contato["Endereço"], ';', 'Email:', contato["Email"])
        break

    else:
        print("Você digitou algo errado, aqui o que você digitou:", digitaSouN)

