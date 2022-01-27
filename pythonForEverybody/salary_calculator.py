"""
3.1 Escriba un programa para pedirle al usuario las horas y la tarifa por hora usando la entrada para calcular el salario bruto.
 Paga la tarifa por hora por las horas hasta 40 y 1.5 veces la tarifa por hora para todas las horas que se trabajaron por encima 
 de las 40 horas. Use 45 horas y una tasa de 10.50 por hora para probar el programa (la paga debe ser 498.75). Debes utilizar 
 input para leer una cadena y float () para convertir la cadena en un número. No se preocupe por la comprobación de errores en 
 la entrada del usuario: suponga que el usuario escribe los números correctamente.
"""
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

if hrs <= 40:
    totalPay = hrs * rate
    print(totalPay)
else : #Hrs up to 40 pays 1.5 more
    normalPay = 40 * rate
    extraHrs = hrs - 40
    extraRate = rate * 1.5
    extraPay = extraHrs * extraRate
    totalPay = normalPay + extraPay
    print( totalPay )

