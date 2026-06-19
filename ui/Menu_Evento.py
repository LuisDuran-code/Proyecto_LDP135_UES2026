import os
from utils.Tools import limpiar_pantalla

class MenuEvento:

    def __init__(self, asistente_service, evento_service):

        self.asistente_service = asistente_service
        self.evento_service = evento_service

    def mostrar_menu(self):

        while True:
            limpiar_pantalla()

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

            print("====================================")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "0":
                break
            elif opcion == "1":
                # Delegar toda la interacción al servicio
                try:
                    self.crear_evento_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "2":
                try:
                    self.modificar_evento_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "3":
                try:
                    self.cancelar_evento_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "4":
                try:
                    self.eliminar_evento_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "5":
                try:
                    self.mostrar_eventos_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "6":
                try:
                    self.buscar_evento_por_id_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "7":
                try:
                    self.buscar_evento_por_nombre_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            else:
                print("Opción inválida.")

        # Métodos interactivos para la interfaz
    def crear_evento_interactivo(self):
        try:
            print("\n=== CREAR EVENTO ===")

            nombre = input("Nombre: ")
            ubicacion = input("Ubicación: ")
            fecha = input("Fecha (dd/mm/yyyy): ")
            hora = input("Hora (HH:MM): ")

            capacidad = int(input("Capacidad: "))
            edad_minima = int(input("Edad mínima: "))

            categoria = input("Categoría: ")
            organizador = input("Organizador: ")

            resultado = self.evento_service.crear_evento(
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

        except ValueError:
            print("Error: Ingrese valores válidos.")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    def cancelar_evento_interactivo(self):
        try:
            id_evento = int(input("\nIngrese el ID del evento a cancelar: "))
        
            resultado = self.evento_service.cancelar_evento(id_evento)
        
            if resultado:
                print("\nEvento cancelado correctamente.")
            else:
                print("\nNo se encontró el evento.")
        except ValueError:
            print("Error: Ingrese un ID válido.")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    
    def modificar_evento_interactivo(self):
        try:
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

            resultado = self.evento_service.modificar_evento(
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

        except ValueError:
            print("Error: Ingrese valores válidos.")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    def eliminar_evento_interactivo(self):
        try:
            id_evento = int(input("\nIngrese el ID del evento a eliminar: "))

            resultado = self.evento_service.eliminar_evento(id_evento)

            if resultado:
                print("\nEvento eliminado correctamente.")
            else:
                print("\nNo se encontró el evento.")
        except ValueError:
            print("Error: Ingrese un ID válido.")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    def mostrar_eventos_interactivo(self):
        try:
            eventos = self.evento_service.obtener_eventos()

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
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    def buscar_evento_por_id_interactivo(self):
        try:
            id_evento = int(input("\nIngrese el ID del evento: "))

            evento = self.evento_service.buscar_evento_por_id(id_evento)

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
        except ValueError:
            print("Error: Ingrese un ID válido.")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

    def buscar_evento_por_nombre_interactivo(self):
        try:
            nombre = input("\nIngrese el nombre del evento: ")

            evento = self.evento_service.buscar_evento_por_nombre(nombre)

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
        except Exception as e:
            print(f"Error: {e}")

        input("\nPresione ENTER para continuar...")

        return True
    

