# ============================================================
# Archivo: ejercicio5.py
# Curso: SOFT-01 - Principios de Programacion 1
# Integrantes: Daniel Cordero
# Fecha: 13/11/2026
# Version: 1.0
# Descripcion: Selección del destino y autorización de la misión.
# ============================================================

# Pedir los datos de la mision
nombre_mision = input("Ingrese el nombre de la mision: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

# Reservas de recursos para la mision
RESERVA_COMBUSTIBLE = 25
RESERVA_PROVISIONES = 10

# Mostrar los destinos
print("Seleccione un destino:")
print("1. Luna")
print("2. Marte")
print("3. Europa")

opcion_destino = int(input("Ingrese una opcion: "))

# Seleccionar el destino
match opcion_destino:
    case 1:
        destino = "Luna"
        dias_viaje = 3
    case 2:
        destino = "Marte"
        dias_viaje = 5
    case 3:
        destino = "Europa"
        dias_viaje = 7
    case _:
        destino = ""
        dias_viaje = 0

# Revisar si el destino es valido
if dias_viaje == 0:
    print("Opcion de destino no valida. La mision no puede planificarse.")

else:
    # Pedir los recursos disponibles
    combustible_disponible = int(input("Combustible disponible: "))
    oxigeno_disponible = int(input("Oxigeno disponible: "))
    energia_disponible = int(input("Energia disponible: "))
    provisiones_disponibles = int(input("Provisiones disponibles: "))

    # Calcular requerimientos de recursos
    combustible_ida = dias_viaje * 10
    combustible_regreso = dias_viaje * 6
    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = tripulantes * dias_viaje * 4
    energia_requerida = tripulantes * dias_viaje * 3

    # Calcular provisiones
    provisiones_requeridas = dias_viaje * tripulantes + RESERVA_PROVISIONES

    # Mostrar los resultados
    print()
    print("RESUMEN DE LA MISION")
    print("Nombre:", nombre_mision)
    print("Destino:", destino)
    print("Tripulantes:", tripulantes)
    print("Dias de viaje:", dias_viaje)

    print("Combustible de ida:", combustible_ida)
    print("Combustible de regreso:", combustible_regreso)
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE)
    print("Combustible total:", combustible_total)
    print("Oxigeno requerido:", oxigeno_requerido)
    print("Energia requerida:", energia_requerida)
    print("Provisiones requeridas:", provisiones_requeridas)

    # Revisar si hay suficientes recursos
    if combustible_disponible >= combustible_total:
        if oxigeno_disponible >= oxigeno_requerido:
            if energia_disponible >= energia_requerida:
                if provisiones_disponibles >= provisiones_requeridas:
                    print("Lanzamiento autorizado.")
                else:
                    print("Lanzamiento no autorizado. La mision debe ser revisada.")
            else:
                print("Lanzamiento no autorizado. La mision debe ser revisada.")
        else:
            print("Lanzamiento no autorizado. La mision debe ser revisada.")
    else:
        print("Lanzamiento no autorizado. La mision debe ser revisada.")
