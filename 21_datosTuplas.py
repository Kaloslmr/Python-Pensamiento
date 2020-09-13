"""
Tuplas: Secuencias inmutables de objetos, no se pueden modificar.
Se definen con paréntesis y comas, si dentro de la tupla solo hay un valor
se necesita poner de igual forma la ','!
"""

my_tuple = (1, 'dos', True)
my_tuple[0] # Esto es igual al índice 0 de nuestra tupla: '1'
my_tuple = (1,) #Se necesita poner coma aunque solo haya un valor


my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(my_tuple) # (1,2,3,4)


x, y, z = my_other_tuple # Asignamos variables a cada valor: x = 2, y = 3, z = 4


#Función que regresa una tupla
def coordenadas():
    return(5, 4)


coordenada = coordenadas()
print(coordenada) # (5, 4)
x, y = coordenadas()
print(x, y) # 5 4




