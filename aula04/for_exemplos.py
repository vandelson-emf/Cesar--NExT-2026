# print (f'\n')

# frutas = ["maçã", "banana", "laranja", "uva", "ração", "desodorante"]

# for fruta in frutas:
#     if fruta in ["ração", "desodorante"]:
#         print(f"{fruta} não é uma fruta!")
#     else:
#         print(f"{fruta} é uma fruta!")

# print ('*'*10)

# idades = [19, 45, 30, 35, 33, 13, 67, 22]

# for idade in idades:
#     if idade > 35:
#         print(f"Idade {idade}.")

# print ('*'*10)

# nome_completo = 'Vandelson Elias Monteiro Filho'

# for letra in nome_completo:
#     print (letra)

# print ('*'*10)

# for palavra in nome_completo.split():
#     print (palavra)

# print ('*'*10)

# notas = []

# qtd_notas = int(input("Quantas notas deseja digitar? "))

# for _ in range(qtd_notas):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)

# print(f"Notas digitadas: {notas}")

# print (f"Média: {sum(notas)/len(notas):.2f}")

# Exibir os numeros pares contidos de 1 a 100
# for numero in range(1, 101):
#     if numero % 2 == 0: print(numero, end=' ')

for numero in range(2, 101, 2): print(numero, end=' ')