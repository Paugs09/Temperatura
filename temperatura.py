"""Programa No.3
Programa para convertir grados celcius a kelvin y farenheit"""

print("---------------------------------------")
print("Temperatura")
print("---------------------------------------")

#input
c=int(input("Digite la temperatura en grados celcius: "))

#processing
k=(c+273.15)
f=(1.8*c+32)

#output
print("\nEn grados Kelvin:\n")
print("La conversión da como resultado: " + str(k) +  "° kelvin ")
print("\nEn grados Farenheit:\n")
print("La conversión da como resultado: " + str(f) + "° Farenheit ")