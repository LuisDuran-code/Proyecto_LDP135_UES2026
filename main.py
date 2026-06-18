
import os
from utils.Tools import limpiar_pantalla

from ui.Menu_principal import MenuPrincipal
from ui.Menu_Asistente import MenuAsistente
from Services.Asistente_service import AsistenteService
from Repositories.Asistente_repository import AsistenteRepository
from Repositories.Evento_repository import EventoRepository
from Services.Evento_service import EventoService
from Services.Estadisticas_Service import EstadisticasService
from data.data import eventos_prueba, asistentes_prueba


def main():
    limpiar_pantalla()
    # Crear repositorios
    evento_repo = EventoRepository()
    asistente_repo = AsistenteRepository()

    # Cargar datos de prueba
    for evento in eventos_prueba:
        evento_repo.agregar(evento)

    for asistentes in asistentes_prueba:
        for asistente in asistentes:
            asistente_repo.guardar(asistente)

    # Crear servicios
    evento_service = EventoService(evento_repo)
    asistente_service = AsistenteService(asistente_repo, evento_service)
    estadisticas_service = EstadisticasService(evento_repo)

    menu_principal = MenuPrincipal(asistente_service, evento_service, estadisticas_service)
    menu_principal.mostrar()


if __name__ == "__main__":
    main()