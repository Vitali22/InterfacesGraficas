from tkinter import *

raiz = Tk()

mi_frame=Frame(raiz, width=1200, height=600)#Medidas del frame
mi_frame.pack()#Empaquetar 

cuadro_nombre=Entry(mi_frame)#Crear un cuadro de entrada
cuadro_nombre.grid(row=0,column=1, padx=10, pady=10)#fila 1 columna 0 separacion 10en X y 10 en Y
cuadro_nombre.config(fg="red", justify="right")#color rojo y estará justificado a la izquierda

cuadro_apellido=Entry(mi_frame)
cuadro_apellido.grid(row=1,column=1, padx=10, pady=10)

cuadro_direccion=Entry(mi_frame)
cuadro_direccion.grid(row=2,column=1, padx=10, pady=10)

nombre_label=Label(mi_frame, text="Nombre: ")
nombre_label.grid(row=0,column=0,sticky="e", padx=10, pady=10)#Stiky estará al este (Ver tabla de stiky en imágenes)

apellido_label=Label(mi_frame, text="Apellido: ")
apellido_label.grid(row=1,column=0, sticky="e",padx=10, pady=10)

direccion_label=Label(mi_frame, text="Direccion: ")
direccion_label.grid(row=2,column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()#Se pone al último para que esté refrescando la ventana