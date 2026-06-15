# ============================================================
# SISTEMA DE GESTIÓN DE VEHÍCULOS
# Fundamentos de Programación - FPY1101
# EA3: Listas, diccionarios y funciones en Python
# ============================================================


# ------------------------------------------------------------
# FUNCIÓN: mostrar_menu
# ------------------------------------------------------------
# Esta función muestra el menú principal del sistema.
# No recibe datos.
# No retorna datos.
# ------------------------------------------------------------

def mostrar_menu():
    print()
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")


# ------------------------------------------------------------
# FUNCIÓN: leer_opcion
# ------------------------------------------------------------
# Esta función lee la opción que ingresa el usuario.
# Valida que sea un número entero entre 1 y 6.
#
# Retorna:
# - opción válida entre 1 y 6
# - 0 si la opción es inválida
# ------------------------------------------------------------

def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Error: debe ingresar una opción entre 1 y 6.")
            return 0

    except ValueError:
        print("Error: debe ingresar un número entero.")
        return 0


# ------------------------------------------------------------
# FUNCIÓN: validar_modelo
# ------------------------------------------------------------
# Valida que el modelo no esté vacío.
#
# Parámetro:
# - modelo: texto ingresado por el usuario.
#
# Retorna:
# - True si el modelo es válido.
# - False si el modelo está vacío.
# ------------------------------------------------------------

def validar_modelo(modelo):
    if modelo.strip() != "":
        return True
    else:
        return False


# ------------------------------------------------------------
# FUNCIÓN: validar_anio
# ------------------------------------------------------------
# Valida que el año sea mayor que 1900.
#
# Parámetro:
# - anio: número entero.
#
# Retorna:
# - True si el año es válido.
# - False si el año es inválido.
# ------------------------------------------------------------

def validar_anio(anio):
    if anio > 1900:
        return True
    else:
        return False


# ------------------------------------------------------------
# FUNCIÓN: validar_precio
# ------------------------------------------------------------
# Valida que el precio sea mayor que cero.
#
# Parámetro:
# - precio: número decimal.
#
# Retorna:
# - True si el precio es válido.
# - False si el precio es inválido.
# ------------------------------------------------------------

def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False


# ------------------------------------------------------------
# FUNCIÓN: agregar_vehiculo
# ------------------------------------------------------------
# Permite agregar un vehículo a la lista principal.
#
# Parámetro:
# - lista_vehiculos: lista donde se guardan los vehículos.
#
# Cada vehículo se guarda como un diccionario:
# {
#   "modelo": modelo,
#   "anio": anio,
#   "precio": precio,
#   "disponible": False
# }
# ------------------------------------------------------------

def agregar_vehiculo(lista_vehiculos):
    print()
    print("=== AGREGAR VEHÍCULO ===")

    modelo = input("Ingrese el modelo del vehículo: ")

    if not validar_modelo(modelo):
        print("Error: el modelo no puede estar vacío.")
        return

    try:
        anio = int(input("Ingrese el año del vehículo: "))

        if not validar_anio(anio):
            print("Error: el año debe ser mayor que 1900.")
            return

    except ValueError:
        print("Error: el año debe ser un número entero.")
        return

    try:
        precio = float(input("Ingrese el precio del vehículo: "))

        if not validar_precio(precio):
            print("Error: el precio debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: el precio debe ser un número decimal.")
        return

    vehiculo = {
        "modelo": modelo.strip(),
        "anio": anio,
        "precio": precio,
        "disponible": False
    }

    lista_vehiculos.append(vehiculo)

    print("Vehículo agregado correctamente.")


# ------------------------------------------------------------
# FUNCIÓN: buscar_vehiculo
# ------------------------------------------------------------
# Busca un vehículo por modelo dentro de la lista.
#
# Parámetros:
# - lista_vehiculos: lista donde están los vehículos.
# - modelo_buscado: modelo que se quiere buscar.
#
# Retorna:
# - posición del vehículo si lo encuentra.
# - -1 si no lo encuentra.
#
# Esta versión busca sin importar mayúsculas, minúsculas
# ni espacios al inicio o final.
# ------------------------------------------------------------

def buscar_vehiculo(lista_vehiculos, modelo_buscado):
    modelo_buscado = modelo_buscado.strip().lower()

    for i in range(len(lista_vehiculos)):
        modelo_actual = lista_vehiculos[i]["modelo"].strip().lower()

        if modelo_actual == modelo_buscado:
            return i

    return -1


# ------------------------------------------------------------
# FUNCIÓN: mostrar_datos_vehiculo
# ------------------------------------------------------------
# Muestra los datos de un vehículo específico.
#
# Parámetro:
# - vehiculo: diccionario con los datos del vehículo.
# ------------------------------------------------------------

def mostrar_datos_vehiculo(vehiculo):
    print("Modelo:", vehiculo["modelo"])
    print("Año:", vehiculo["anio"])
    print("Precio:", vehiculo["precio"])

    if vehiculo["disponible"] == True:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: NO DISPONIBLE")


# ------------------------------------------------------------
# FUNCIÓN: eliminar_vehiculo
# ------------------------------------------------------------
# Elimina un vehículo de la lista usando su modelo.
#
# Parámetro:
# - lista_vehiculos: lista donde están guardados los vehículos.
# ------------------------------------------------------------

def eliminar_vehiculo(lista_vehiculos):
    print()
    print("=== ELIMINAR VEHÍCULO ===")

    modelo = input("Ingrese el modelo del vehículo que desea eliminar: ")

    posicion = buscar_vehiculo(lista_vehiculos, modelo)

    if posicion != -1:
        lista_vehiculos.pop(posicion)
        print("Vehículo eliminado correctamente.")
    else:
        print(f"El vehículo '{modelo}' no se encuentra registrado.")


# ------------------------------------------------------------
# FUNCIÓN: actualizar_disponibilidad
# ------------------------------------------------------------
# Recorre todos los vehículos y actualiza su disponibilidad.
#
# Regla:
# - Si el año es mayor o igual a 2020, disponible = True.
# - Si el año es menor a 2020, disponible = False.
# ------------------------------------------------------------

def actualizar_disponibilidad(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False


# ------------------------------------------------------------
# FUNCIÓN: mostrar_vehiculos
# ------------------------------------------------------------
# Muestra todos los vehículos registrados en la lista.
#
# Antes de mostrar, actualiza la disponibilidad de todos.
# ------------------------------------------------------------

def mostrar_vehiculos(lista_vehiculos):
    print()
    print("=== LISTA DE VEHÍCULOS ===")

    actualizar_disponibilidad(lista_vehiculos)

    if len(lista_vehiculos) == 0:
        print("No hay vehículos registrados.")
        return

    for vehiculo in lista_vehiculos:
        mostrar_datos_vehiculo(vehiculo)
        print("*********************************************")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
# Aquí comienza el programa.
# Se crea la lista principal y se ejecuta el menú.
# ------------------------------------------------------------

vehiculos = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    # --------------------------------------------------------
    # OPCIÓN 1: Agregar vehículo
    # --------------------------------------------------------
    if opcion == 1:
        agregar_vehiculo(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 2: Buscar vehículo
    # --------------------------------------------------------
    elif opcion == 2:
        print()
        print("=== BUSCAR VEHÍCULO ===")

        modelo = input("Ingrese el modelo del vehículo a buscar: ")

        posicion = buscar_vehiculo(vehiculos, modelo)

        if posicion != -1:
            print("Vehículo encontrado en la posición:", posicion)

            # Antes de mostrar, actualizamos disponibilidad.
            actualizar_disponibilidad(vehiculos)

            mostrar_datos_vehiculo(vehiculos[posicion])
        else:
            print("Vehículo no encontrado.")

    # --------------------------------------------------------
    # OPCIÓN 3: Eliminar vehículo
    # --------------------------------------------------------
    elif opcion == 3:
        eliminar_vehiculo(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 4: Actualizar disponibilidad
    # --------------------------------------------------------
    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("Disponibilidad actualizada correctamente.")

    # --------------------------------------------------------
    # OPCIÓN 5: Mostrar vehículos
    # --------------------------------------------------------
    elif opcion == 5:
        mostrar_vehiculos(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 6: Salir
    # --------------------------------------------------------
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break

    # --------------------------------------------------------
    # OPCIÓN INVÁLIDA
    # --------------------------------------------------------
    else:
        print("Intente nuevamente.")