import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "idade": [18, 21, 19, 20],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão"],
    "nota": [8.5, 6.0, 9.0, 5.5]
}

df = pd.DataFrame(dados)

print("Tabela completa:")
print(df)

print("\nDuas primeiras linhas:")
print(df.head(2))

print("\nFormato da tabela:")
print(df.shape)

print("\nTipos das colunas:")
print(df.dtypes)
