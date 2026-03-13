

nombre = input("Ingrese el nombre del producto: ")
 

while True:
    try:
        precio = float(input("Ingrese el precio unitario: "))
        break
    except ValueError:
        print("Valor inválido. Por favor ingrese un número para el precio.")
 

while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        break  
    except ValueError:
        print("Valor inválido. Por favor ingrese un número entero para la cantidad.")
 
 

costo_total = precio * cantidad
 
 

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")