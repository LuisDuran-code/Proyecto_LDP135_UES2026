class Evento:

    def __init__(
        self,
        id_evento,
        nombre,
        ubicacion,
        fecha,
        hora,
        capacidad,
        edad_minima,
        categoria,
        organizador
    ):

        self.id_evento = id_evento
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.hora = hora
        self.capacidad = capacidad
        self.edad_minima = edad_minima
        self.categoria = categoria
        self.organizador = organizador

        self.estado = "Abierto"
        self.asistentes = []