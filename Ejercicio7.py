# ============================================================
# Archivo: ejercicio7.py
# Curso: SOFT-01 - Principios de Programacion 1
# Integrantes: Daniel Cordero
# Fecha: 13/11/2026
# Version: 1.0
# Descripcion: Selección del destino y autorización de la misión.
# ============================================================

# Constantes de consumo y puntos de cada actividad
ENERGIA_ANALIZAR = 8
PUNTOS_ANALIZAR = 10
ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20
ENERGIA_OBSERVAR = 5
PUNTOS_OBSERVAR = 8

# Entrada de recursos disponibles
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de contadores, acumulador y variable de control
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_activa = True

# Repetir el menú mientras continúe la exploración
while exploracion_activa:
    print("\nMENÚ DE EXPLORACIÓN")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una opción: "))

    # Elegir una actividad y comprobar sus recursos antes de descontarlos
    match opcion:
        case 1:
            if energia >= ENERGIA_ANALIZAR:
                energia = energia - ENERGIA_ANALIZAR
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR
                print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_ANALIZAR)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 2:
            if energia >= ENERGIA_MUESTRA and provisiones >= PROVISIONES_MUESTRA:
                energia = energia - ENERGIA_MUESTRA
                provisiones = provisiones - PROVISIONES_MUESTRA
                actividades_realizadas = actividades_realizadas + 1
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA
                print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", PUNTOS_MUESTRA)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 3:
            if energia >= ENERGIA_OBSERVAR:
                energia = energia - ENERGIA_OBSERVAR
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVAR
                print("Actividad realizada: Realizar observación. Puntos obtenidos:", PUNTOS_OBSERVAR)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 4:
            exploracion_activa = False

        case _:
            print("Opción no válida.")

# Salida del resumen final
print("\nRESUMEN DE LA EXPLORACIÓN")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia, "unidades")
print("Provisiones restantes:", provisiones, "unidades")
