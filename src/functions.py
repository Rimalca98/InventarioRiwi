def agregar_producto():
    # Solicitar el nombre del producto (string)
    nombre = input("Ingrese el nombre del producto: ")
            
    # Solicitar el precio unitario con validación (float)
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio > 0: break
            else: print("Debe ser mayor a 0...")
        except ValueError: # Salir del bucle si el valor es válido
            print("Valor inválido. Por favor ingrese un número para el precio.")
            
            # Solicitar la cantidad con validación (int)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad > 0:
                break
            else:
                print("El numero debe ser mayor a 0...") 
                  
        except ValueError: # Salir del bucle si el valor es válido
            print("Valor inválido. Por favor ingrese un número entero para la cantidad.")
    # Calcular el costo total multiplicando precio por cantidad
    costo_total = precio * cantidad
    # Mostrar los datos del producto registrado
    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


    producto = {"nombre": "Lápiz", "precio": 500, "cantidad": 3}

#def mostrar_inventario():
