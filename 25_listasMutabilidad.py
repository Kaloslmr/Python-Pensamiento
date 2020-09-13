"""
Listas: Podemos hacer crecer la memoria que ocupa una lista, estas son mutables
existen efectos secundarios de usar estos tipos de datos.
"""

my_list = [1, 2, 3]
my_list[0] # int 1
my_list[1:] # Desde el primero + 1 hasta el final (Por que no cuenta primer numero)
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
my_list[0] = 'a'
print(my_list) # ['a', 2, 3, 4]
my_list.pop() # Elimina el último elemento en este caso '4'
print(my_list)


for element in my_list:
    print(element) # a, 2, 3


#Dos nombres apuntan al mismo lugar
a = [1, 2, 3]
b = a
print(a)
print(b)
print(id(a)) #Mismo ID, es decir, si modificas uno el otro tambien se afecta!!!
print(id(b))


c = [a, b]
print(c) #[[1,2,3][1,2,3]]
a.append(5)
print(c) #[[1,2,3,5][1,2,3,5]] Se modifican las dos!!!









