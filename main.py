from tkinter import *
from tkinter import scrolledtext

from Contacto import Contacto
from ListaContactos import ListaContactos

window = Tk()
contactos = ListaContactos()

window.title("Contactos Romero")
window.geometry('400x300')
window.configure(background="light gray")

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0, row=0, columnspan=3)

def actualizaTexto():
    txt.delete(1.0, END)
    str = contactos.getContactos()
    txt.insert(INSERT, str)

actualizaTexto()

lbl_1 = Label(window, text="Telefono")
lbl_1.grid(column=0, row=1)

lbl_2 = Label(window, text="Nombre")
lbl_2.grid(column=1, row=1)

lbl_3 = Label(window, text="Apellidos")
lbl_3.grid(column=2, row=1)

input_tlf = Entry(window,width=10)
input_tlf.grid(column=0, row=2)

input_nombre = Entry(window, width=10)
input_nombre.grid(column=1, row=2)

input_apellido = Entry(window, width=10)
input_apellido.grid(column=2, row=2)

def anadirClicked():
    telefono = int(input_tlf.get())
    nombre = input_nombre.get()
    apellido = input_apellido.get()

    ct = Contacto(telefono,nombre,apellido)
    ct.print()
    contactos.altaContacto(ct)
    actualizaTexto()



boton_alta = Button(window, text="Añadir", command=anadirClicked)
boton_alta.grid(column=0, row=3)

def borrarClicked():
    telefono = int(input_tlf.get())
    contactos.bajaContacto(telefono)
    actualizaTexto()

boton_baja = Button(window, text="Baja", command=borrarClicked)
boton_baja.grid(column=1, row=3)

def actualizarClicked():
    telefono = int(input_tlf.get())
    nombre = input_nombre.get()
    apellido = input_apellido.get()

    ct = Contacto(telefono, nombre, apellido)

    contactos.actualizaContacto(ct)
    actualizaTexto()

boton_baja = Button(window, text="Actualizar", command=actualizarClicked)
boton_baja.grid(column=2, row=3)

window.mainloop()