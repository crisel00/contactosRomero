class Contacto:
    def __init__(self, telefono, nombre, apellidos):
        self.telefono = telefono
        self.nombre = nombre
        self.apellidos = apellidos

    def print(self):
        print("Telefono: ", self.telefono," "
              "Nombre: ", self.nombre, " "
              "Apellidos: ",self.apellidos, " ")

    def getContacto(self):
        str = "Tlf: {}, Nombre: {} {}".format(self.telefono,self.nombre,self.apellidos)
        return str