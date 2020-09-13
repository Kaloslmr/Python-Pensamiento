#Importamos librerías
import time


#Pregunta al usuario
user_Value = int(input('>>>Ingresa un numero entero: '))


#Variable contador en 0
initial_Value = 0


#Contador de tiempo total
total_Time = time.time()


#Ciclo valor por valor
while initial_Value**2 < user_Value:
    initial_Value += 1


#Imprimir con condicional IF
if initial_Value**2 == user_Value:
    print(f'\n>>>La raíz cuadrada de {user_Value} es {initial_Value}\n')
else:
    print(f'\n>>>{user_Value} no tiene una raíz exacta.\n')


#Imprimir el tiempo total de ejecución
print(f'El programa se demoró {total_Time} segundos\n')