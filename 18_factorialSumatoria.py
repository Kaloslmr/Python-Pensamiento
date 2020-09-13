#----- 1.- Haremos la suma total de las cantidades que componen a un numero 'n'


#              Función Sumatoria
def sumatoria(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumatoria(numero - 1)


#           Imprimimos resultado
user_number = int(input('Ingresa un número entero para sumar su descomposicion: '))
print(f'El numero {user_number} sumado a sus componentes es {sumatoria(user_number)}')