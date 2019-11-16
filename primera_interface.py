from tkinter import *

raiz = Tk()

raiz.title("Titulo")#Poner titulo a las ventanas

raiz.resizable(True,True)#Se pueda agrandar la pantalla

#raiz.iconbitmap("gato.ico") #poner un icono

#raiz.geometry("650x350") #poner una medida de ventana

raiz.config(bg="blue")

raiz.mainloop()#Siempre debe ir al último del código
