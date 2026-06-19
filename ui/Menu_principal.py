from ui.Menu_Asistente import MenuAsistente
from ui.Menu_Evento import MenuEvento
from ui.Menu_Estadisticas import MenuEstadisticas
from utils.Tools import limpiar_pantalla


class MenuPrincipal:
    def __init__(self, asistente_service, evento_service, estadisticas_service):
        self.menu_asistente = MenuAsistente(asistente_service, evento_service)
        self.menu_evento = MenuEvento(asistente_service, evento_service)
        self.menu_estadisticas = MenuEstadisticas(estadisticas_service)

    def mostrar(self):
        while True:
            limpiar_pantalla()
            print("\n====== MENÚ PRINCIPAL ======")
            print("1. Gestión de asistentes")
            print("2. Gestión de eventos")
            print("3. Estadísticas")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.menu_asistente.mostrar_menu()
            elif opcion == "2":
                self.menu_evento.mostrar_menu()
            elif opcion == "3":
                self.menu_estadisticas.mostrar_menu()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")