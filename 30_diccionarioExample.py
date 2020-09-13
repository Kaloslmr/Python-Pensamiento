"""
Diccionarios: Envez de acceder mediante indices, accedemos por llaves
en otros lenguajes se le llama hashmap, no tienen un orden interno, son
mutables y pueden iterarse igual a las listas!
"""

my_dict = {
    'Kalos': 35,
    'Raul': 49,
    'Jose': 50,
}

#Cuando nosotros sabemos el nombre de la llave
print(my_dict['Kalos'])

#Cuando no existe el valor que nos regrese un numero
print(my_dict.get('Juan', 30))

#Editar un llave y cambiar el valor
my_dict['Jose'] = 20
print(my_dict)

#Para borrar una llave
del my_dict['Raul']
print(my_dict)


#---------- ITERACION ----------
#Imprimir las LLAVES! en iteracion
for llave in my_dict.keys():
    print(llave)

#Imprimir los VALORES! en iteracion
for valor in my_dict.values():
    print(valor)

#Imprimir VALORES y LLAVES! en iteracion
for llave, valor in my_dict.items():
    print(f'{llave} tiene {valor} años.')

#Preguntar si existe una llave en nuestra 
print('Kalos' == my_dict)