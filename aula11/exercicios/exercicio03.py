import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "idade": [18, 21, 19, 20],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão"],
    "nota": [8.5, 6.0, 9.0, 5.5]
}

df = pd.DataFrame(dados)

aprovados = df[df["nota"] >= 7]
recife = df[df["cidade"] == "Recife"]
recife_aprovados = df[(df["cidade"] == "Recife") & (df["nota"] >= 7)]
recuperacao = df[(df["nota"] >= 5) & (df["nota"] < 7)]

print("Estudantes com nota maior ou igual a 7:")
print(aprovados)

print("\nEstudantes de Recife:")
print(recife)

print("\nEstudantes de Recife com nota maior ou igual a 7:")
print(recife_aprovados)

print("\nEstudantes com nota entre 5 e 6.9:")
print(recuperacao)
