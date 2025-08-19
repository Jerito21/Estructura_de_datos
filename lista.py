lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
#lista de acesso 
print(lista[6])


lista_vacia = []
#lista vacia 
lista_vacia.append(1)
print(lista_vacia)

lista_vacia.append("hola")
print(lista_vacia)

lista_vacia.insert(1, True)

print(lista_vacia)

print(f"ultimo elemento de la lista es{lista_vacia[-1]}")

print(f"cuantos elementos tiene la lista{len(lista_vacia)}")

lista_vacia.remove(1)

lista_vacia.pop()
print(lista_vacia)

lista_vacia[0] = "modificado"
print(lista_vacia)

print("\033[34mPotencia de vectores:", lista_vacia)

lista_vacia.extend([1,2,3])

print("\033[35m Lista extendida:",lista_vacia, "\033[0m")

lista_de_listas = [[1,2,3], [4,5,6], [7,8,9]]
print("\033[32m Lista de listas:",lista_de_listas, "\033[0m")

print("\033[33m elemento de la lista de listas:",lista_de_listas[1][2], "\033[0m")

import random
lista_aleatoria = [random.randint(1,100) for _ in range(10)]

print("\033[35m Lista aleatoria:",lista_aleatoria, "\033[0m")

import numpy as np
lista_numpy = np.random.randint(1, 100, size=10).tolist()

print("\033[35m Lista numpy aleatoria:",lista_numpy, "\033[0m")

lista_numpy.sort()
print("\033[36m Lista numpy ordenada:",lista_numpy, "\033[0m")

lista_numpy.reverse()
print("\033[36m Lista numpy invertida:",lista_numpy, "\033[0m")

print("\033[36m buscar un elemento en la lista numpy:", 30 in lista_numpy, "\033[0m")

print("\033[36m buscar un elemento en la lista numpy:", 2 in lista_vacia, "\033[0m")

print("\033[36m buscar un elemento en la lista numpy:", lista_vacia.index(2), "\033[0m")

print("\033[36m buscar un elemento en la lista numpy:", lista_vacia.count(50), "\033[0m")

lista_copiada = lista_numpy.copy()
print("\033[36m Lista numpy invertida:",lista_copiada, "\033[0m")

listaCopia=lista_numpy[:]
print("\033[36m copia num:", listaCopia, "\033[0m")
