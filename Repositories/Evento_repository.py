class EventoRepository:

    def __init__(self):
        self.eventos = []

    def agregar(self, evento):
        self.eventos.append(evento)

    def obtener_todos(self):
        return self.eventos

    def buscar_por_id(self, id_evento):
        for evento in self.eventos:

            if evento.id_evento == id_evento:
                return evento

        return None


    def eliminar(self, id_evento):

        evento = self.buscar_por_id(id_evento)

        if evento:
            self.eventos.remove(evento)
            return True

        return False

    def buscar_por_nombre(self, nombre):

        for evento in self.eventos:

            if evento.nombre.lower() == nombre.lower():
                return evento

        return None