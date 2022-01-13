from tkinter import *

raiz=Tk()

raiz.title("Rody")

miFrame=Frame(raiz, width=1200, height=800)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=1, column=1, padx=10,pady=10, columnspan=4)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1,column=0)

cuadroapellido=Entry(miFrame)
cuadroapellido.grid(row=2, column=1, padx=10,pady=10, columnspan=4)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0)

cuadrofecha=Entry(miFrame)
cuadrofecha.grid(row=3, column=1, padx=10,pady=10, columnspan=4)

fechaLabel=Label(miFrame, text="Fecha de nacimiento(DD/MM/AAAA):")
fechaLabel.grid(row=3,column=0)


#raiz.config(bg="black")
Label(miFrame, text="Hola Mundo, mi intención es ser un ayudante").grid(row=0, column=0, columnspan=4)

raiz.mainloop()
