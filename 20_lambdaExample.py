#Usando función en una linea con lambda
#---------- MULTIPLICACION LAMBDA ----------
multiplicar = lambda x, y: x * y

print(multiplicar(10, 10))
#Output = <<< 100

#---------- COMISION LAMBDA ----------
comisionDisplay = lambda comision: f'>>>Total comisión del mes: {comision}$'

print(comisionDisplay(160))
#Output = Total comisión del mes: 160$