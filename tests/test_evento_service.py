import unittest

from Models.Evento import Evento
from Repositories.Evento_repository import EventoRepository
from Services.Evento_service import EventoService


class TestEventoService(unittest.TestCase):

    def setUp(self):
        self.repositorio = EventoRepository()
        self.service = EventoService(self.repositorio)

    def test_crear_evento_exitosamente(self):
        resultado = self.service.crear_evento(
            nombre="Feria de Software",
            ubicacion="Campus",
            fecha="15/07/2026",
            hora="10:00",
            capacidad=50,
            edad_minima=16,
            categoria="Educacion",
            organizador="UES"
        )

        self.assertTrue(resultado)
        eventos = self.repositorio.obtener_todos()
        self.assertEqual(len(eventos), 1)
        self.assertEqual(eventos[0].id_evento, 1)
        self.assertEqual(eventos[0].nombre, "Feria de Software")
        self.assertEqual(eventos[0].estado, "Abierto")

    def test_actualizar_estado_evento_lleno(self):
        evento = Evento(
            id_evento=1,
            nombre="Charla Tecnica",
            ubicacion="Auditorio",
            fecha="20/07/2026",
            hora="09:00",
            capacidad=2,
            edad_minima=18,
            categoria="Tecnologia",
            organizador="UES"
        )
        self.repositorio.agregar(evento)
        evento.asistentes.append(object())
        evento.asistentes.append(object())

        self.service.actualizar_estado_evento(evento.id_evento)

        self.assertEqual(evento.estado, "Lleno")


if __name__ == "__main__":
    unittest.main()
