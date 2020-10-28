# -*- coding: utf-8 -*-
import funciones as f
import write as w
import read as r

from tkinter import *
from PIL import Image,ImageTk

raiz = Tk()

raiz.call('wm', 'iconphoto', raiz._w, PhotoImage(file='message.png'))
raiz.title("Esteganografía")
raiz.resizable(0,0)#La raiz siempre se adaptara al tamaño de lo que contiene

frame = Frame(raiz, width=500, height=700, bg="black")
frame.pack()

ruta = StringVar()
foto = StringVar()
de = StringVar()
user = StringVar()
password = StringVar()

def see():
	img = f.getRuta()+"/"+foto.get()+".png"
	mensaje = r.leer(img)
	mensaje = mensaje.split(',')
	de.set(mensaje[0])
	user.set(mensaje[1])
	password.set(mensaje[2])

def save():
	mensaje = de.get()+","+user.get()+","+password.get()
	#mensaje="Holi"
	img = f.getRuta()+"/"+foto.get()+".png"
	output = f.getRuta()+"/"+"n_"+foto.get()+".png"
	w.save(mensaje,img,output)

lRuta = Label(frame, textvariable=ruta, bg="white", font=("Arial", 10))
lRuta.place(x=25, y=90, width=400, height=25)


bSee = Button(frame, text="Ver contraseña", bg="blue", fg="white", bd=0, command=see)
bSee.place(x=25, y=45)
bSave = Button(frame, text="Guardar contraseña", bg="orange", fg="white", bd=0, command=save)
bSave.place(x=335, y=45)


gear = Image.open('gear.png')
gear = gear.resize((15, 15), Image.ANTIALIAS)
gear = ImageTk.PhotoImage(gear)
bConfiguracion = Button(frame, image=gear, bg="white", bd=0, width=20, height=20, command=f.setRuta)
bConfiguracion.place(x=448, y=90)


lFoto = Label(frame, text="Foto:", bg="black", font=("Arial", 10), fg="white")
lFoto.place(x=25, y=130, width=90)
eFoto = Entry(frame, textvariable=foto, font=("Arial", 10))
eFoto.place(x=135, y=130, width=335)


lDe = Label(frame, text="De:", bg="black", font=("Arial", 10), fg="white")
lDe.place(x=25, y=160, width=90)
eDe = Entry(frame, textvariable=de, font=("Arial", 10))
eDe.place(x=135, y=160, width=335)

lUsuario = Label(frame, text="Usuario:", bg="black", font=("Arial", 10), fg="white")
lUsuario.place(x=25, y=190, width=90)
eUsuario = Entry(frame, textvariable=user, font=("Arial", 10))
eUsuario.place(x=135, y=190, width=335)


lContraseña = Label(frame, text="Contraseña:", bg="black", font=("Arial", 10), fg="white")
lContraseña.place(x=25, y=220, width=90)
eContraseña = Entry(frame, textvariable=password, font=("Arial", 10))
eContraseña.place(x=135, y=220, width=335)


navegador = Frame(frame, width=450, height=300, bg="black")
navegador.place(x=25, y=250)

ruta.set(f.getRuta())
f.showFiles(f.getRuta(), navegador)

raiz.mainloop()