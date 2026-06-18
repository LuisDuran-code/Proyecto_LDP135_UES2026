class EstadisticasService:

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def contar_eventos_abiertos(self):
        eventos = self.repositorio.obtener_todos()
        return sum(1 for evento in eventos if getattr(evento, "estado", None) == "Abierto")

    def contar_eventos_cerrados(self):
        eventos = self.repositorio.obtener_todos()
        return sum(1 for evento in eventos if getattr(evento, "estado", None) == "Cerrado")

    def contar_eventos_cancelados(self):
        eventos = self.repositorio.obtener_todos()
        return sum(1 for evento in eventos if getattr(evento, "estado", None) == "Cancelado")

    def total_asistentes(self):
        eventos = self.repositorio.obtener_todos()
        return sum(len(getattr(evento, "asistentes", [])) for evento in eventos)
