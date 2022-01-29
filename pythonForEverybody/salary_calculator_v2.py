"""
Escriba un programa para avisar al usuario por horas y tasa por hora utilizando input para calcular el salario bruto. 
El pago debe ser la tarifa normal por horas hasta 40 y 1.5 veces para la tarifa por hora para todas las horas trabajadas 
por encima de las 40 horas. Ponga la lógica para hacer el cálculo de la paga en una función llamada computepay() y use la 
función para hacer el cálculo. La función debe devolver un valor. Use 45 horas y una tasa de 10.50 por hora para probar el 
programa (la paga debe ser 498.75). Debes utilizar input para lee una cadena y float() para convertir la cadena en un número. 
No se preocupe por la comprobación de errores en la entrada del usuario a menos que desee: Usted puede asumir que el usuario 
escribe los números correctamente. No nombre su variable sum o use la función sum().
"""

def computepay(hrs, rate):
    if hrs <= 40:
        totalPay = hrs * rate
        #print(totalPay)
    else:  # Hrs up to 40 pays 1.5 more
        normalPay = 40 * rate
        extraHrs = hrs - 40
        extraRate = rate * 1.5
        extraPay = extraHrs * extraRate
        totalPay = normalPay + extraPay
        #print(totalPay)
    return totalPay

inputHrs = input("Worked hours: ")
try:
    hrs = float(inputHrs)
except:
    print("ERROR. Problem converting the input. Please insert a number.")
    quit()

inputRate = input("Hourly rate: ")
try:
    rate = float(inputRate)
except:
    print("ERROR. Problem converting the input. Please insert a number.")
    quit()

print(computepay(hrs,rate))