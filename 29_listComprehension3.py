#Lista Example:
lista = [valor for valor in range(0, 101) if valor % 2 == 0]
#1- valor a agregar en la lista (VALOR)
#2- un ciclo, for
#3- si queremos un condicional!
print(lista)


#Tupla Example:
tupla = tuple((valor for valor in range(0, 101) if valor % 2 != 0))
print(tupla)


#Diccionario Example:
diccionario = {indice:valor  for indice, valor in enumerate(lista)}
print(diccionario)