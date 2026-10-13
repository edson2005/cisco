
import csv

# ==========================================
# FASE 1: INVENTARIO DE PRODUCTOS
# ==========================================

inventario = [
    {"codigo": 1, "nombre": "Leche Gloria lata 350 ml",
     "precio": 4.50, "stock": 20},
    {"codigo": 2, "nombre": "Arroz Costeno 1 kg",
     "precio": 4.20, "stock": 30},
    {"codigo": 3, "nombre": "Aceite Primor 1 litro",
     "precio": 9.50, "stock": 15},
    {"codigo": 4, "nombre": "Azucar rubia 1 kg",
     "precio": 4.00, "stock": 25},
    {"codigo": 5, "nombre": "Fideos Don Vittorio 500 g",
     "precio": 3.80, "stock": 18},
    {"codigo": 6, "nombre": "Agua San Luis 625 ml",
     "precio": 1.50, "stock": 40},
    {"codigo": 7, "nombre": "Gaseosa Inca Kola 500 ml",
     "precio": 3.00, "stock": 25},
    {"codigo": 8, "nombre": "Yogurt Gloria 1 litro",
     "precio": 7.50, "stock": 12},
    {"codigo": 9, "nombre": "Huevos por unidad",
     "precio": 0.80, "stock": 100},
    {"codigo": 10, "nombre": "Galletas de chocolate",
     "precio": 1.20, "stock": 35},
    {"codigo": 11, "nombre": "Detergente 800 g",
     "precio": 8.50, "stock": 10},
    {"codigo": 12, "nombre": "Jabon de tocador",
     "precio": 2.50, "stock": 20}
]

ventas = []
numero_venta = 1


# ==========================================
# MOSTRAR PRIMERO LA LISTA DE PRODUCTOS
# ==========================================

print("=" * 75)
print("       SISTEMA DE AUTOCObRO Y GESTION DE VENTAS")
print("=" * 75)

print("\nLISTA COMPLETA DE PRODUCTOS")
print("-" * 75)
print(f"{'CODIGO':<8}{'PRODUCTO':<36}{'PRECIO':>12}{'STOCK':>12}")
print("-" * 75)

for producto in inventario:
    print(
        f"{producto['codigo']:<8}"
        f"{producto['nombre']:<36}"
        f"S/ {producto['precio']:>8.2f}"
        f"{producto['stock']:>10}"
    )

print("-" * 75)
print("Total de productos registrados:", len(inventario))


# ==========================================
# FASE 2: REGISTRO DE PRODUCTOS
# ==========================================

while True:

    print(f"\n========== VENTA N.° {numero_venta} ==========")
    carrito = []

    while True:

        try:
            codigo = int(input(
                "\nIngrese el codigo del producto (0 para terminar): "
            ))
        except ValueError:
            print("Error: ingrese un codigo numerico.")
            continue

        if codigo == 0:
            if len(carrito) == 0:
                print("Debe registrar al menos un producto.")
                continue
            break

        # Buscar producto mediante FOR
        producto_encontrado = None

        for producto in inventario:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        # Validar existencia
        if producto_encontrado is None:
            print("Producto no encontrado.")
            continue

        print("Producto:", producto_encontrado["nombre"])
        print("Precio: S/", f"{producto_encontrado['precio']:.2f}")
        print("Stock disponible:", producto_encontrado["stock"])

        try:
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

        except ValueError:
            print("Ingrese una cantidad entera valida.")
            continue

        # Validar stock
        if cantidad > producto_encontrado["stock"]:
            print("Stock insuficiente.")
            continue

        precio = producto_encontrado["precio"]
        importe = round(precio * cantidad, 2)

        carrito.append({
            "codigo": codigo,
            "producto": producto_encontrado["nombre"],
            "cantidad": cantidad,
            "precio": precio,
            "importe": importe
        })

        producto_encontrado["stock"] -= cantidad

        print("Producto agregado al carrito.")
        print("Importe: S/", f"{importe:.2f}")

        respuesta = input(
            "Desea agregar otro producto? (si/no): "
        ).strip().lower()

        while respuesta not in ("si", "sí", "no"):
            respuesta = input("Responda si o no: ").strip().lower()

        if respuesta == "no":
            break


    # ==========================================
    # FASE 3: CIERRE DE LA VENTA
    # ==========================================

    total = 0

    for articulo in carrito:
        total = round(total + articulo["importe"], 2)

    print("\n========== RESUMEN DEL CARRITO ==========")

    for articulo in carrito:
        print(
            articulo["producto"],
            "| Cantidad:", articulo["cantidad"],
            "| Importe: S/", f"{articulo['importe']:.2f}"
        )

    print(f"TOTAL A PAGAR: S/ {total:.2f}")

    while True:
        try:
            pago = float(input("Ingrese el monto pagado: S/ "))

            if pago < total:
                print("Pago insuficiente. Ingrese otro monto.")
            else:
                break

        except ValueError:
            print("Ingrese un monto numerico valido.")

    vuelto = round(pago - total, 2)

    print("\n" + "=" * 45)
    print("             BOLETA DE VENTA")
    print("=" * 45)
    print("Venta N.°:", numero_venta)

    for articulo in carrito:
        print(
            f"{articulo['producto']} x {articulo['cantidad']} "
            f"= S/ {articulo['importe']:.2f}"
        )

    print("-" * 45)
    print(f"TOTAL:  S/ {total:.2f}")
    print(f"PAGO:   S/ {pago:.2f}")
    print(f"VUELTO: S/ {vuelto:.2f}")
    print("=" * 45)

    ventas.append({
        "numero": numero_venta,
        "productos": carrito.copy(),
        "total": total,
        "pago": pago,
        "vuelto": vuelto
    })

    numero_venta += 1

    otro_cliente = input(
        "\nDesea atender a otro cliente? (si/no): "
    ).strip().lower()

    while otro_cliente not in ("si", "sí", "no"):
        otro_cliente = input("Responda si o no: ").strip().lower()

    if otro_cliente == "no":
        break


# ==========================================
# FASE 4: REPORTES DEL DIA
# ==========================================

print("\n========== REPORTE DEL DIA ==========")

total_recaudado = 0
productos_vendidos = {}

for venta in ventas:
    total_recaudado += venta["total"]

    for articulo in venta["productos"]:
        nombre = articulo["producto"]
        cantidad = articulo["cantidad"]

        if nombre in productos_vendidos:
            productos_vendidos[nombre] += cantidad
        else:
            productos_vendidos[nombre] = cantidad

print("Ventas realizadas:", len(ventas))
print(f"Total recaudado: S/ {total_recaudado:.2f}")

print("\nPRODUCTOS MAS VENDIDOS:")

if productos_vendidos:
    mayor = max(productos_vendidos.values())

    for nombre, cantidad in productos_vendidos.items():
        if cantidad == mayor:
            print(nombre, "-", cantidad, "unidades")
else:
    print("No hubo ventas.")

print("\nPRODUCTOS CON STOCK BAJO (5 O MENOS):")

hay_stock_bajo = False

for producto in inventario:
    if producto["stock"] <= 5:
        print(producto["nombre"], "- Stock:", producto["stock"])
        hay_stock_bajo = True

if not hay_stock_bajo:
    print("No hay productos con stock bajo.")


# ==========================================
# FASE 5: EXPORTACION DEL HISTORIAL A CSV
# ==========================================

with open(
    "historial_ventas.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as archivo:

    escritor = csv.writer(archivo, delimiter=";")

    escritor.writerow([
        "Venta", "Codigo", "Producto", "Cantidad",
        "Precio unitario", "Importe", "Total venta",
        "Pago", "Vuelto"
    ])

    for venta in ventas:
        for articulo in venta["productos"]:
            escritor.writerow([
                venta["numero"],
                articulo["codigo"],
                articulo["producto"],
                articulo["cantidad"],
                f"{articulo['precio']:.2f}",
                f"{articulo['importe']:.2f}",
                f"{venta['total']:.2f}",
                f"{venta['pago']:.2f}",
                f"{venta['vuelto']:.2f}"
            ])

print("\nHistorial exportado a historial_ventas.csv")
print("Sistema cerrado correctamente.")
