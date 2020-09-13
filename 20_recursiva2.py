total = 0
limite_inf = int(input("Escribe el valor en donde comenzara la sumatoria: "))
limite_sup = int(input("Escribe el valor final que sumara la suma"))

for numero in range(limite_inf, limite_sup):
    total += numero
    print(numero)

print(total)
repeticiones = (limite_sup - limite_inf)/2
print(repeticiones)
resultado_simplificado = (limite_sup + limite_inf - 1)*repeticiones
print(resultado_simplificado)