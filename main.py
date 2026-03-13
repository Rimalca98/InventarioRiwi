while True:
    nombre = input("Nombre de producto: ")
    if nombre.isalpha():
        break
    print("Solo se permiten letras, intenta de nuevo.")

while True:
    try:
        precio = float(input("Precio: "))
        if precio > 0:
            break
        print("Debe ser mayor que 0...")
    except ValueError:
         print("Ingrese un valor valido...")