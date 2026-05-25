print (f'\n')

frutas = ["maçã", "banana", "laranja", "uva", "ração", "desodorante"]

for fruta in frutas:
    if fruta in ["ração", "desodorante"]:
        print(f"{fruta} não é uma fruta!")
    else:
        print(f"{fruta} é uma fruta!")

print ('*'*10)

idades = [19, 45, 30, 35, 33, 13, 67, 22]

for idade in idades:
    if idade > 35:
        print(f"Idade {idade}.")

print ('*'*10)

nome_completo = 'Vandelson Elias Monteiro Filho'

for letra in nome_completo:
    print (letra)
    # if letra in 'aeiouAEIOU':
    #     print(f'Letra {letra} é uma vogal.')
    # else:
    #     print(f'Caractere {letra} é uma consoante ou espaço.')

print ('*'*10)

for palavra in nome_completo.split():
    print (palavra)

print ('*'*10)