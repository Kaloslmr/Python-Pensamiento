import unittest

"""
Caja Cristal: Se basa en el flujo de el programa, asumen que podemos probar todos
los posibles caminos dentro de nuestra funcion 'recursiones', 'for', etc. 
"""


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaCristalTest(unittest.TestCase):
    #Primera función: 20 años es mayor de edad
    def test_es_mayor_de_edad(self):
        edad = 20
        
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)


    def test_es_menor_de_edad(self):
        edad = 15
        
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()
