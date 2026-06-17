import unittest

from Models.Evento import Evento
from Repositories.Asistente_repository import AsistenteRepository
from Services.Asistente_service import AsistenteService


class TestAsistenteService(unittest.TestCase):

    def setUp(self):

        self.repositorio = AsistenteRepository()
        self.service = AsistenteService(self.repositorio)

        self.evento = Evento(
            id_evento=1,
            nombre="Conferencia Python",
            ubicacion="Universidad",
            fecha="20/06/2025",
            hora="08:00",
            capacidad=2,
            edad_minima=18,
            categoria="Tecnología",
            organizador="UES"
        )

    # ---------------------------------
    # Prueba 1: Registro exitoso
    # ---------------------------------

    def test_registrar_asistente_exitosamente(self):

        asistente = self.service.registrar_asistente(
            "Juan Pérez",
            20,
            "juan@gmail.com",
            self.evento
        )

        self.assertEqual(asistente.nombre, "Juan Pérez")
        self.assertEqual(len(self.evento.asistentes), 1)
        self.assertEqual(self.evento.estado, "Abierto")

    # ---------------------------------
    # Prueba 2: Edad menor a la permitida
    # ---------------------------------

    def test_no_permitir_registro_por_edad(self):

        with self.assertRaises(ValueError):

            self.service.registrar_asistente(
                "Pedro López",
                15,
                "pedro@gmail.com",
                self.evento
            )


if __name__ == "__main__":
    unittest.main()
    