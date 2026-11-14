# ============================================================
# Archivo: ejercicio5.py
# Curso: SOFT-01 - Principios de Programacion 1
# Integrantes: Daniel Cordero
# Fecha: 13/11/2026
# Version: 1.0
# Descripcion: Selección del destino y autorización de la misión.
# ============================================================

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_PERSONA_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_PERSONA_DIA = 1

# Entrada de datos
dias_viaje = int(input("Ingrese los dias del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxigeno disponible: "))
energia = int(input("Ingrese la energia disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Calcular el consumo diario
oxigeno_diario = tripulantes * CONSUMO_OXIGENO_PERSONA_DIA
provisiones_diarias = tripulantes * CONSUMO_PROVISIONES_PERSONA_DIA

# Inicializar variables
dias_transcurridos = 0
viaje_posible = True

# Simular el viaje
while dias_transcurridos < dias_viaje and viaje_posible:

    # Verificar los recursos antes de consumirlos
    if combustible >= CONSUMO_COMBUSTIBLE_DIA and oxigeno >= oxigeno_diario and energia >= CONSUMO_ENERGIA_DIA and provisiones >= provisiones_diarias:

        # Descontar los recursos del dia
        combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno = oxigeno - oxigeno_diario
        energia = energia - CONSUMO_ENERGIA_DIA
        provisiones = provisiones - provisiones_diarias

        # Aumentar los dias completados
        dias_transcurridos = dias_transcurridos + 1

        # Mostrar el estado de los recursos
        print("Dia", dias_transcurridos, "Combustible:", combustible, "Oxigeno:", oxigeno, "Energia:", energia, "Provisiones:", provisiones)

    else:
        # Detener el viaje si faltan recursos
        viaje_posible = False

        print("Viaje interrumpido en el dia", dias_transcurridos + 1, ".")

        # Mostrar cada recurso insuficiente
        if combustible < CONSUMO_COMBUSTIBLE_DIA:
            print("Combustible insuficiente.")

        if oxigeno < oxigeno_diario:
            print("Oxigeno insuficiente.")

        if energia < CONSUMO_ENERGIA_DIA:
            print("Energia insuficiente.")

        if provisiones < provisiones_diarias:
            print("Provisiones insuficientes.")

        print("Dias completados:", dias_transcurridos)

# Resultado final
if dias_transcurridos == dias_viaje:

    print("La nave llego al destino en", dias_transcurridos, "dias.")
    print("Combustible restante:", combustible)
    print("Oxigeno restante:", oxigeno)
    print("Energia restante:", energia)
    print("Provisiones restantes:", provisiones)