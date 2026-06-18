from Models.Evento import Evento
from datetime import datetime

class EventoService:

    def __init__(self, repositorio):
        self.repositorio = repositorio
        # Inicializar siguiente_id basándose en los eventos existentes
        eventos = self.repositorio.obtener_todos()
        if eventos:
            # Encontrar el ID máximo y sumar 1
            max_id = max(evento.id_evento for evento in eventos)
            self.siguiente_id = max_id + 1
        else:
            self.siguiente_id = 1


    def cancelar_evento(self, id_evento):
        evento = self.repositorio.buscar_por_id(id_evento)

        if evento:
            evento.estado = "Cancelado"
            return True

        return False


    def eliminar_evento(self, id_evento):

        return self.repositorio.eliminar(id_evento)

    def crear_evento(
        self,
        nombre,
        ubicacion,
        fecha,
        hora,
        capacidad,
        edad_minima,
        categoria,
        organizador
    ):
        if nombre.strip() == "":
            return False

        if capacidad <= 0:
            return False

        if edad_minima < 0:
            return False

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            return False

        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            return False

        if self.repositorio.buscar_por_nombre(nombre):
            return False

        

        evento = Evento(
            self.siguiente_id,
            nombre,
            ubicacion,
            fecha,
            hora,
            capacidad,
            edad_minima,
            categoria,
            organizador
        )

        self.repositorio.agregar(evento)

        return True


    def modificar_evento(
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
        evento = self.repositorio.buscar_por_id(id_evento)

        if not evento:
            return False

        if nombre.strip() == "":
            return False

        if capacidad <= 0:
            return False

        if edad_minima < 0:
            return False

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            return False

        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            return False

        evento.nombre = nombre
        evento.ubicacion = ubicacion
        evento.fecha = fecha
        evento.hora = hora
        evento.capacidad = capacidad
        evento.edad_minima = edad_minima
        evento.categoria = categoria
        evento.organizador = organizador

        return True


    def obtener_eventos(self):
        return self.repositorio.obtener_todos()


    def buscar_evento_por_nombre(self, nombre):
        return self.repositorio.buscar_por_nombre(nombre)


    def buscar_evento_por_id(self, id_evento):
        return self.repositorio.buscar_por_id(id_evento)


    def actualizar_estado_evento(self, id_evento):

        evento = self.repositorio.buscar_por_id(id_evento)

        if not evento:
            return False

        if len(evento.asistentes) >= evento.capacidad:
            evento.estado = "Lleno"

        elif evento.estado != "Cancelado":
            evento.estado = "Abierto"


    


    

    


 


   


    

    


