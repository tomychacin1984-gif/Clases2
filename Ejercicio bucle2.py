# Ejercicio 1: Escribe un programa que tome dos números del usuario y verifique si el primer número es mayor, menor o igual al segundo número.
print("Ejercicio 1: Comparar dos números")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num1} es menor que {num2}")
else:
    print(f"El número {num1} es igual a {num2}")

print()  # aca para dejar un espacio en los ejercicios

# Ejercicio 2: Escribe un programa que tome tres números del usuario y determine cuál es el mayor y cuál es el menor de los tres.
print("Ejercicio 2: Determinar el mayor y menor de tres números")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")