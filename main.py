print("1. Agregar Producto")
print("2. Mostrar inventario")
print("3. Calcular estadistica")
print("4. Salir")

opcion = int(input("Seleccione una opcion:"))

while opcion < 1 or opcion > 4:
        print ("Opción no válida.")
        opcion = int(input("Seleccione una opción: "))
        
if opcion == 1:
    # Solicitar el nombre del producto (string)
    nombre = input("Ingrese el nombre del producto: ")
            
    # Solicitar el precio unitario con validación (float)
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            break
        except ValueError: # Salir del bucle si el valor es válido
            print("Valor inválido. Por favor ingrese un número para el precio.")
            
            # Solicitar la cantidad con validación (int)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break  
        except ValueError: # Salir del bucle si el valor es válido
                    print("Valor inválido. Por favor ingrese un número entero para la cantidad.")
            # Calcular el costo total multiplicando precio por cantidad
                    costo_total = precio * cantidad
            # Mostrar los datos del producto registrado
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")




