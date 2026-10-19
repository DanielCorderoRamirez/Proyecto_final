
# ============================================================
# Archivo: ejercicio4.py
# Curso: SOFT-01 - Principios de Programacion 1
# Integrantes: Daniel Cordero
# Fecha: 18/10/2026
# Version: 1.0
# Descripcion: Verifica si el lanzamiento puede autorizarse.
# ============================================================

# Entrada de datos
combustible_disponible = int(input("Digite el combustible disponible: "))
combustible_ida = int(input("Digite el combustible requerido para llegar: "))
combustible_regreso = int(input("Digite el combustible requerido para regresar: "))
oxigeno_disponible = int(input("Digite el oxigeno disponible: "))
oxigeno_requerido = int(input("Digite el oxigeno requerido: "))
energia_disponible = int(input("Digite la energia disponible: "))
energia_requerida = int(input("Digite la energia requerida: "))
provisiones_disponibles = int(input("Digite las provisiones disponibles: "))
provisiones_requeridas = int(input("Digite las provisiones requeridas: "))

# Constante
RESERVA_COMBUSTIBLE = 10

# Calculo del combustible total
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Verificar si todos los recursos son suficientes
if (combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas):

    print("Lanzamiento autorizado.")

else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
