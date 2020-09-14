"""
Excepciones: cuando hay un error en tu código.
Las excepciones se manejan con keywords como: try, except, finally. Varía en el lenguaje
"""


def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    #Permiten asegurarnos manejar las excepciones con try and except!
    except ZeroDivisionError as e:
        return lista


lista = list(range(10))
divisor = 3

print(divide_elementos_de_lista(lista, divisor))

"""
Excepciones comunes: 
    ImportError : una importación falla
    IndexError : una lista se indexa con un número fuera de rango
    NameError : se usa una variable desconocida
    SyntaxError : el código no se puede analizar correctamente
    TypeError : se llama a una función en un valor de un tipo inapropiado
    ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado
"""