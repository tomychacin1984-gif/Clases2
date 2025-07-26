#ser vendedor 
cesta = []
seguir = True

while seguir:
    print("2. Agregar producto")
    print("3. Mostrar cesta")
    print("4. Eliminar producto")
    print("5. Calcular total")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "2":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cesta.append([nombre, precio])
        print(f'{nombre} agregado a la cesta.') 
    elif opcion == "3":
        if cesta:
            print("Contenido de la cesta:")
            for item in cesta: 
                nombre, precio = item
                print(f"{nombre} = {precio}")
        else:
            print("La cesta está vacía.")
    elif opcion == "4":
        nombre = input("Nombre del producto a eliminar: ")
        for item in cesta:
            if item[0] == nombre:
                cesta.remove(item)
                print(f'{nombre} eliminado de la cesta.')
                break
        else:
            print(f'{nombre} no se encuentra en la cesta.')
    elif opcion == "5":
        total = sum(item[1] for item in cesta)
        print(f'Total de la compra: {total}')
    elif opcion == "6":
        print("Hasta luego bro, te esperamos cuando quieras")
        seguir = False