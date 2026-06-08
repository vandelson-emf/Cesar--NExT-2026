import pandas as pd


dados = {
    "vendedor": ["Ana", "Ana", "Bruno", "Bruno", "Carlos", "Carlos"],
    "cidade": ["Recife", "Olinda", "Recife", "Olinda", "Recife", "Olinda"],
    "valor": [1200, 1500, 900, 1000, 2000, 2100]
}

df = pd.DataFrame(dados)

total_por_vendedor = df.groupby("vendedor")["valor"].sum()
media_por_vendedor = df.groupby("vendedor")["valor"].mean()
total_por_cidade = df.groupby("cidade")["valor"].sum()
maior_venda = df["valor"].max()

vendedores_acima_3000 = total_por_vendedor[total_por_vendedor > 3000]

print("Total vendido por vendedor:")
print(total_por_vendedor)

print("\nMédia de venda por vendedor:")
print(media_por_vendedor)

print("\nTotal vendido por cidade:")
print(total_por_cidade)

print("\nMaior venda registrada:")
print(maior_venda)

print("\nVendedores com total acima de 3000:")
print(vendedores_acima_3000)
