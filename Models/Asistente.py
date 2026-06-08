class Asistente:

    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} | Edad: {self.edad} | Correo: {self.correo}"
    