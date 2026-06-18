import os
from utils.Tools import limpiar_pantalla

class MenuAsistente:

    def __init__(self, asistente_service, evento_service):

        self.asistente_service = asistente_service
        self.evento_service = evento_service

    def mostrar_menu(self):

        while True:
            limpiar_pantalla()

            print("\n=================================")
            print("    GESTIÓN DE ASISTENTES")
            print("=================================")
            print("1. Registrar Asistente")
            print("2. Mostrar Asistentes")
            print("3. Buscar Asistente")
            print("4. Regresar")
            print("=================================")

            opcion = input("Seleccione una opción: ")


            if opcion == "1":
                try:
                    self.registrar_asistente_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "2":
                try:
                    self.mostrar_asistentes_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "3":
                try:
                    self.buscar_asistente_interactivo()
                except Exception as e:
                    print(f"Error: {e}")

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")

    def registrar_asistente_interactivo(self):
        try:
            eventos = self.evento_service.obtener_eventos()
            if not eventos:
                raise ValueError("No hay eventos registrados")

            print("\nEventos disponibles:")
            for i, evento in enumerate(eventos):
                print(f"{i + 1}. {evento.nombre} - Estado: {evento.estado}")

            indice = int(input("\nSeleccione el número del evento: ")) - 1
            if indice < 0 or indice >= len(eventos):
                raise ValueError("Evento inválido")

            evento = eventos[indice]
            if evento.estado == "Lleno":
                raise ValueError("El evento está lleno")
            if evento.estado == "Cancelado":
                raise ValueError("El evento está cancelado")

            nombre = input("Nombre del asistente: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")

            asistente = self.asistente_service.registrar_asistente(nombre, edad, correo, evento)
            print(f"\nAsistente registrado: {asistente}")
            if evento.estado == "Lleno":
                print("El evento alcanzó su capacidad máxima")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            input("\nPresione ENTER para continuar...")

    def mostrar_asistentes_interactivo(self):
        try:
            eventos = self.evento_service.obtener_eventos()
            if not eventos:
                raise ValueError("No hay eventos registrados")
        except ValueError as e:
            print(f"Error: {e}")
            print("Presione cualquier tecla para continuar...")
            input()
            return

        print("\nEventos disponibles:")
        for i, evento in enumerate(eventos):
            print(f"{i + 1}. {evento.nombre} - Estado: {evento.estado}")

        try:
            indice = int(input("\nSeleccione el número del evento: ")) - 1
        except ValueError:
            print("Debe ingresar un número.")
            print("Presione cualquier tecla para continuar...")
            input()
            return
        if indice < 0 or indice >= len(eventos):
            print("Error: Evento inválido")
            print("Presione cualquier tecla para continuar...")
            input()
            return

        evento = eventos[indice]

        if not evento.asistentes:
            print(f"\nEl evento '{evento.nombre}' no tiene asistentes registrados.")
            print("Presione cualquier tecla para continuar...")
            input()
            return

        print(f"\nAsistentes registrados para el evento '{evento.nombre}':")
        asistesntes = self.asistente_service.mostrar_asistentes()
        for asistente in asistesntes:
            print(asistente)

        print("Presione cualquier tecla para continuar...")
        input()

    #Completado ya no tocar
    def buscar_asistente_interactivo(self):
        nombre = input("Nombre a buscar: ")
        encontrados = self.asistente_service.buscar_asistente(nombre)
        if not encontrados:
            print("No se encontraron asistentes.")
            print("Presione cualquier tecla para continuar...")
            input()
            return
        print("Resultados:")
        for a in encontrados:
            print(a)
        print("Presione cualquier tecla para continuar...")
        input()