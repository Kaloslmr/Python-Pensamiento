

def factorial(n):
    """Calcula el factorial de 'n':
    
    'n' int > 0
    'n' es un numero entero mayor a 0
    returns n! ('n' factorial)
    
    """
    if n == 1:
        return 1
    return n * factorial(n-1)


userNumber = int(input('Escribe un numero entero: '))
print(f'{userNumber} factorial es: {factorial(userNumber)}')