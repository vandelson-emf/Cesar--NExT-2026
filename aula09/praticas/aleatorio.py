import random
from datetime import datetime, timedelta


nomes = ['Deangelis', 'Bia', 'Carol', 'Bedor', 'Paulo']

'''for _ in range(10):
    print(random.randint(1, 10))'''

print(random.choice(nomes))
print(random.sample(nomes, 3))

random.shuffle(nomes)
print(nomes)

agora = datetime.now()
print(agora)

data_formatada = agora.strftime("%d🐍%m/%Y")
print(data_formatada)
