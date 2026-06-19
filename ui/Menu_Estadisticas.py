import os
from utils.Tools import limpiar_pantalla

class MenuEstadisticas:

    def __init__(self, estadisticas_service):
        self.estadisticas_service = estadisticas_service

    def mostrar_menu(self):
        while True:
            limpiar_pantalla()
            print("\n====== MENÚ DE ESTADÍSTICAS ======")
            print("1. Ver cantidad de eventos abiertos")
            print("2. Ver cantidad de eventos cerrados")
            print("3. Ver cantidad de eventos cancelados")
            print("4. Ver total de asistentes")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                break
            elif opcion == "1":
                cantidad = self.estadisticas_service.contar_eventos_abiertos()
                print(f"\nEventos abiertos: {cantidad}")
            elif opcion == "2":
                cantidad = self.estadisticas_service.contar_eventos_cerrados()
                print(f"\nEventos cerrados: {cantidad}")
            elif opcion == "3":
                cantidad = self.estadisticas_service.contar_eventos_cancelados()
                print(f"\nEventos cancelados: {cantidad}")
            elif opcion == "4":
                total = self.estadisticas_service.total_asistentes()
                print(f"\nTotal de asistentes: {total}")
            else:
                print("Opción inválida.")

            input("\nPresione ENTER para continuar...")