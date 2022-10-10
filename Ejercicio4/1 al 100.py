import random

lista = []
for i in range(100):
    lista.append(i + 1)

listaReverse = list(reversed(lista))

for i in listaReverse:
    print(i)
