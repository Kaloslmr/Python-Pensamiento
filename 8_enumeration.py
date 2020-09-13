#Imprimir si un numero tiene raiz cuadrada o no!

user_Number = int(input('Ingresa un numero entero: '))
timer = 0

#Iteracion While!
while timer ** 2 < user_Number:
    print(timer)
    timer += 1

if timer**2 == user_Number:
    print(f'El número {user_Number} SI tiene raiz cuadrada exacta y es: {timer}')
else:
    print(f'El numero {user_Number} NO tiene raiz cuadrada exacta.')