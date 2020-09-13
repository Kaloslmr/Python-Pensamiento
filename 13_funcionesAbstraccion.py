#Poder cambiar el orden de valores o visibilidad en funciones
def nombre_completo(nombre, apellido, inverso=False):
    #Si inverso es TRUE
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'


#Output
print(nombre_completo('Kalos', 'Lazo'))
print(f"Cuando Inverso es Falso: {nombre_completo('Kalos', 'Lazo', inverso=False)}")
print(f"Cuando Inverso es Falso: {nombre_completo('Kalos', 'Lazo', inverso=True)}")
print(f"Usando KeyWords: {nombre_completo(apellido = 'Lazo', nombre = 'Kalos')}")