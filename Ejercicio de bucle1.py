# Ejercicio 1: solicite al usuario una calificaion numerica y determine el grado segun la escala de la imagen de la actividad
print("Ejercicio 1: Calificación numérica a letra")
calificacion = int(input("Ingresa la calificación numérica: "))

if calificacion >= 90:
    print("Tu calificación es: A")
elif calificacion >= 80:
    print("Tu calificación es: B")
elif calificacion >= 70:
    print("Tu calificación es: C")
elif calificacion >= 60:
    print("Tu calificación es: D")
else:
    print("Tu calificación es: F")

print()  # Espacio en blanco para separar los ejercicios

# Ejercicio 2: Determinar si un número es positivo, negativo o cero
print("Ejercicio 2: Determinar si un número es positivo, negativo o cero")
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")