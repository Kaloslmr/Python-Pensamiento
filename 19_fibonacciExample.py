#Funcion de fibonacci en recursiva
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input('Introduce el indice del numero fibonacci: '))
print(fibonacci(number))