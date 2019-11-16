from tkinter import *

raiz = Tk()

mi_frame=Frame(raiz)

mi_frame.pack()

pantalla=Entry(mi_frame)
pantalla.grid(row=1, colum=1, padx=10,pady=10, columspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")



#------------------------------fila 1------------------------


boton7=Button(mi_frame, text="7", width=3)
boton7.grid(row=2,colum=1)

boton8=Button(mi_frame, text="8", width=3)
boton8.grid(row=2,colum=1)

boton9=Button(mi_frame, text="9", width=3)
boton9.grid(row=2,colum=1)

boton_div=Button(mi_frame, text="/", width=3)
boton_div.grid(row=2,colum=4)