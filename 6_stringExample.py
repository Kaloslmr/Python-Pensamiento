contador = 0

while contador <= 10:
    print(contador, end=' ')
    contador += 1

print('\n\n')

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1
        if contador_interno >= 3:
            break
    
    contador_externo += 1
    contador_interno = 0# resetear este 


frutas = ['manzana', 'pera', 'mango']

iterator = iter(frutas)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("Usando For loop".center(25,'-'))
for fruta in frutas:
    print(f"\t-{fruta}")

estudaintes = {
    'mexico': 10,
    'colombia': 15,
    'puerto rico': 4
}

print("Estudiantes".center(15, '-'))
for pais in estudaintes:
    print(pais.title())

print('\n')

for pais in estudaintes.keys():
    print(pais.title())

print("\n\n")
for numero_de_estudiantes in estudaintes.values():
    print(numero_de_estudiantes)

print("\n\n")
print("pais".title().rjust(11), "estudiantes".title().rjust(13))
for pais, numero_de_estudiantes in estudaintes.items():
    print(f"{pais.title().rjust(11)} : {numero_de_estudiantes}")