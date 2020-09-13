#Vamos a representar diccionarios con atributos!

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

#It gives us only the key name but not the value
for estudiante in estudiantes:
    print(f'Nombre de llave: {estudiante}')
#This it's similir like the first 
for estudiante in estudiantes.keys():
    print(estudiante)
#This give us the quantity of students in an object
for numero_estudiantes in estudiantes.values():
    print(f'Numero de estudiantes : {numero_estudiantes}')
#This gives us all items that we called, we need to use items!
for pais_estudiantes, cantidad_estudiantes in estudiantes.items():
    print(f'Estudiantes de {pais_estudiantes} : {cantidad_estudiantes}')