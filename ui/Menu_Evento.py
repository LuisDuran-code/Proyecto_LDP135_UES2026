class MenuEvento:

    def __init__(self, service):
        self.service = service

    def mostrar_menu(self):

        while True:

            print("\n====================================")
            print("      GESTIÓN DE EVENTOS")
            print("====================================")

            print("1. Crear Evento")
            print("2. Modificar Evento")
            print("3. Cancelar Evento")
            print("4. Eliminar Evento")
            print("5. Mostrar Eventos")
            print("6. Buscar Evento por ID")
            print("7. Buscar Evento por Nombre")
            print("0. Volver")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "0":
                break



            elif opcion == "1":

                print("\n=== CREAR EVENTO ===")

                nombre = input("Nombre: ")
                ubicacion = input("Ubicación: ")
                fecha = input("Fecha (dd/mm/yyyy): ")
                hora = input("Hora (HH:MM): ")

                capacidad = int(input("Capacidad: "))
                edad_minima = int(input("Edad mínima: "))

                categoria = input("Categoría: ")
                organizador = input("Organizador: ")

                resultado = self.service.crear_evento(
                    nombre,
                    ubicacion,
                    fecha,
                    hora,
                    capacidad,
                    edad_minima,
                    categoria,
                    organizador
                )

                if resultado:
                    print("\nEvento creado correctamente.")
                else:
                    print("\nError al crear el evento.")

                input("\nPresione ENTER para continuar...")



            elif opcion == "2":

                print("\n=== MODIFICAR EVENTO ===")

                id_evento = int(input("ID del evento: "))

                nombre = input("Nuevo nombre: ")
                ubicacion = input("Nueva ubicación: ")
                fecha = input("Nueva fecha (dd/mm/yyyy): ")
                hora = input("Nueva hora (HH:MM): ")

                capacidad = int(input("Nueva capacidad: "))
                edad_minima = int(input("Nueva edad mínima: "))

                categoria = input("Nueva categoría: ")
                organizador = input("Nuevo organizador: ")

                resultado = self.service.modificar_evento(
                    id_evento,
                    nombre,
                    ubicacion,
                    fecha,
                    hora,
                    capacidad,
                    edad_minima,
                    categoria,
                    organizador
                )

                if resultado:
                    print("\nEvento modificado correctamente.")
                else:
                    print("\nNo se pudo modificar el evento.")

                input("\nPresione ENTER para continuar...")



            elif opcion == "3":

                id_evento = int(input("\nIngrese el ID del evento a cancelar: "))
            
                resultado = self.service.cancelar_evento(id_evento)
            
                if resultado:
                    print("\nEvento cancelado correctamente.")
                else:
                    print("\nNo se encontró el evento.")
                input("\nPresione ENTER para continuar...")



            elif opcion == "4":

                id_evento = int(input("\nIngrese el ID del evento a eliminar: "))

                resultado = self.service.eliminar_evento(id_evento)

                if resultado:
                    print("\nEvento eliminado correctamente.")
                else:
                    print("\nNo se encontró el evento.")
                input("\nPresione ENTER para continuar...")




            elif opcion == "5":

                eventos = self.service.obtener_eventos()

                if not eventos:
                    print("\nNo hay eventos registrados.")

                else:
                    print("\n=== LISTA DE EVENTOS ===")

                    for evento in eventos:
                        print("\n----------------------")

                        print("ID:", evento.id_evento)
                        print("Nombre:", evento.nombre)
                        print("Ubicación:", evento.ubicacion)
                        print("Fecha:", evento.fecha)
                        print("Hora:", evento.hora)
                        print("Capacidad:", evento.capacidad)
                        print("Edad mínima:", evento.edad_minima)
                        print("Categoría:", evento.categoria)
                        print("Organizador:", evento.organizador)
                        print("Estado:", evento.estado)
                input("\nPresione ENTER para continuar...")




            elif opcion == "6":

                id_evento = int(input("\nIngrese el ID del evento: "))

                evento = self.service.buscar_evento_por_id(id_evento)

                if evento:

                    print("\n=== EVENTO ENCONTRADO ===")

                    print("ID:", evento.id_evento)
                    print("Nombre:", evento.nombre)
                    print("Ubicación:", evento.ubicacion)
                    print("Fecha:", evento.fecha)
                    print("Hora:", evento.hora)
                    print("Capacidad:", evento.capacidad)
                    print("Edad mínima:", evento.edad_minima)
                    print("Categoría:", evento.categoria)
                    print("Organizador:", evento.organizador)
                    print("Estado:", evento.estado)

                else:
                    print("\nNo se encontró un evento con ese ID.")
                input("\nPresione ENTER para continuar...")




            elif opcion == "7":

                nombre = input("\nIngrese el nombre del evento: ")

                evento = self.service.buscar_evento_por_nombre(nombre)

                if evento:
                
                    print("\n=== EVENTO ENCONTRADO ===")

                    print("ID:", evento.id_evento)
                    print("Nombre:", evento.nombre)
                    print("Ubicación:", evento.ubicacion)
                    print("Fecha:", evento.fecha)
                    print("Hora:", evento.hora)
                    print("Capacidad:", evento.capacidad)
                    print("Edad mínima:", evento.edad_minima)
                    print("Categoría:", evento.categoria)
                    print("Organizador:", evento.organizador)
                    print("Estado:", evento.estado)

                else:
                    print("\nNo se encontró un evento con ese nombre.")
                input("\nPresione ENTER para continuar...")