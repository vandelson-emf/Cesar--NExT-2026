import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "idade": [18, 21, 19, 20],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão"],
    "nota": [8.5, 6.0, 9.0, 5.5]
}

df = pd.DataFrame(dados)

df["nota_corrigida"] = df["nota"] + 0.5

df["situacao"] = "Recuperação"
df.loc[df["nota"] >= 7, "situacao"] = "Aprovado"
df.loc[df["nota"] < 5, "situacao"] = "Reprovado"

print(df)
