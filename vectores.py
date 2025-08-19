import numpy as np
#vectores siempre empieza desde 0
vector = np.array([1, 2, 3, 4, 5, 6, 7 , 8, 9, 10])
print("vector original : ", vector)
print(vector[2]) # 3 imprime el valor en la posición 2 osea el 3
"""los vectores no son como las listas, no tienen un metodo append() para agregar elemento no tienen un metodo pop para eliminar elementos pero si tienen un metodo reshape() para cambiar la forma del vector, adicionalmente despues de ser creado un vector no se puede cambiar su tamaño"""

vector1 = np.zeros(5)
print("vector de zeros : ", vector1)
vector2 = np.ones(5)
print("vector de unos : ", vector2)
vector3 = np.arange(1,10)
print("vector de rango : ", vector3) 
vector4 = np.linspace(1,10,5)
print("vector de rango con 5 elementos : ", vector4) # 1,
vector5 = np.random.rand(10)
print("vector de numeros aleatorios : ", vector5) # 1, 0.
vector6 = np.random.randint(1,10,10) #vector de numeros aleatorios entre 1 y 10
print("vector de numeros aleatorios entre 1 y 10 : ", vector6) 
