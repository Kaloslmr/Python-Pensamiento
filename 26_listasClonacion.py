"""
Clonar Lista: usamos 'slice' o 'list'
"""

a = [1, 2, 3]
print(id(a))
b = a
print(id(b))

#Aquí clonamos la lista!
c = list(a)
print(a)
print(f'ID de "a": {id(a)}') # Diferente dirección de memoria de 'c'
print(c)
print(f'ID de "c": {id(c)}') # Diferente dirección de memoria de 'a'
d = a[::] # :: Significa copiar todos los datos desde inicio a final de 'a'
print(c)
print(f'ID de "d": {id(d)}') # Diferente dirección de memoria de 'c y a'