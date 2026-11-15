
# ============================================================
# Archivo: ejercicio8.py
# Curso: SOFT-01 - Principios de Programacion 1
# Integrantes: Daniel Cordero
# Fecha: 13/11/2026
# Version: 1.0
# Descripcion: Evaluación del regreso y supervivencia de la tripulació
# ============================================================

# Constantes del consumo diario
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_PERSONA_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_PERSONA_DIA = 1

# Entrada de datos
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Calcular el combustible necesario para iniciar el regreso
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
oxigeno_diario = tripulantes * CONSUMO_OXIGENO_PERSONA_DIA
provisiones_diarias = tripulantes * CONSUMO_PROVISIONES_PERSONA_DIA

# Decidir si la nave puede iniciar el regreso
if combustible >= combustible_regreso:
    dias_transcurridos = 0
    regreso_posible = True

    # Simular cada día del regreso
    while dias_transcurridos < dias_viaje and regreso_posible:

        # Comprobar los cuatro recursos antes de consumirlos
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA and
                oxigeno >= oxigeno_diario and
                energia >= CONSUMO_ENERGIA_DIA and
                provisiones >= provisiones_diarias):

            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - oxigeno_diario
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - provisiones_diarias

            dias_transcurridos = dias_transcurridos + 1

            print("Día", dias_transcurridos,
                  "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno,
                  "| Energía:", energia,
                  "| Provisiones:", provisiones)

        else:
            regreso_posible = False

            print("El regreso se interrumpió en el día " +
                  str(dias_transcurridos + 1) + ".")

            # Identificar todos los recursos insuficientes
            if combustible < CONSUMO_COMBUSTIBLE_DIA:
                print("Combustible insuficiente.")

            if oxigeno < oxigeno_diario:
                print("Oxígeno insuficiente.")

            if energia < CONSUMO_ENERGIA_DIA:
                print("Energía insuficiente.")

            if provisiones < provisiones_diarias:
                print("Provisiones insuficientes.")

            print("La tripulación no completó el regreso.")

    # Mostrar el resultado del regreso completo
    if dias_transcurridos == dias_viaje:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible)
        print("Oxígeno restante:", oxigeno)
        print("Energía restante:", energia)
        print("Provisiones restantes:", provisiones)

else:
    # Estimar la supervivencia cuando falta combustible para regresar
    print("La tripulación quedó varada en el destino.")

    dias_oxigeno = oxigeno // oxigeno_diario
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // provisiones_diarias

    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

    # Encontrar el menor valor mediante condicionales
    supervivencia_estimada = dias_oxigeno

    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    print("Supervivencia estimada:", supervivencia_estimada, "días")
    print("Recurso(s) limitante(s):")

    # Mostrar todos los recursos que empatan en el mínimo
    if dias_oxigeno == supervivencia_estimada:
        print("Oxígeno")

    if dias_energia == supervivencia_estimada:
        print("Energía")

    if dias_provisiones == supervivencia_estimada:
        print("Provisiones")
