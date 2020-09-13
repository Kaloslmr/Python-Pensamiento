#Imprimir si un numero tiene raiz cuadrada o no!

user_Number = int(input('Ingresa un numero entero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - user_Number) >= epsilon and respuesta <= user_Number:
    print(respuesta)
    respuesta += paso
if abs(respuesta**2 - user_Number) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {user_Number}')
else:
    print(f'La raiz cuadrada de {user_Number} es {respuesta}')