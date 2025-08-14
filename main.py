clientes = {}
id_producto_global = 1

def crear_cuenta():
    global clientes
    cedula = input("Ingrese cédula: ")
    if cedula in clientes:
        print("Ya existe una cuenta con esa cédula.")
        return

    nombre = input("Ingrese nombre completo: ")
    edad = input("Ingrese edad: ")
    telefono_fijo = input("Ingrese teléfono fijo: ")
    telefono_movil = input("Ingrese teléfono móvil: ")
    email = input("Ingrese correo electrónico: ")
    pais = input("Ingrese país: ")
    departamento = input("Ingrese departamento: ")
    ciudad = input("Ingrese ciudad: ")
    direccion = input("Ingrese dirección: ")

    saldo_inicial = float(input("Ingrese saldo inicial: "))

    clientes[cedula] = {
        "nombre": nombre,
        "edad": edad,
        "telefono_fijo": telefono_fijo,
        "telefono_movil": telefono_movil,
        "email": email,
        "pais": pais,
        "departamento": departamento,
        "ciudad": ciudad,
        "direccion": direccion,
        "saldo": saldo_inicial,
        "estado": "Activo",
        "productos": {},
        "historial": [f"Cuenta creada con saldo inicial {saldo_inicial}"]
    }
    print("Cuenta creada exitosamente.")

def depositar_dinero():
    cedula = input("Ingrese cédula: ")
    if cedula not in clientes:
        print("Cuenta no encontrada.")
        return
    monto = float(input("Ingrese monto a depositar: "))
    clientes[cedula]["saldo"] += monto
    clientes[cedula]["historial"].append(f"Depósito: +{monto}")
    print("Depósito realizado con éxito.")

def solicitar_credito():
    global id_producto_global
    cedula = input("Ingrese cédula: ")
    if cedula not in clientes:
        print("Cuenta no encontrada.")
        return
    monto = float(input("Ingrese monto del crédito: "))
    clientes[cedula]["productos"][id_producto_global] = {
        "monto": monto,
        "pendiente": monto,
        "estado": "Activo"
    }
    clientes[cedula]["historial"].append(f"Crédito solicitado ID {id_producto_global}: +{monto}")
    id_producto_global += 1
    print("Crédito registrado exitosamente.")

def retirar_dinero():
    cedula = input("Ingrese cédula: ")
    if cedula not in clientes:
        print("Cuenta no encontrada.")
        return
    monto = float(input("Ingrese monto a retirar: "))
    if monto > clientes[cedula]["saldo"]:
        print("Saldo insuficiente.")
        return
    clientes[cedula]["saldo"] -= monto
    clientes[cedula]["historial"].append(f"Retiro: -{monto}")
    print("Retiro realizado con éxito.")

def pagar_cuota():
    cedula = input("Ingrese cédula: ")
    if cedula not in clientes:
        print("Cuenta no encontrada.")
        return

    if not clientes[cedula]["productos"]:
        print("El cliente no tiene créditos activos.")
        return

    print("\n--- Créditos del cliente ---")
    for pid, datos in clientes[cedula]["productos"].items():
        print(f"ID: {pid} | Monto total: {datos['monto']} | Pendiente: {datos['pendiente']} | Estado: {datos['estado']}")

    id_producto = int(input("Ingrese ID del crédito a pagar: "))
    if id_producto not in clientes[cedula]["productos"]:
        print("Producto no encontrado.")
        return

    cuota = float(input("Ingrese valor de la cuota: "))
    if cuota > clientes[cedula]["saldo"]:
        print("Saldo insuficiente para pagar la cuota.")
        return

    clientes[cedula]["saldo"] -= cuota
    clientes[cedula]["productos"][id_producto]["pendiente"] -= cuota
    if clientes[cedula]["productos"][id_producto]["pendiente"] <= 0:
        clientes[cedula]["productos"][id_producto]["estado"] = "Pagado"
        print("Crédito pagado en su totalidad.")

    clientes[cedula]["historial"].append(f"Pago cuota crédito ID {id_producto}: -{cuota}")
    print("Pago realizado con éxito.")

def cancelar_cuenta():
    cedula = input("Ingrese cédula: ")
    if cedula not in clientes:
        print("Cuenta no encontrada.")
        return
    if clientes[cedula]["productos"]:
        for datos in clientes[cedula]["productos"].values():
            if datos["estado"] != "Pagado":
                print("No se puede cancelar la cuenta: aún existen créditos activos.")
                return
    clientes[cedula]["estado"] = "Cancelado"
    clientes[cedula]["historial"].append("Cuenta cancelada.")
    print("Cuenta cancelada con éxito.")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear cuenta")
        print("2. Depositar dinero")
        print("3. Solicitar crédito")
        print("4. Retirar dinero")
        print("5. Pagar cuota crédito")
        print("6. Cancelar cuenta")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            solicitar_credito()
        elif opcion == "4":
            retirar_dinero()
        elif opcion == "5":
            pagar_cuota()
        elif opcion == "6":
            cancelar_cuenta()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()