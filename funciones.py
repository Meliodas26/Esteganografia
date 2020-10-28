from tkinter import *
import json
from tkinter import filedialog as fd
import os
from tkinter import messagebox
from os import listdir
from PIL import Image

fotos = list()

def setRuta():
	directorio = fd.askdirectory()
	if directorio!="":
		os.chdir(directorio)
	ruta = {"ruta": os.getcwd()}
	with open('/home/aldo/Documents/7mo/ProcesamientoImagenes/Proyecto/configuracion.json', 'w') as file:
		json.dump(ruta, file)
	messagebox.showinfo(message="Vuelva a correr el programa para reflejar los cambios", title="Mensaje")

def getRuta():
	with open('/home/aldo/Documents/7mo/ProcesamientoImagenes/Proyecto/configuracion.json') as file:
		ruta = json.load(file)
	ruta = ruta["ruta"]
	return ruta

def showFiles(ruta, navegador):
	files = listdir(ruta)
	fotos = list()
	lFoto = Label(navegador, text="Fotos:", bg="black", fg="white", height=3)
	lFoto.place(x=0, y=0)
	y=30
	for file in files:
		if file.find(".png") >= 0:
			lFoto = Label(navegador, text=file.replace(".png", ""), bg="black", fg="white", height=3)
			lFoto.place(x=0, y=y)
			y+=30
