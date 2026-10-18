# ============================================================
# Archivo: ejercicio1.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Daniel Cordero, Deylan Tencio
# Fecha: 16/10/2026 Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================
# Entrada de datos
nombre_mision = input("Digite el nombre de la mision: ")
tripulantes = int(input("Digite la cantidad de tripulantes: "))
dias_viaje = int(input("Digite los dias de viaje: "))

# Constantes
combustible_por_dia = 8
reserva_combustible = 10
Oxigeno_persona_dia = 2
Reserva_oxigeno = 5
Energia_por_dia = 5
Energia_exploracion = 10
Provisiones_por_persona_dia = 1
Reserva_provisiones = 3

# Calculo del combustible
combustible_ida = dias_viaje * combustible_por_dia
combustible_regreso = dias_viaje * combustible_por_dia
combustible_total = combustible_ida + combustible_regreso + reserva_combustible

# Calculo del oxigeno
oxigeno_requerido = dias_viaje * tripulantes * Oxigeno_persona_dia + Reserva_oxigeno

# Calculo de la energia
energia_requerida = dias_viaje * Energia_por_dia + Energia_exploracion

# Calculo de las provisiones
provisiones_requeridas = dias_viaje * tripulantes * Provisiones_por_persona_dia + Reserva_provisiones

# Mostrar los resultados
print("Resultados de la mision:")
print("Mision:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duracion estimada hasta el destino:", dias_viaje, "dias")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", reserva_combustible, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxigeno requerido:", oxigeno_requerido, "unidades")