import math

peso = float(input("Introduzca su peso en kilos: "))
estatura = float(input("Introduzca su estatura en metros: "))

imc = peso/math.pow(estatura,2)

print("Su IMC es: " + str(round(imc, 2)))
