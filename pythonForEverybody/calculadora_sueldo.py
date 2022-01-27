"""
2.3 Escriba un programa para solicitar al usuario Horas y tarifa por hora utilizando la función input para calcular 
el salario bruto. Utilice 35 horas y una tasa de 2,75 por hora para probar el programa(la paga debe ser 96.25). 
Debes utilizar input() para leer una cadena y float() para convertir la cadena en un número. No se preocupe por 
la comprobación de errores o los datos de usuario incorrectos.
"""
hrs = input("Introduce horas: ")
tasa = input("Tasa por hora? ")

print(float(hrs) * float(tasa))
