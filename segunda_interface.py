from tkinter import *

root=Tk()

mi_frame = Frame(root, width=500, height=400)#Tamaño del frame

mi_frame.pack()#empaquetamos mi_frame

mi_imagen=PhotoImage(file="mouse.gif")

Label(mi_frame, image=mi_imagen).place(x=100,y=100)

#mi_lable = Label(mi_frame, text="Hola Alumnos de Python",fg="red",font=("Arial", 18)).place(x=100,y=100)#Creamos una etiqueta

root.mainloop()
