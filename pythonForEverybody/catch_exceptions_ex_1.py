"""3.3 Escriba un programa para solicitar una puntuación entre 0.0 y 1.0. Si el puntaje está fuera de rango, imprima un error. 
Si el puntaje está entre 0.0 y 1.0, imprima un grado usando la siguiente tabla:
Score Grado
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Si el usuario ingresa un valor fuera de rango, imprima un mensaje de error adecuado y salga. Para probar el código, ingrese 
un puntaje de 0.85.
"""
inScore = input("Score: ")
try:
    score = float(inScore)
except:
    print("ERROR. Insert a numeric value.")
    quit()

lowerLimit = 0.0
maxLimit = 1.0

if score < lowerLimit or score > maxLimit:
    print("ERROR. Score must be between 0.0 and 1.0")
else:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
        