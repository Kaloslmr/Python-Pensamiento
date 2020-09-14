"""
Afirmaciones: Método de programación defensiva, si los input que recibimos son
del tipo correcto. Cuando este tipo no es correcto nuetro programa nos da un bug de lógica
los resultados dependen de que los input cumplan la condición!
Afirmaciones es un gran método para debuggear.
"""

# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_palabras):
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ['Kalos',5.5, '', 2 , 'Pruebaaa', 0.35]
print('Primeras letras validas son : ' , primera_letra(lista))