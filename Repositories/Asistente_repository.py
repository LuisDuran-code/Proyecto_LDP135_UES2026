class AsistenteRepository:

    def __init__(self):
        self.asistentes = []

    def guardar(self, asistente):
        self.asistentes.append(asistente)

    def obtener_todos(self):
        return self.asistentes
    
    def buscar_por_nombre(self, nombre):

        encontrados = []

        for asistente in self.asistentes:

            if nombre.lower() in asistente.nombre.lower():
                encontrados.append(asistente)

        return encontrados
