from tkinter import *

raiz = Tk()

raiz.title("Titulo")#Poner titulo a las ventanas

#raiz.resizable(True,True)#Se pueda agrandar la pantalla

#raiz.iconbitmap("gato.ico") #poner un icono

#raiz.geometry("650x350") #poner una medida de ventana

raiz.config(bg="blue")#Cambiar el color de la raíz

mi_frame = Frame()#Creaar un frame

#mi_frame.pack(fill="x")#Responsivo respecto a X

#mi_frame.pack(side="right", anchor="n")#Empaquetar hacia la derecha y abajo

mi_frame.pack(fill="both", expand="True")#Responsivo respecto a Y y se espande

mi_frame.config(bg="red")# cambiamos el color de mi frame a rojo

mi_frame.config(width="650", height="350")#Poner alto y ancho a un frame

mi_frame.config(relief="groove")#Poner un relieve


mi_frame.config(bd=35)#Poner borde

mi_frame.config(cursor="pirate")#cambiar cursor

raiz.mainloop()#Siempre debe ir al último del código
