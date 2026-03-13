while True:
    try:
        nombre = input("Ingrese nombre: ")
        if not nombre or not nombre.isalpha():
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
            elif not nombre.isalpha():
                print("Error: El nombre debe contener solo letras.")
    except ValueError:
        print("Error: Por favor ingrese un nombre válido.")

    try:
        precio = float(input("Ingrese precio: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
    except ValueError:
        print("Error: Por favor ingrese un precio válido.")
        continue

    try:    
        cantidad = int(input("Ingrese cantidad: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            continue
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")






