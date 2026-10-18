# ============================================================
# Archivo: ejercicio2.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Daniel Cordero, Deylan Tencio
# Fecha: 16/10/2026 Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# Entrada de datos
combustible_disponible = int(input("Digite el combustible disponible: "))
combustible_ida = int(input("Digite el combustible necesario para llegar: "))
combustible_regreso = int(input("Digite el combustible necesario para regresar: "))

# Constantes
Reserva_combustible = 10
UMBRAL_MARGEN = 10
# Calculos
combustible_total = combustible_ida + combustible_regreso + Reserva_combustible

combustible_adicional = combustible_disponible - combustible_total

# Condicional simple
if combustible_adicional < UMBRAL_MARGEN:
    print("Advertencia: el margen adicional de combustible es bajo.")
# Mostrar resultados
print("Verificación de combustible")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", Reserva_combustible, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")