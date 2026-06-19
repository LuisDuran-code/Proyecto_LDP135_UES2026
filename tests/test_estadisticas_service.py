import unittest

from Models.Evento import Evento
from Repositories.Evento_repository import EventoRepository
from Services.Estadisticas_Service import EstadisticasService


class TestEstadisticasService(unittest.TestCase):

    def setUp(self):
        self.repositorio = EventoRepository()
        self.service = EstadisticasService(self.repositorio)

    def test_contar_eventos_abiertos_y_cancelados(self):
        evento_abierto = Evento(
            id_evento=1,
            nombre="Evento Abierto",
            ubicacion="Sala 1",
            fecha="01/08/2026",
            hora="10:00",
            capacidad=100,
            edad_minima=0,
            categoria="General",
            organizador="UES"
        )
        evento_cancelado = Evento(
            id_evento=2,
            nombre="Evento Cancelado",
            ubicacion="Sala 2",
            fecha="02/08/2026",
            hora="11:00",
            capacidad=50,
            edad_minima=0,
            categoria="General",
            organizador="UES"
        )
        evento_cancelado.estado = "Cancelado"

        self.repositorio.agregar(evento_abierto)
        self.repositorio.agregar(evento_cancelado)

        self.assertEqual(self.service.contar_eventos_abiertos(), 1)
        self.assertEqual(self.service.contar_eventos_cancelados(), 1)
        self.assertEqual(self.service.contar_eventos_cerrados(), 0)

    def test_total_asistentes(self):
        evento1 = Evento(
            id_evento=1,
            nombre="Evento 1",
            ubicacion="Sala 1",
            fecha="03/08/2026",
            hora="12:00",
            capacidad=3,
            edad_minima=0,
            categoria="General",
            organizador="UES"
        )
        evento2 = Evento(
            id_evento=2,
            nombre="Evento 2",
            ubicacion="Sala 2",
            fecha="04/08/2026",
            hora="13:00",
            capacidad=5,
            edad_minima=0,
            categoria="General",
            organizador="UES"
        )
        evento1.asistentes.extend([object(), object()])
        evento2.asistentes.append(object())

        self.repositorio.agregar(evento1)
        self.repositorio.agregar(evento2)

        self.assertEqual(self.service.total_asistentes(), 3)


if __name__ == "__main__":
    unittest.main()
