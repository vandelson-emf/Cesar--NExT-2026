import pandas as pd


#print(pd.__version__)

list_notas = [8.0, 7.5, 9.0, 6.5]
#notas = pd.Series(list_notas)
notas = pd.Series(
    list_notas,
    index=['Ana', 'Bruno', 'Carlos', 'Duda']
)

print(list_notas)
print(notas)

notas = notas + 0.5

print(notas)
print(notas.mean())
print(notas.std())
