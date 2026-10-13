
import csv

# ==========================================
# FASE 1: INICIO DEL SISTEMA E INVENTARIO
# ==========================================

inventario = [
    {"nombre": "Leche Gloria lata de 350 ml", "precio": 4.50, "stock": 20},
    {"nombre": "Arroz Costeno 1 kg", "precio": 4.20, "stock": 30},
    {"nombre": "Aceite Primor 1 litro", "precio": 9.50, "stock": 15},
    {"nombre": "Azucar rubia 1 kg", "precio": 4.00, "stock": 25},
    {"nombre": "Fideos Don Vittorio 500 g", "precio": 3.80, "stock": 18}
]

ventas = []
numero_venta = 1

print("=" * 45)
print(" SISTEMA DE AUTOCObRO Y GESTION DE VENTAS")
print("=" * 45)
print("Inventario cargado correctamente.")


# ==========================================
# FUNCION PARA BUSCAR PRODUCTOS
# ==========================================

def buscar_producto(descripcion):
    for producto in inventario:
        if descripcion.lower() in producto["nombre"].lower():
            return producto
    return None


# ==========================================
# FASE 2, 3 Y 4: CICLO PRINCIPAL DE VENTAS
# ==========================================

while True:

    print("\n--- NUEVA VENTA ---")

    carrito = []
    subtotal = 0

    # Registro continuo de productos
    while True:

        descripcion = input(
            "\nIngrese el nombre del producto (o escriba 'fin'): "
        ).strip()

        if descripcion.lower() == "fin":
            if not carrito:
                print("No hay productos en el carrito.")
                continue
            break

        # Buscar el producto usando FOR
        producto = buscar_producto(descripcion)

        # Validar existencia
        if producto is None:
            print("Producto no encontrado. Intente nuevamente.")
            continue

        print("Producto encontrado:", producto["nombre"])
        print("Precio unitario: S/", round(producto["precio"], 2))
        print("Stock disponible:", producto["stock"])

        # Validar cantidad
        try:
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

        except ValueError:
            print("Error: ingrese una cantidad entera valida.")
            continue

        # Validar stock suficiente
        if cantidad > producto["stock"]:
            print("Stock insuficiente.")
            continue

        # Calcular subtotal del producto
        importe = round(producto["precio"] * cantidad, 2)

        # Agregar al carrito
        carrito.append({
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio": producto["precio"],
            "importe": importe
        })

        subtotal = round(subtotal + importe, 2)

        # Actualizar inventario
        producto["stock"] -= cantidad

        print("Producto agregado al carrito.")
        print("Subtotal actual: S/", f"{subtotal:.2f}")

        # Preguntar si desea agregar otro producto
        while True:
            respuesta = input(
                "Desea agregar otro producto? (si/no): "
            ).strip().lower()

            if respuesta in ("si", "sí", "no"):
                break

            print("Respuesta no valida. Escriba si o no.")

        if respuesta == "no":
            break

    # ==========================================
    # FASE 3: CIERRE DE LA VENTA
    # ==========================================

    # Sumar los importes del carrito usando FOR
    total = 0

    for articulo in carrito:
        total = round(total + articulo["importe"], 2)

    print("\n========== RESUMEN DE VENTA ==========")

    for articulo in carrito:
        print(
            articulo["producto"],
            "| Cantidad:", articulo["cantidad"],
            "| Precio: S/", f"{articulo['precio']:.2f}",
            "| Importe: S/", f"{articulo['importe']:.2f}"
        )

    print("TOTAL A PAGAR: S/", f"{total:.2f}")

    # Validar el pago
    while True:
        try:
            pago = float(input("Ingrese el monto pagado: S/ "))

            if pago < total:
                print("Pago insuficiente. Intente nuevamente.")
            else:
                break

        except ValueError:
            print("Error: ingrese un monto numerico valido.")

    vuelto = round(pago - total, 2)

    # Imprimir boleta
    print("\n" + "=" * 45)
    print("             BOLETA DE VENTA")
    print("=" * 45)
    print("Venta N.°:", numero_venta)

    for articulo in carrito:
        print(
            f"{articulo['producto']} | "
            f"{articulo['cantidad']} x "
            f"S/ {articulo['precio']:.2f} = "
            f"S/ {articulo['importe']:.2f}"
        )

    print("-" * 45)
    print(f"TOTAL:   S/ {total:.2f}")
    print(f"PAGO:    S/ {pago:.2f}")
    print(f"VUELTO:  S/ {vuelto:.2f}")
    print("=" * 45)

    # Guardar venta en el historial
    ventas.append({
        "numero": numero_venta,
        "productos": carrito.copy(),
        "total": total,
        "pago": pago,
        "vuelto": vuelto
    })

    numero_venta += 1

    # ==========================================
    # FASE 4: CONTROL DE CLIENTES
    # ==========================================

    while True:
        otro_cliente = input(
            "\nDesea atender a otro cliente? (si/no): "
        ).strip().lower()

        if otro_cliente in ("si", "sí", "no"):
            break

        print("Respuesta no valida. Escriba si o no.")

    if otro_cliente == "no":
        break


# ==========================================
# FASE 5: REPORTES Y EXPORTACION CSV
# ==========================================

print("\n========== REPORTE DEL DIA ==========")

total_recaudado = 0
productos_vendidos = {}

# Recorrer el historial de ventas
for venta in ventas:
    total_recaudado = round(total_recaudado + venta["total"], 2)

    for articulo in venta["productos"]:
        nombre = articulo["producto"]
        cantidad = articulo["cantidad"]

        if nombre in productos_vendidos:
            productos_vendidos[nombre] += cantidad
        else:
            productos_vendidos[nombre] = cantidad

print("Cantidad de ventas:", len(ventas))
print(f"Total recaudado: S/ {total_recaudado:.2f}")

# Mostrar productos mas vendidos
print("\nPRODUCTOS MAS VENDIDOS:")

if productos_vendidos:
    mayor_cantidad = max(productos_vendidos.values())

    for nombre, cantidad in productos_vendidos.items():
        if cantidad == mayor_cantidad:
            print(f"{nombre}: {cantidad} unidades")

else:
    print("No se registraron productos vendidos.")

# Mostrar productos con stock bajo
print("\nPRODUCTOS CON STOCK BAJO (5 o menos):")

hay_stock_bajo = False

for producto in inventario:
    if producto["stock"] <= 5:
        print(
            producto["nombre"],
            "- Stock restante:", producto["stock"]
        )
        hay_stock_bajo = True

if not hay_stock_bajo:
    print("No hay productos con stock bajo.")

# Exportar historial a CSV
with open(
    "historial_ventas.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as archivo:

    escritor = csv.writer(archivo, delimiter=";")

    escritor.writerow([
        "Numero de venta",
        "Producto",
        "Cantidad",
        "Precio unitario",
        "Importe",
        "Total de venta",
        "Pago",
        "Vuelto"
    ])

    for venta in ventas:
        for articulo in venta["productos"]:
            escritor.writerow([
                venta["numero"],
                articulo["producto"],
                articulo["cantidad"],
                f"{articulo['precio']:.2f}",
                f"{articulo['importe']:.2f}",
                f"{venta['total']:.2f}",
                f"{venta['pago']:.2f}",
                f"{venta['vuelto']:.2f}"
            ])

print("\nHistorial exportado a historial_ventas.csv")
print("Sistema de ventas cerrado correctamente.")
