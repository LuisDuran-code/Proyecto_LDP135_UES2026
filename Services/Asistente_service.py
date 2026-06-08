from Models.Asistente import Asistente

class AsistenteService:

    def __init__(self, repositorio):
        self.repositorio = repositorio

#registrar asistente

def registrar_asistente(
        self,
        nombre,
        edad,
        correo,
        evento):
    
    if nombre.strip() == "":
        raise ValueError(
            "El nombre no puede estar vacío"
        )
    
    if edad < evento.edad_minima:
        raise ValueError(
            f"Edad mínima requerida: {evento.edad_minima}"
        )
    
    if evento.estado != "Abierto":
        raise ValueError(
            "El evento no acepta registros"
        )
    if len(evento.asistentes) >= evento.capacidad:
        evento.estado = "Lleno"
        raise ValueError(
            "El evento alcanzó su capacidad máxima"
        )
    
    nuevo_asistente = Asistente(
        nombre,
        edad,
        correo
    )

    self.repositorio.guardar(
        nuevo_asistente
    )

    evento.asistentes.append(
        nuevo_asistente
    )

    if len(evento.asistentes) == evento.capacidad:
        evento.estado = "Lleno"
    
    return nuevo_asistente

#Mostrar asistentes

def mostrar_asistentes(self):

    return self.repositorio.obtener_todos()

#Buscar asistente

def buscar_asistente(self, nombre):

    return self.repositorio.buscar_por_nombre(
        nombre
    )
