"""
Rangos: representan secuencia de enteros, tienen comienzo fin
y pasos, también son inmutables. Consumen poca memoria
"""

# Sintáxis: range(comienzo, fin, pasos)

my_range = range(1, 5)
type(my_range) # <class 'range'>

for i in my_range:
    print(i) # Imprime valores desde el 1 hasta el 4 (No incluye el 5)
my_range = range(0, 7, 2) #Inicia: 0, Termina: 7, Pasos: 2
my_other_range = range(0, 8, 2)


my_range == my_other_range # True, mismo valores en pantalla
for i in my_range:
    print(i) # 0, 2, 4, 6

for j in my_other_range:
    print(j) # 0, 2, 4, 6
my_range is my_other_range #False, por que no tienen mismos parametros


#Imprimir numeros del 0 al 100 pares
for i in range(0, 101, 2):
    print(i)