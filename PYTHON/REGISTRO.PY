from tkinter import *

import pandas as pd ()



#VENTANA GENERAL
ventana = Tk()
ventana.title("REGISTRO")
ventana.geometry("1400x800")
ventana.configure(background="black")

#ARRAY
nombres,apellidos,cedula,celular,correo,empresa = [],[],[],[],[],[]

def registrar():
    global nombres,apellidos,cedula,celular,correo,empresa
    
    nombres.append(e_nombre.get())
    apellidos.append(e_apellidos.get())
    cedula.append(e_cedula.get())
    celular.append(e_celular.get())
    correo.append(e_correo.get())
    empresa.append(empresa.get())
    
    e_nombre.delete(0,END)
    e_apellidos.delete(0,END)
    e_cedula.delete(0,END)
    e_celular.delete(0,END)
    e_correo.delete(0,END)
    e_empresa.delete(0,END)
    
def guardar():
    global nombres,apellidos,cedula,celular,correo,empresa
    datos = {"NOMBRES":e_nombre,"APELLIDOS":e_apellidos,"CEDULA":e_cedula,"CELULAR":e_celular,"CORREO":e_correo,"EMPRESA":e_empresa}
    nom_exel =str(nombre_archivo.get()+"xlsx")
    df=pd
    
    
    

#icono
icono=PhotoImage(file="Logo Moya 02-01.png").subsample(1,1)

#imagen
image=PhotoImage(file="Logo mOY-01.png").subsample(3,2)

##CUERPO DE LA VENTANA
titulo=Label(text="FORMULARIO DE REGISTRO",font=("cambria",20),bg="red",fg="white")

#ingresar datos

#NOMBRES
label_nombre = Label(ventana, text="NOMBRES",font=("cambria",20),bg="black",fg="white")
e_nombre = Entry(ventana,width=60)

#APELLIDOS
label_apellidos = Label(ventana, text="APELLIDOS",font=("cambria",20),bg="black",fg="white")
e_apellidos = Entry(ventana,width=60)

#CEDULA
label_cedula = Label(ventana, text="NUMERO DE CEDULA",font=("cambria",20),bg="black",fg="white")
e_cedula = Entry(ventana,width=60)

#CELULAR
label_celular = Label(ventana, text="NUMERO DE CELULAR",font=("cambria",20),bg="black",fg="white")
e_celular = Entry(ventana,width=60)

#CORREO ELECTRONICO
label_correo = Label(ventana, text="CORREO",font=("cambria",20),bg="black",fg="white")
e_correo = Entry(ventana,width=60)

#EMPRESA
label_empresa = Label(ventana, text="EMPRESA",font=("cambria",20),bg="black",fg="white")
e_empresa = Entry(ventana,width=60)

#BOTONES#

#Boton registro
boton_r=Button(text="REGISTAR",font=("cambria",20),bg="red",fg="white")

#Boton Buscar
boton_b=Button(text="BUSCAR",font=("cambria",20),bg="red",fg="white")

#Boton nuevo registro
boton_nd=Button(text="NUEVO REGISTRO",font=("cambria",20),bg="red",fg="white")


Label=Label(image=image)







Label.pack()
Label.place(x=490,y=10)


titulo.pack(pady=10)
titulo.place(x=510,y=150)

#entrada nombres
label_nombre.pack()
label_nombre.place(x=320,y=200)
e_nombre.pack(pady=10,ipady=10)
e_nombre.place(x=200,y=250)

#entrada apellidos
label_apellidos.pack()
label_apellidos.place(x=920,y=200)
e_apellidos.pack(pady=5,ipady=10)
e_apellidos.place(x=800,y=250)

#entrada cedula
label_cedula.pack()
label_cedula.place(x=260,y=300)
e_cedula.pack(pady=15,ipady=10)
e_cedula.place(x=200,y=350)

#entrada celular
label_celular.pack()
label_celular.place(x=860,y=300)
e_celular.pack(pady=10,ipady=10)
e_celular.place(x=800,y=350)


#entrada correo
label_correo.pack()
label_correo.place(x=330,y=400)
e_correo.pack(pady=10,ipady=10)
e_correo.place(x=200,y=450)

#entrada empresa
label_empresa.pack()
label_empresa.place(x=930,y=400)
e_empresa.pack(pady=10,ipady=10)
e_empresa.place(x=800,y=450)

boton_r.pack()
boton_r.place(x=300,y=500)

boton_b.pack()
boton_b.place(x=930,y=500)

boton_nd.pack()
boton_nd.place(x=300,y=580)

#icono de ventana 
ventana.iconphoto(True,icono)
ventana.mainloop()

