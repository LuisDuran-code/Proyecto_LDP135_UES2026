# FUNCION 1: CREAR EVENTO



# FUNCION 2: REGISTRAR ASISTENTE (TU PARTE)



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
        crear_evento(eventos, ubicaciones, capacidades, asistentes, estados)
    
    elif opcion == 2:
        registrar_asistente(eventos, capacidades, asistentes, estados)
    
    elif opcion == 3:
        mostrar_eventos(eventos, ubicaciones, capacidades, asistentes, estados)
    
    elif opcion == 4:
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida")
