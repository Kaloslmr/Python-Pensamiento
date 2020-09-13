#Generamos una lista:
lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
#Con esto hacemos que la lista sea ordenada!
lista.sort()
print(lista)


#Primero: Buscar el punto medio
#Segundo: Comprobar si el punto medio es el valor que buscamos
#Tercero: Si el numero es menor al valor que buscamos aumentamos al inicio punto medio + 1 
#Cuarto: Si el numero es mayor al valor que buscamos disminuimos el final punto medio - 1
#Quinto: Si el inicio es mayor o igual que el final entonces el número no está en la lista.



def busqueda_binaria(valor):
    #Indicador de Inicio
    inicio = 0
    #Indicador de final
    final = len(lista) - 1
    while inicio <= final:
        puntoMedio = (inicio + final) // 2
        if valor == lista[puntoMedio]:
            return puntoMedio
        elif valor > lista[puntoMedio]:
            inicio = puntoMedio + 1
        else:
            final = puntoMedio - 1
    return None



def display_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f'El número {valor} no está en la lista'
    else:
        return f'El número {valor} se encuentra en la posición {res_busqueda}'

print(display_valor(16))
print(display_valor(0))
print(display_valor(88))
print(display_valor(47))