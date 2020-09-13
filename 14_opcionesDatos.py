#We are going to give differents solutions to user 


#FUNCIÓN DE BUSQUEDA BINARIA!
def busqueda_binaria (objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'>>> bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2   
        print(f'>>> La raiz cuadrada de {objetivo} es {respuesta}')


#FUNCION DE BUSQUEDA APROXIMACION
def aproximacion (objetivo, epsilon):
    paso = epsilon**2
    respuesta = 0.0
    iteraciones = 0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        iteraciones += 1
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'>>> No se encontro raiz cuadrada {objetivo}')
    else:
        print(f'>>> La raiz cuadrada de {objetivo} es {respuesta}')


#FUNCION ENUMERACIÓN EXHAUSTIVA
def enumeracion_exhaustiva (objetivo):
    respuesta = 0
    
    while respuesta**2 < objetivo:
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'>>> La raiz de {objetivo} es {respuesta}')
    else:
        print(f'>>> {objetivo} no tiene raiz cuadrada exacta')


#INICIO DEL PROGRAMA
user_name = input('\n>>> Hola, para continuar digite su nombre: ')
print(f'>>> Bienvenido {user_name.capitalize()}, Elija el algoritmo de ordenamiento para buscar la raiz cuadrada de su numero\n')
user_option = int(input(f'>>> 1.Enumeracion Exhaustiva \n>>> 2.Aproximacion \n>>> 3.Busqueda Binaria\n\n<<< Su opción: '))


#CONDICIONALES DEL DISPLAY
if user_option == 1:
    print('\n>>> 1.Enumeracion Exhaustiva')
    numero = int(input('<<< Digite un numero: '))
    enumeracion_exhaustiva(numero)
elif user_option == 2:
    print('\n>>> 2.Aproximacion')
    numero = int(input('<<< Digite un numero: '))
    parametro_epsilon = float(input('<<< Digite un epsilon: '))
    aproximacion(numero,parametro_epsilon)
elif user_option == 3:
    print('\n>>> 3.Busqueda Binaria')
    numero = int(input('<<< Digite un numero: '))
    parametro_epsilon = float(input('<<< Digite un epsilon: '))
    busqueda_binaria(numero,parametro_epsilon)
else:
    print('\n>>> Opción no valida')