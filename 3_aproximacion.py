#Encontrar la raíz de cualquier número sin necesario ser par
user_Objective = int(input('Escoge un número: '))


#Que tan preciso queremos ser
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0


#Ciclo ---> Abs significa valor absoluto
while abs(respuesta**2 - user_Objective) >= epsilon and respuesta <= user_Objective:
    respuesta += paso


#Condicion
if abs(respuesta**2 - user_Objective) >= epsilon:
    print(f'No se encontró la raíz cuadrada del objetivo')
else:
    print(f'La raíz cuadrada de {user_Objective} es {respuesta}')