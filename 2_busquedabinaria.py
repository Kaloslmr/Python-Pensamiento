objetivo = int(input('Escoge un numero entero: '))
epsilon = 0.01
limiteInferior = 0.0
#Valor mas alto entre dos valores:
valorAlto = max(1.0, objetivo)
respuesta = (valorAlto + limiteInferior) / 2


while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        limiteInferior = respuesta
    else:
        valorAlto = respuesta
    
    respuesta = (valorAlto + limiteInferior) / 2


print(f'La raiz cuadrada de {objetivo} es {respuesta}')