""" Autores: Gabriel Gerardo Pineda Riveiro  #22880
             Sergio Alejandro Orellana Colindres #221122
             Angela Rosana Garcia Donis #22869
             Alisson Anette López Barrientos #221011
    Fase #03
    Recursos: python 3.10
    Catedratico: Ludwing Cano
    Auxiliares: Daniela Villamar y José Perez
    ultima fecha de modificacion: 13/05/2022

"""
#Módulos:
from tkinter import *
from tkinter import messagebox
import csv

class v1(Tk):
    def __init__(self):
        Tk.__init__(self)
        #Configuracion
        self.geometry("800x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Menu Principal")
        #Textos de la pantalla
        Label(text="Iniciar sesión", fg="White", bg="blueviolet", font=("Times New Roman",28)).place(x=320,y=120)
        #Botones para las ventanas
        self.texto1 = StringVar()
        #self.texto1.set("Ingresar usuario")
        #self.texto1.set("gerax")
        self.texto2 = StringVar()
        #self.texto2.set("Ingresar Contraseña")
        #self.texto2.set("loloco123")
        self.c1 = Entry(width=30, textvariable=self.texto1)
        self.c1.place(x=325,y=200)
        self.c2 = Entry(width=30, textvariable=self.texto2)
        self.c2.place(x=325,y=240)
        Button(height=1, width=15 , bg="#deaaff", fg="#240046" ,text="Ingresar", command=lambda:self.iniciarSesion()).place(x=355,y=300)
        Label(text="-------------------------------------------------------", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=225,y=325)
        Label(text="Aún no tienes cuenta?\nInscribite aquí:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=325,y=350)
        Button(height=1, width=15 , bg="#deaaff", fg="#240046" , text="Registrarse", command=lambda:self.ventana2()).place(x=355,y=420)
        self.mainloop()

    def iniciarSesion(self):
        self.usuario = (self.c1.get())
        self.contra = (self.c2.get())
        datos = []
        with open("usuarios.csv", newline='') as ar:
            reader = csv.DictReader(ar)
            for row in reader:
                datos.append(dict(row))

        bandera = False
        for i in range(len(datos)):
            if datos[i]['usuario'] == self.usuario and datos[i]['contrasenia'] == self.contra:
                bandera = True

        if bandera:
            self.destroy()
            ventana2 = v2()
        else:
            messagebox.showerror("Error","Error: Contraseña o Usuario incorrectos")
        
class v2(Tk):
    def __init__(self):
        Tk.__init__(self)
        #Configuracion
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Pantalla principal")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿En qué nivel se encuentra?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=250,y=20)
        Button(height=2, width=50 ,text="Primaria", bg="#deaaff", fg="#240046", command=lambda:self.ventana3()).place(x=300,y=120)
        Button(height=2, width=50 ,text="Secundaria", bg="#deaaff", fg="#240046", command=lambda:self.ventana4()).place(x=300,y=190)
        Button(height=2, width=50 ,text="Bachillerato", bg="#deaaff", fg="#240046", command=lambda:self.ventana5()).place(x=300,y=260)
        Button(height=2, width=50 ,text="Universidad", bg="#deaaff", fg="#240046", command=lambda:self.ventana6()).place(x=300,y=330)
        Button(height=2, width=50 ,text="Tomar curso libre", bg="#deaaff", fg="#240046", command=lambda:self.ventana6()).place(x=300,y=400)
        self.mainloop()

    #regresar
    def regres(self):
        self.destroy()
        ventana = v1()

    def ventana3(self):
        self.destroy()
        ventana3 = Primaria()

    def ventana4(self):
        self.destroy()
        ventana4 = Secundaria()

    def ventana5(self):
        self.destroy()
        ventana5 = Bachillerato()

    def ventana6(self):
        self.destroy()
        ventana6 = UniCursos()
     

class Primaria(Tk):
    def __init__(self):
        Tk.__init__(self)
        #Configuracion
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Primaria")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.matem()).place(x=280,y=120)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Comunicación").place(x=280,y=190)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Ciencias").place(x=280,y=260)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046",text="Sociales").place(x=280,y=330)
        self.mainloop()

    #regreso
    def regres(self):
        self.destroy()
        ventana = v2()

    def matem(self):
        self.destroy()
        ventana = mate()

    

class Secundaria(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Secundaria")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Comunicación").place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Ciencias naturales").place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Sociales").place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Computación").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Inglés").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

class Bachillerato(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Bachillerato")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Comunicación").place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Quimica").place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Seminario").place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046",text="Computación").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

class UniCursos(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Universidad y Cursos varios")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Matematicas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Química").place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología").place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Física").place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Programación").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

class mate(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("matematicas")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Matemáticas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=290,y=20)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Operacion básicos",command=lambda:self.operaciones()).place(x=40,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Derivadas").place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Integrales").place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Geometría").place(x=40,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones líneales").place(x=520,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones cuadraticas").place(x=40,y=290)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

    def operaciones(self):
        self.destroy()
        ventana = opera()

class opera(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("matematicas")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Matemáticas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=280,y=20)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Sumas",command=lambda:self.suma()).place(x=40,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Restas").place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Multiplicacion").place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Divisiones").place(x=40,y=200)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

    def suma(self):
        self.destroy()
        ventana = sum()


class sum(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Sumas")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Sumas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
        Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="Consiste en la adicion de dos o mas elementos para\nLlegar a un resultado final donde todo se incluye.\nEl simbolo de la suma es el simbolo mas (+) y se\nintercala entre los elementos que se quiere sumar", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
        Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
        Label(text="4 + 5 = 9", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
        Label(text="300 + 200 = 500", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic()).place(x=370,y=390)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

    def ejercic(self):
        self.destroy()
        ventana = ejerc()

class ejerc(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Sumas")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Ejercicios de Suma", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Label(text="8 + 13            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
        Label(text="2 + 250           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
        Label(text="9 + 756           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
        Label(text="1590 + 258        =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
        Label(text="796 + 75          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        self.c1 = Entry(width=10)
        self.c1.place(x=340,y=80)
        self.c2 = Entry(width=10)
        self.c2.place(x=340,y=120)
        self.c3 = Entry(width=10)
        self.c3.place(x=340,y=180)
        self.c4 = Entry(width=10)
        self.c4.place(x=340,y=220)
        self.c5 = Entry(width=10)
        self.c5.place(x=340,y=280)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" , text="Verificar",command=lambda:self.ver()).place(x=340,y=390)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2()

    def ver(self):
        bandera = False
        try:
            r1 = int(self.c1.get())
            r2 = int(self.c2.get())
            r3 = int(self.c3.get())
            r4 = int(self.c4.get())
            r5 = int(self.c5.get())
            if r1 == 21:
                if r2 == 252:
                    if r3 == 765:
                        if r4 == 1848:
                            if r5 == 871:
                                bandera = True
        except:
            messagebox.showerror("Error", "Debe de ingresar números válidos")
        if bandera:
            messagebox.showinfo("Informacion","Obtuviste todo correcto")
        else:
            messagebox.showinfo("Informacion","Fallaste")

programa = v1()