from Models.Asistente import Asistente


class AsistenteService:

    def __init__(self, repositorio, evento_service=None):
        self.repositorio = repositorio
        self.evento_service = evento_service

    def registrar_asistente(self, nombre, edad, correo, evento):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        if edad < evento.edad_minima:
            raise ValueError("Edad menor a la permitida")

        if evento.estado == "Lleno":
            raise ValueError("El evento está lleno")

        if evento.estado == "Cancelado":
            raise ValueError("El evento está cancelado")

        nuevo = Asistente(nombre, edad, correo)
        self.repositorio.guardar(nuevo)
        evento.asistentes.append(nuevo)

        if len(evento.asistentes) >= evento.capacidad:
            evento.estado = "Lleno"

        return nuevo
    
    def mostrar_asistentes(self):

        return self.repositorio.obtener_todos()
    
    # Buscar asistente
    def buscar_asistente(self, nombre):

        return self.repositorio.buscar_por_nombre(
            nombre
        )

    

    
