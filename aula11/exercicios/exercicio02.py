import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "idade": [18, 21, 19, 20],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão"],
    "nota": [8.5, 6.0, 9.0, 5.5]
}

df = pd.DataFrame(dados)

print("Apenas a coluna nome:")
print(df["nome"])

print("\nColunas nome e nota:")
print(df[["nome", "nota"]])

print("\nPrimeira linha usando iloc:")
print(df.iloc[0])

print("\nNome da terceira pessoa usando iloc:")
print(df.iloc[2]["nome"])

print("\nNome da terceira pessoa usando loc:")
print(df.loc[2, "nome"])
