# ============================================================
# Archivo: ejercicio3.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Daniel Cordero, Deylan Tencio
# Fecha: 16/10/2026 Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# Entrada de datos
oxigeno_disponible = int(input("Digite el oxigeno disponible: "))
oxigeno_requerido = int(input("Digite el oxigeno requerido: "))
provisiones_disponibles = int(input("Digite las provisiones disponibles: "))
provisiones_requeridas = int(input("Digite las provisiones requeridas: "))

# Verificar los recursos
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")