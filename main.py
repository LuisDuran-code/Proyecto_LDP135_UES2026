# FUNCION 1: CREAR EVENTO



# FUNCION 2: REGISTRAR ASISTENTE (TU PARTE)
def registrar_asistente(eventos, capacidades, asistentes, estados):
    if len(eventos) == 0:
        print("No hay eventos disponibles para registrar asistentes.")
        return
    
    print("\nEventos disponibles:")
    for i in range(len(eventos)):
        print(f"{i+1}. {eventos[i]} (Asistentes: {asistentes[i]}/{capacidades[i]}, Estado: {'Abierto' if estados[i] == 0 else 'Cerrado'})")
    
    try:
        seleccion = int(input("Seleccione el número del evento al que desea registrarse: "))
        if seleccion < 1 or seleccion > len(eventos):
            print("Número de evento inválido.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        return
    
    indice_evento = seleccion - 1
    
    if estados[indice_evento] == 1:
        print("El evento está cerrado. No se pueden registrar más asistentes.")
        return
    
    if asistentes[indice_evento] >= capacidades[indice_evento]:
        print("El evento ha alcanzado su capacidad máxima. No se pueden registrar más asistentes.")
        return
    
    asistentes[indice_evento] += 1
    print(f"Registro exitoso. Ahora hay {asistentes[indice_evento]} asistentes en el evento '{eventos[indice_evento]}'.")



# FUNCION 3: MOSTRAR EVENTOS
def mostrar_eventos(eventos, ubicaciones, capacidades, asistentes, estados):
    if len(eventos) == 0:
        print("No hay eventos registrados.")
        return
    
    for i in range(len(eventos)):
        print(f"\n--- Evento #{i+1} ---")
        print("Nombre:", eventos[i])
        print("Ubicación:", ubicaciones[i])
        print("Capacidad máxima:", capacidades[i])
        print("Asistentes:", asistentes[i])
        
        if estados[i] == 0:
            print("Estado: Abierto")
        else:
            print("Estado: Cerrado")


# -------------------------------
# PRINCIPAL
# -------------------------------

eventos = []
ubicaciones = []
capacidades = []
asistentes = []
estados = []

opcion = 0  # Variable del menú

while True:
    print("\n==============================")
    print("   SISTEMA DE EVENTOS")
    print("==============================")
    print("1. Crear Evento")
    print("2. Registrar Asistente")
    print("3. Mostrar Eventos")
    print("4. Salir")
    print("==============================")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción inválida")
        continue
    
    if opcion == 1:
        print("1")
    
    elif opcion == 2:
        registrar_asistente(eventos, capacidades, asistentes, estados)
    
    elif opcion == 3:
        mostrar_eventos(eventos, ubicaciones, capacidades, asistentes, estados)
    
    elif opcion == 4:
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida")
