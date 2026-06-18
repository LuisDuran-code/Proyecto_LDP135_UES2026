from Models.Evento import Evento
from Models.Asistente import Asistente

asistentes_prueba = [
    [
        Asistente("Ana Pérez", 28, "ana.perez@example.com"),
        Asistente("Carlos López", 32, "carlos.lopez@example.com"),
        Asistente("María Gómez", 24, "maria.gomez@example.com"),
    ],
    [
        Asistente("Luis Ramírez", 22, "luis.ramirez@example.com"),
        Asistente("Sofía Fernández", 27, "sofia.fernandez@example.com"),
        Asistente("Pablo Torres", 35, "pablo.torres@example.com"),
    ],
    [
        Asistente("Jimena Castillo", 26, "jimena.castillo@example.com"),
        Asistente("Mateo Díaz", 30, "mateo.diaz@example.com"),
        Asistente("Valeria Cruz", 29, "valeria.cruz@example.com"),
    ],
    [
        Asistente("Diego Aguilar", 31, "diego.aguilar@example.com"),
        Asistente("Lucía Navarro", 23, "lucia.navarro@example.com"),
        Asistente("Alejandro Rojas", 33, "alejandro.rojas@example.com"),
    ],
    [
        Asistente("Camila Vargas", 21, "camila.vargas@example.com"),
        Asistente("Hugo Morales", 34, "hugo.morales@example.com"),
        Asistente("Nadia Herrera", 28, "nadia.herrera@example.com"),
    ],
    [
        Asistente("Sara Molina", 25, "sara.molina@example.com"),
        Asistente("Miguel Castro", 36, "miguel.castro@example.com"),
        Asistente("Elena Salazar", 27, "elena.salazar@example.com"),
    ],
    [
        Asistente("Andrés Blanco", 29, "andres.blanco@example.com"),
        Asistente("Paula Paredes", 24, "paula.paredes@example.com"),
        Asistente("Iván Varela", 32, "ivan.varela@example.com"),
    ],
    [
        Asistente("Clara Medina", 26, "clara.medina@example.com"),
        Asistente("Jorge Peña", 31, "jorge.pena@example.com"),
        Asistente("Nuria Gallego", 30, "nuria.gallego@example.com"),
    ],
    [
        Asistente("Rosa Cabrera", 33, "rosa.cabrera@example.com"),
        Asistente("Óscar Solís", 28, "oscar.solis@example.com"),
        Asistente("Marta León", 22, "marta.leon@example.com"),
    ],
    [
        Asistente("Enrique Bravo", 35, "enrique.bravo@example.com"),
        Asistente("Paula Duarte", 27, "paula.duarte@example.com"),
        Asistente("Bruno Silva", 29, "bruno.silva@example.com"),
    ],
]

eventos_prueba = []

for i in range(1, 11):
    evento = Evento(
        i,
        f"Evento de prueba {i}",
        f"Ubicación {i}",
        f"{10 + i:02d}/06/2026",
        f"{i % 24:02d}:00",
        4,
        18,
        f"Categoría {i}",
        f"Organizador {i}"
    )
    evento.asistentes = asistentes_prueba[i - 1]
    eventos_prueba.append(evento)

