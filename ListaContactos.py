import pickle


class ListaContactos:

    contactos = []

    def __init__(self):
        try:
            listacontactos = open("fichero_contactos", "ab+")
            listacontactos.seek(0)

            self.contactos = pickle.load(listacontactos)
            print("Cargados {} contactos".format(len(self.contactos)))
        except:
            print("Fichero vacío")
        finally:
            listacontactos.close()
            del(listacontactos)

    def exportaContactos(self):
        listaContactos = open("fichero_contactos", "wb")
        pickle.dump(self.contactos, listaContactos)
        listaContactos.close()
        del (listaContactos)


    def altaContacto(self, p):
        self.contactos.append(p)
        self.exportaContactos()

    def bajaContacto(self, telefono):
        for Contacto in self.contactos:
            if(Contacto.telefono == int(telefono)):
                self.contactos.remove(Contacto)
                print("HOLA PAPA")
        self.exportaContactos()


    def mostrarContactos(self):
        for Contacto in self.contactos:
            Contacto.print()

    def getContactos(self):
        contactostxt = ""
        for Contacto in self.contactos:
            contactostxt = contactostxt + Contacto.getContacto() + "\n"
        return contactostxt