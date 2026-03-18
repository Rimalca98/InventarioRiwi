from src.functions import agregar_producto


opcion = 1


while opcion != 0:
        
    print("1. Agregar Producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadistica")
    print("4. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Por favor ingrese un numero...")


    if opcion == 1:
            agregar_producto()
    print("\nOpcion invalida\n")




