""" Autores: Gabriel Gerardo Pineda Riveiro  #22880
             Sergio Alejandro Orellana Colindres #221122
             Angela Rosana Garcia Donis #22869
             Alisson Anette López Barrientos #221011
    Fase #04
    Recursos: python 3.10
    Catedratico: Ludwing Cano
    Auxiliares: Daniela Villamar y José Perez
    ultima fecha de modificacion: 27/05/2022

"""
#Módulos:
from tkinter import *
from tkinter import messagebox
import csv
import Registrar as reg
import AgregarInformacion as ag
import graficas as gr

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
        Button(height=1, width=15 , bg="#deaaff", fg="#240046" , text="Registrarse", command=lambda:self.registrar()).place(x=355,y=420)
        self.mainloop()


    def registrar(self):
        self.destroy()
        ventana2 = Registro()

    def iniciarSesion(self):
        self.usuario = (self.c1.get()).lower()
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
            ventana2 = v2(self.usuario)
        else:
            messagebox.showerror("Error","Error: Contraseña o Usuario incorrectos")


class Registro(Tk):
    def __init__(self):
        Tk.__init__(self)
        #Configuracion
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Pantalla principal")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        Label(text="Nuevo Usuario", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=250,y=20)
        Label(text="Ingrese nombre de usuario: ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=10,y=150)
        self.c1 = Entry(width=40) 
        self.c1.place(x=250,y=155)
        Label(text="Ingrese Contraseña: ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=10,y=220)
        self.c2 = Entry(width=40)
        self.c2.place(x=250,y=225)
        Button(height=2, width=50 ,text="Ingresar Datos", bg="#deaaff", fg="#240046", command=lambda:self.ingresarDatos()).place(x=300,y=300)
        #Pantalla 
        self.mainloop()

    def ingresarDatos(self):
        nombre = self.c1.get()
        contra = self.c2.get()
        confirmacion = reg.ingrearRegistro(nombre,contra)
        if confirmacion:
            self.destroy()
            ventana = v1()

    #regresar
    def regres(self):
        self.destroy()
        ventana = v1()


class v2(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        #Configuracion
        self.usuario = usuario
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
        ventana3 = Primaria(self.usuario)

    def ventana4(self):
        self.destroy()
        ventana4 = Secundaria(self.usuario)

    def ventana5(self):
        self.destroy()
        ventana5 = Bachillerato(self.usuario)

    def ventana6(self):
        self.destroy()
        ventana6 = UniCursos(self.usuario)
     

class Primaria(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        #Configuracion
        self.geometry("900x500")
        self.usuario = usuario
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Primaria")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.matem()).place(x=280,y=120)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Comunicación", command=lambda:self.comu()).place(x=280,y=190)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Ciencias", command=lambda:self.cs()).place(x=280,y=260)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046",text="Sociales", command=lambda:self.ss()).place(x=280,y=330)
        self.mainloop()

    #regreso
    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def matem(self):
        self.destroy()
        ventana = mate(self.usuario)
        
    def comu(self):
        self.destroy()
        ventana = comunicacion(self.usuario)

    def cs(self):
        self.destroy()
        ventana = ciencias(self.usuario)

    def ss(self):
        self.destroy()
        ventana = sociales(self.usuario)
   

class Secundaria(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Secundaria")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.matem()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Comunicación", command=lambda:self.comu()).place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Ciencias naturales", command=lambda:self.cs()).place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Sociales", command=lambda:self.ss()).place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Computación", command=lambda:self.c()).place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Inglés", command=lambda:self.i()).place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)
        
    def matem(self):
        self.destroy()
        ventana = mate(self.usuario)

    def comu(self):
        self.destroy()
        ventana = comunicacion(self.usuario)

    def cs(self):
        self.destroy()
        ventana = ciencias(self.usuario)

    def ss(self):
        self.destroy()
        ventana = sociales(self.usuario)

    def c(self):
        self.destroy()
        ventana = computacion(self.usuario)

    def i(self):
        self.destroy()
        ventana = ingles(self.usuario)
        
class Bachillerato(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Bachillerato")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.matem()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Comunicación", command=lambda:self.comu()).place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Quimica", command=lambda:self.qui()).place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Seminario",command=lambda:self.semi()).place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046",text="Computación", command=lambda:self.c()).place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología",command=lambda:self.b()).place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def matem(self):
        self.destroy()
        ventana = mate(self.usuario)

    def comu(self):
        self.destroy()
        ventana = comunicacion(self.usuario)

    def c(self):
        self.destroy()
        ventana = computacion(self.usuario)

    def b(self):
        self.destroy()
        ventana = biologia(self.usuario)

    def qui(self):
        self.destroy()
        ventana = quimica(self.usuario)

    def semi(self):
        self.destroy()
        ventana = seminario(self.usuario)

class UniCursos(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Universidad y Cursos varios")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="¿Qué curso desea tomar?", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=260,y=20)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Matematicas",command=lambda:self.matem()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Química", command=lambda:self.qui()).place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología",command=lambda:self.b()).place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Física",command=lambda:self.fi()).place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Cálculo",command=lambda:self.ca()).place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Programación",command=lambda:self.pro()).place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def matem(self):
        self.destroy()
        ventana = mate(self.usuario)

    def b(self):
        self.destroy()
        ventana = biologia(self.usuario)

    def qui(self):
        self.destroy()
        ventana = quimica(self.usuario)

    def fi(self):
        self.destroy()
        ventana = fisica(self.usuario)

    def ca(self):
        self.destroy()
        ventana = calculo(self.usuario)

    def pro(self):
        self.destroy()
        ventana = progra(self.usuario)


#----------------------------------------------------------------------------------

class mate(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("matematicas")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Matemáticas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=290,y=20)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Operacion básicos",command=lambda:self.operaciones()).place(x=40,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Derivadas",command=lambda:self.otrasOperaciones('derivada')).place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Integrales").place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Geometría").place(x=40,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones líneales").place(x=520,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones cuadraticas").place(x=40,y=290)
        if self.usuario == 'admin':
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Estadisticas matematicas",command=lambda:self.esta()).place(x=350,y=400)
        self.mainloop()

    def otrasOperaciones(self,accion):
        self.destroy()
        vantana = pantallaEjemplos(self.usuario, accion)

    def esta(self):
        self.destroy()
        ventana = estadisticas(self.usuario)

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def operaciones(self):
        self.destroy()
        ventana = opera(self.usuario)

#---------------------------------------------------------------- 

class estadisticas(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Estadisticas")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Estadisticas Matematicas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=290,y=20)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Operaciones básicas",command=lambda:self.estadistica('operaciones_basicas')).place(x=40,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Derivadas",command=lambda:self.estadistica('derivada')).place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Integrales",command=lambda:self.estadistica('integral')).place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Geometría").place(x=40,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones líneales").place(x=520,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones cuadraticas").place(x=40,y=290)
        self.mainloop()

    def estadistica(self,accion):
        gr.estadisticasMate(accion)

    def regres(self):
        self.destroy()
        ventana = mate(self.usuario)

#------------------------------------------------

class opera(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("matematicas")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Matemáticas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=280,y=20)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Sumas",command=lambda:self.operacionBasica('suma')).place(x=40,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Restas",command=lambda:self.operacionBasica('resta')).place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Multiplicacion",command=lambda:self.operacionBasica('multiplicacion')).place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Divisiones",command=lambda:self.operacionBasica('division')).place(x=40,y=200)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def operacionBasica(self,accion):
        self.destroy()
        ventana = pantallaEjemplos(self.usuario,accion)


class pantallaEjemplos(Tk):
    def __init__(self,usuario,accion):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        if accion == 'suma':
        #Pantalla 
            self.title("Sumas")
            Label(text="Sumas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="Consiste en la adicion de dos o mas elementos para\nLlegar a un resultado final donde todo se incluye.\nEl simbolo de la suma es el simbolo mas (+) y se\nintercala entre los elementos que se quiere sumar", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="4 + 5 = 9", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="300 + 200 = 500", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('suma')).place(x=370,y=390)
        if accion == 'resta':
            self.title("Resta")
            Label(text="Restas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="quitar una cantidad (el sustraendo) de otra (el minuendo)\npara averiguar la diferencia entre las dos\nse representa con el signo -.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="800 - 400 = 400", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="300 - 500 = -200", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('resta')).place(x=370,y=390)
        if accion == 'multiplicacion':
            self.title("multiplicacion")
            Label(text="Multiplicacion", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="Operación aritmética que consiste en calcular el resultado (producto)\n de sumar un mismo número (multiplicando) tantas veces como\n indica otro número (multiplicador)\n se representa con los signos · o ×.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="5 * 5 = 25", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="7 * 30 = 210", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('multiplicacion')).place(x=370,y=390)
        if accion == 'division':
            self.title("division")
            Label(text="Divison", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="Operacion aritmetica que consiste en la separación o partición\n de un todo en partes. Usual mente se representa por '/'", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="5 / 5 = 1", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="80 / 8 = 10", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('division')).place(x=370,y=390)
        if accion == 'derivada':
            self.title("derivada")
            Label(text="Derivada", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="En una función, límite hacia el cual tiende la razón entre\n el incremento de la función y el correspondiente a la variable cuando\n el incremento tiende a cero.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="'f(x) = 5'  f'(x) = 0", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="'f(x) = x^2' f'(x) = 2x", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('derivada')).place(x=370,y=390)
        if accion == 'integral':
            self.title("integral")
            Label(text="integrales", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="En una función, límite hacia el cual tiende la razón entre\n el incremento de la función y el correspondiente a la variable cuando\n el incremento tiende a cero.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="'∫ (x+2)^3 dx'  = 1/4(x+2)^4+C", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="'∫ sin^4(x) cos(x) dx' = 1/5sin^5(x)+C", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('derivada')).place(x=370,y=390)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def ejercic(self,accion):
        self.destroy()
        ventana = ejercOpera(self.usuario,accion)

class ejercOpera(Tk):
    def __init__(self,usuario,accion):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.columna = "operaciones_basicas"
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla
        if accion == 'suma':
            self.title("Sumas")
            Label(text="Ejercicios de Suma", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="8 + 13            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="2 + 250           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="9 + 756           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="1590 + 258        =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="796 + 75          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        if accion == 'resta':
            self.title("Resta")
            Label(text="Ejercicios de Resta", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="25 - 13            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="1000 - 2           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="9 - 756           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="5 - 3        =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="78 - 75          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        if accion == 'multiplicacion':
            self.title("multiplicacion")
            Label(text="Ejercicios de multiplicacion", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="25 * 5            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="63 * 4           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="1000 * 1           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="1000 * 10        =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="50 * 30          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        if accion == 'division':
            self.title("division")
            Label(text="Ejercicios de division", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="25 / 5            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="60 /  4           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="100 / 25           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="900 / 9        =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="555 / 37          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        if accion == 'derivada':
            self.title("derivada")
            Label(text="Ejercicios de derivada", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="'f(x) = x^5'            f'(x)=", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="'f(x) = e^x'             f'(x)=", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="'f(x) = lnx'           f'(x)=", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="'f(x) = sin(x)'        f'(x)=", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="'f(x) = 5x^2'          f'(x)=", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
        if accion == 'integral':
            self.title("integral")
            Label(text="Ejercicios de derivada", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
            Label(text="'∫ tan(x) dx'            =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=80)
            Label(text="'∫ (x+1)/x dx'           =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=120)
            Label(text="'∫ (5^x) dx'              =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=180)
            Label(text="'∫ (3-sin(x) dx'          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=220)
            Label(text="'∫ tan^2(x) dx'          =", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=150,y=280)
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

        Button(height=2, width=30 , bg="#deaaff", fg="#240046" , text="Verificar",command=lambda:self.ver(accion)).place(x=340,y=390)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def ver(self,accion):
        bandera = False
        try:
            puntos = 0
            if accion == 'suma' or accion == 'resta' or accion == 'multiplicacion' or accion == 'division':
                r1 = int(self.c1.get())
                r2 = int(self.c2.get())
                r3 = int(self.c3.get())
                r4 = int(self.c4.get())
                r5 = int(self.c5.get())
            else:
                r1 = self.c1.get()
                r2 = self.c2.get()
                r3 = self.c3.get()
                r4 = self.c4.get()
                r5 = self.c5.get()
            if accion == 'suma':
                if r1 == 21:
                    puntos+=1
                if r2 == 252:
                    puntos+=1
                if r3 == 765:
                    puntos+=1
                if r4 == 1848:
                    puntos+=1
                if r5 == 871:
                    puntos+=1
            if accion == 'resta':
                if r1 == 12:
                    puntos+=1
                if r2 == 998:
                    puntos+=1
                if r3 == -747:
                    puntos+=1
                if r4 == 2:
                    puntos+=1
                if r5 == 3:
                    puntos+=1
            if accion == 'multiplicacion':
                if r1 == 125:
                    puntos+=1
                if r2 == 252:
                    puntos+=1
                if r3 == 1000:
                    puntos+=1
                if r4 == 10000:
                    puntos+=1
                if r5 == 1500:
                    puntos+=1
            if accion == 'division':
                if r1 == 5:
                    puntos+=1
                if r2 == 15:
                    puntos+=1
                if r3 == 4:
                    puntos+=1
                if r4 == 100:
                    puntos+=1
                if r5 == 15:
                    puntos+=1
            if accion == 'derivada':
                self.columna = "derivada"
                if r1 == '5x':
                    puntos+=1
                if r2 == 'e^x':
                    puntos+=1
                if r3 == '1/x':
                    puntos+=1
                if r4 == 'cos(x)':
                    puntos+=1
                if r5 == '10x':
                    puntos+=1
            if accion == 'integral':
                self.columna = "integral"
                if r1 == '-ln(cos(x))+c':
                    puntos+=1
                if r2 == 'x+ln(x)+c':
                    puntos+=1
                if r3 == '5^x/ln(5)':
                    puntos+=1
                if r4 == '3x+cos(x)':
                    puntos+=1
                if r5 == 'tan(x)-x+c':
                    puntos+=1
            ag.Agregar(self.usuario,self.columna,puntos)
        except:
            messagebox.showerror("Error", "Debe de ingresar números válidos")
        if puntos == 5:
            messagebox.showinfo("Informacion","Obtuviste todo correcto")
        else:
            messagebox.showinfo("Informacion","Obtuviste "+str(puntos)+" buenas en este ejercicio")

        self.regresar()

    def regresar(self):
        self.destroy()
        ventana = mate(self.usuario)


#----------------------------------------------------------------------------------

#comunicacion

class def_comunicacion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Definición de la comunicación")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Definición de la comunicación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=240,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="La comunicación es un proceso social que consiste en el intercambio \n de información entre un organismo A y un organismo B.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=220,y=120)
        Label(text="Tipos de comunicación:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=190)
        Label(text="- Según el código", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=250)
        Label(text="- Según el espacio", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
        Label(text="- Por la presencia o ausencia de diálogo", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
        Label(text="- Por el tipo de receptor", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=400)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class procesos_de_la_comunicacion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("El proceso de la comunicación de comunicación")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="El proceso de la comunicación de comunicación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=10,y=20)
        Label(text="Emisor:ㅤㅤㅤ Es el elemento que ordena y envía el mensaje. Éste se caracteriza por CODIFICAR.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=120)
        Label(text="Mensaje:ㅤㅤ  Es el contenido de la información que queremos transmitir.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=160)
        Label(text="Receptor: ㅤㅤ Es el que recibe e interpreta el mensaje, es decir, decodifica.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=200)
        Label(text="Código:ㅤㅤㅤ Cualquier sistema de signos convencionales que usan el emisor y receptor.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=240)
        Label(text="Canal:ㅤㅤㅤㅤEs el medio físico a través del cual se difunde el mensaje.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=280)
        Label(text="Referente:ㅤㅤEs el objeto o fenómeno de la realidad a lo que se hace referencia en la comunicación.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=320)
        Label(text="Contexto: ㅤㅤ Es la situación espacio-tiempo que rodea el acto comunicativo.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=360)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class clases_y_estructura_sujeto(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Clases y estructuras del sujeto")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Clases y estructuras del sujeto", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=160,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=100)
        Label(text="Es una parte de la Lingüística que se encarga del estudiar de los elementos o sonidos “mentales”\n que forman parte del plano del significante en el signo lingüístico. Su unidad de estudio es el FONEMA. \nEs necesario anotar que los hablantes-oyentes de una lengua van a percibir\n a los fonemas en la medida que reconozcan que pertenecen a una unidad\n mayor que se denomina palabra.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=10,y=140)
        
        Label(text="Ejemplos: ", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=250)
        Label(text="Cuando uno habla no hay espacios entre las palabras que va pronunciando,\n más o menos sería algo como lo siguiente: \n“lavasaberalejandro”\nEste enunciado puede ser interpretado de 2 formas distintas, \nsegún se reconozcan los fonemas como constituyente de una determinada palabra\n de la lengua española, veamos:", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=100,y=280)        
        Label(text="Primera interpretación: Lo vas a ver a Alejandro.\nSegunda interpretación: Lo va a saber Alejandro. ", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=250,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class fonologia(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Fonología")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Fonología", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=10,y=20)
        Label(text="El sujeto: Es la persona, animal o cosa de quien se habla en la oración o que realiza una acción.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=100)
        Label(text="Clases de sujeto:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=140)
        Label(text="1. Por la presencia o ausencia del sujeto:", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=180)
        Label(text="Sujeto Expreso Sujeto Tácito", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=70,y=200)
        Label(text="2. Por la cantidad de núcleos:", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=240)
        Label(text="Sujeto Simple o Sujeto Compuesto", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=70,y=260)
        Label(text="Núcleo: Es la palabra más importantes del sujeto. Suele ser un sustantivo o pronombre.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=300)
        Label(text="Complementos: modificadores directos o indirectos, aposición", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=320)
        Label(text="Ejemplos: ", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=50,y=350)
        Label(text="- Mi hermano Miguel se ha escondido.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=70,y=380)
        Label(text="- Tu abuelo y tu padre son héroes de guerra.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=70,y=410)
        Label(text="- Yo sigo comiendo pastel.", fg="White", bg="blueviolet", font=("Times New Roman",14)).place(x=70,y=440)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class comunicacion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Comunicación")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Comunicación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=290,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Definición de la comunicación",command=lambda:self.def_c()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Procesos de la comunicación",command=lambda:self.procesos()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Clases y estructura del sujeto",command=lambda:self.sujeto()).place(x=400,y=280)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="La fonología",command=lambda:self.fon()).place(x=120,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def def_c(self):
        self.destroy()
        ventana = def_comunicacion(self.usuario)

    def procesos(self):
        self.destroy()
        ventana = procesos_de_la_comunicacion(self.usuario)

    def sujeto(self):
        self.destroy()
        ventana = clases_y_estructura_sujeto(self.usuario)

    def fon(self):
        self.destroy()
        ventana = fonologia(self.usuario)


#ciencias

class materia(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Materia y sus estados de agregación")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Materia y sus estados de agregación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=120,y=20)
        Label(text="La materia se encuentra en tres estados: sólido, líquido y gaseoso", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=140,y=90)
        Label(text="Los sólidos: Tienen forma y volumen constantes. Se caracterizan por la rigidez y \nregularidad de sus estructuras. Sus partículas se encuentran de una manera compacta \nen la que no se permite un gran movimiento entre ellas, siendo esta la razón de la \nestructura", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=130)
        Label(text="Los líquidos: No tienen una forma definida pero sí volumen. El cambio de forma y el \npresentar unas propiedades muy específicas son características de los líquidos. Sus \npartículas están en movimiento casi constante, pero siempre de una manera \nordenada, de esta manera el material pierde rigidez pero adquiere una forma más\n fluida.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=230)
        Label(text="Los gases: No tienen forma ni volumen fijos. Los gases cambian el volumen que ocupan\n de acuerdo a la temperatura a la que sean sometidos. Sus moléculas tienen una gran\n cantidad de energía, lo que aumenta la cantidad de choques entre estas partículas y\n causa una pérdida de forma completa.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=350)     
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class sentidos(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x600")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Los sentidos")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Los sentidos", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=360,y=20)
        Label(text="Concepto: Los seres humanos tenemos cinco sentidos, los cuales nos permiten \npercibir todo lo que nos rodea, estos cinco sentidos son: ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=140,y=90)
        Label(text="La vista:  con este sentido es posible las imágenes son recibidas por el ojo \n Tus ojos captan grandes cantidades de información sobre lo que está a tu alrededor,\nenviando señales al cerebro para que pueda ver formas, colores, texturas y movimientos", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=140)
        Label(text="La audición: La audición es la percepción de las ondas sonoras y que primero pasan por la oreja \npara luego llegar a los conductos auditivos externos y chocar con el tímpano, que vibra con ellas. \nImplica procesos fisiológicos, por la estimulación de los órganos de la audición, y también \nprocesos psicológicos, por el acto consciente de percibir sonidos.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=220)
        Label(text="El tacto: Este sentirdo es el encargado de  percibir la temperatura, presión y dolor  \ndel cuerpo de cada ser humano. Además de ello, permite que la persona se relacione con su entorno\n de manera precisa y genera señales internas que obedecen las órdenes que dael cerebro, \nlo que crea un ciclo de retroalimentación que facilita la comunicación entre impulsos y respuestas.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=320)     
        Label(text="El gusto: Este permite determinar el gusto y el sabor de los alimentos que ingerimos.\n Para poder determinar el gusto por los alimentos tenemos las papilas (aspecto rugoso en la lengua), \ndonde se ubican los llamados botones gustativos que permiten identificar los sabores. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=420)
        Label(text="El olfato:  Por medio del sentido del olfato percibimos los olores que nos ayudan a identificar los \ncuerpos, objetos y sustancias a nuestro alrededor. La nariz es el órgano por el cual penetran todos \nlos olores que sentimos. Las moléculas de olor entran por las fosas nasales. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=500)            
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class cuerpo(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.geometry("900x550")
        self.usuario = usuario
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("El cuerpo humano")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="El cuerpo humano", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="Si hablamos de la estructura podemos afirmar que el cuerpo humano se divide en:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=140,y=90)
        Label(text="La cabeza: es la parte superior del cuerpo, donde se encuentran algunos órganos de los sentidos y \nel cerebro, es la parte anterior del cuerpo que contiene varios órganos sensoriales como órganos de \nvisión, audición, olfato y gusto. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=140)
        Label(text="Torso: es una de las partes fundamentales del cuerpo humano junto a la cabeza y miembros. En su parte\n superior se encuentra unido a la cabeza, y de sus lados están situados los miembros superiores,\ny los miembros inferiores o pelvianos abajo. Dentro del torso humano se alberga una parte \nfundamental en el movimiento que es la columna vertebral y en el interior también se \nencuentran los principales órganos de los aparatos o sistemas presentes del organismo.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=220)
        Label(text="El tacto: Este sentirdo es el encargado de  percibir la temperatura, presión y dolor  \ndel cuerpo de cada ser humano. Además de ello, permite que la persona se relacione con su entorno\n de manera precisa y genera señales internas que obedecen las órdenes que dael cerebro, \nlo que crea un ciclo de retroalimentación que facilita la comunicación entre impulsos y respuestas.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=340)     
        Label(text="Extremidades: hablando de las extremidades del cuerpo humano estas, se dividen en dos \nclases acorde a la ubicación en el mismo cuerpo, y las extremidades superiores que se \nconocen como brazos, y las extremidades inferiores como las piernas.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=440)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class sentidos(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x600")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Los sentidos")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Los sentidos", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=360,y=20)
        Label(text="Concepto: Los seres humanos tenemos cinco sentidos, los cuales nos permiten \npercibir todo lo que nos rodea, estos cinco sentidos son: ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=140,y=90)
        Label(text="La vista:  con este sentido es posible las imágenes son recibidas por el ojo \n Tus ojos captan grandes cantidades de información sobre lo que está a tu alrededor,\nenviando señales al cerebro para que pueda ver formas, colores, texturas y movimientos", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=140)
        Label(text="La audición: La audición es la percepción de las ondas sonoras y que primero pasan por la oreja \npara luego llegar a los conductos auditivos externos y chocar con el tímpano, que vibra con ellas. \nImplica procesos fisiológicos, por la estimulación de los órganos de la audición, y también \nprocesos psicológicos, por el acto consciente de percibir sonidos.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=220)
        Label(text="El tacto: Este sentirdo es el encargado de  percibir la temperatura, presión y dolor  \ndel cuerpo de cada ser humano. Además de ello, permite que la persona se relacione con su entorno\n de manera precisa y genera señales internas que obedecen las órdenes que dael cerebro, \nlo que crea un ciclo de retroalimentación que facilita la comunicación entre impulsos y respuestas.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=320)     
        Label(text="El gusto: Este permite determinar el gusto y el sabor de los alimentos que ingerimos.\n Para poder determinar el gusto por los alimentos tenemos las papilas (aspecto rugoso en la lengua), \ndonde se ubican los llamados botones gustativos que permiten identificar los sabores. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=420)
        Label(text="El olfato:  Por medio del sentido del olfato percibimos los olores que nos ayudan a identificar los \ncuerpos, objetos y sustancias a nuestro alrededor. La nariz es el órgano por el cual penetran todos \nlos olores que sentimos. Las moléculas de olor entran por las fosas nasales. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=500)            
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class diversidad(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("La diversidad")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="La diversidad", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=140,y=90)
        Label(text="La biodiversidad o diversidad biológica es la variedad de la vida. Este reciente concepto\n incluye varios niveles de la organización biológica. Abarca a la diversidad de especies de\n plantas, animales, hongos y microorganismos que viven en un espacio determinado, a su\n variabilidad genética, a los ecosistemas de los cuales forman parte estas especies y a los paisajes \no regiones en donde se ubican los ecosistemas. También incluye los procesos ecológicos y evolutivos \nque se dan a nivel de genes, especies, ecosistemas y paisajes (Biodiversidad, 2022)", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=70,y=140)
        Label(text="La composición es la identidad y variedad de los elementos (incluye qué especies están\n presentes y cuántas hay), la estructura es la organización física o el patrón del sistema\n (incluye abundancia relativa de las especies, abundancia relativa de los ecosistemas, grado \nde conectividad, etc.) y la función son los procesos ecológicos y evolutivos (incluye a la depredación, \ncompetencia, parasitismo, dispersión, polinización, simbiosis, ciclo de nutrientes,\n perturbaciones naturales, etc.) (Biodiversidad, 2022). ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=70,y=290)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class ciencias(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.geometry("900x500")
        self.usuario = usuario
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Ciencias")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Ciencias", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Materia y sus estados de agregación",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Los sentidos",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Cuerpo humano",command=lambda:self.c()).place(x=400,y=280)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Diversidad",command=lambda:self.d()).place(x=120,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = materia(self.usuario)

    def b(self):
        self.destroy()
        ventana = sentidos(self.usuario)

    def c(self):
        self.destroy()
        ventana = cuerpo(self.usuario)

    def d(self):
        self.destroy()
        ventana = diversidad(self.usuario)

#sociales

class pre(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("La prehistoria")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="La prehistoria", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=120,y=20)
        Label(text="La Prehistoria es el período de mayor duración del pasado de la humanidad, ya que se inició desde el \naparecimiento del ser humano, hace aproximadamente 200 mil años, y terminó cerca del año 3,500 \na.C. En sus inicios, el ser humano vivía únicamente de lo que obtenía directamente de la naturaleza, \ndependía de las posibilidades de su medio natural. Eso hacía que los grupos humanos vivieran de \nmanera temporal en algunos lugares; por ejemplo en espacios donde abundaban frutas, semillas o \nanimales de caza. Cuando estos alimentos escaseaban, los grupos humanos tenían que desplazarse, \npor lo que se dice que eran nómadas; es decir, no tenían residencia fija.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        Label(text="\nPara comprender su estudio, la Prehistoria se ha dividido en tres períodos que son:\n\n• Paleolítico (200, 000 a.C. a 10,000 a.C.) \n\n• Neolítico (10,000 a.C. a 5,000 a.C.) \n\n• Edad de los Metales (5,000 a.C. a 3,500 a.C.)", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=250)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class diversidad_et(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Diversidad étnica")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Diversidad étnica", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="Se le llama grupo étnico a un grupo cuyos integrantes comparten una misma identidad. Esto significa \nque los integrantes del grupo comparten una misma historia, costumbres, tradiciones, idioma, formas \nde comportamiento ante situaciones como el nacimiento, la vida, el matrimonio y la muerte, por citar \nalgunos casos. Aunque existen otros elementos que contribuyen a aumentar al sentido de pertenencia \no de identidad.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        Label(text="Debido a que el idioma es un elemento de mucho peso en la identidad étnica, muchas veces al \nhablar de grupo étnico, también se indica que se trata de grupos etnolingüísticos. La diversidad es \ntan grande en el mundo, que actualmente se hablan más de 6,500 idiomas en el planeta. Solo en \nGuatemala se hablan 25 idiomas, 22 son de origen maya, el xinka, el garífuna y el español.\n", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=250)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class historia(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Historia de la democracia")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Historia de la democracia", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=220,y=20)
        Label(text="Los atenienses del siglo V a.C. consideraban la democracia como el gobierno del pueblo; es decir, \ncomo la forma de gobierno en donde tenían participación todos los ciudadanos. Los antiguos\natenienses entendían como ciudadanos a los hombres libres nacidos en Atenas, mayores de \nedad; por lo que estaban excluidos de la democracia los esclavos, las mujeres y los extranjeros. Los \natenienses y otros pueblos griegos tuvieron la oportunidad de practicar la democracia participativa,\n que es aquella en la que todos los ciudadanos tienen la posibilidad real de acceder a los cargos \npúblicos y de votar en igualdad de condiciones. Lo más importante de la democracia participativa es \nque los ciudadanos, reunidos en asamblea, son quienes toman las decisiones que benefician al grupo.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        Label(text="\nEn la actualidad, ejercer la democracia participativa, aunque es posible en el poder público, es \nmuy difícil. Lo que existe es la democracia representativa; por ejemplo, cuando el Presidente de la \nRepública representa la unidad de la nación y los diputados representan a determinada cantidad de \nciudadanos. \n\nEn lugares más pequeños, como en las comunidades y centros educativos, sí es posible ejercer \nplenamente la democracia participativa. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=250)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class continentes(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Historia de la democracia")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Historia de la democracia", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=220,y=20)
        Label(text="Según el Diccionario de la Real Academia Española de la Lengua (DRAE),\n un continente es cada una de las grandes extensiones de tierra separadas por los océanos. \nEsas grandes masas terrestres que se aprecian en el mapa \nson los tradicionales seis continentes:\n\n1. África\n 2. América \n3. Antártida\n4. Asia \n5. Europa 6.\n Oceanía\n\nSe especifica que son los seis continentes tradicionales, porque \n hay otras formas de nombrar y enumerar a los continentes. \n Por ejemplo, hay especialistas que consideran que se trata de \n siete continentes.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class sociales(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Sociales")
        Button(text="Sociales",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Sociales", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="La prehistoria",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Diversidad étnica",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Historia de la democracia",command=lambda:self.c()).place(x=400,y=280)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Los continentes",command=lambda:self.d()).place(x=120,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = pre(self.usuario)

    def b(self):
        self.destroy()
        ventana = diversidad_et(self.usuario)

    def c(self):
        self.destroy()
        ventana = historia(self.usuario)

    def d(self):
        self.destroy()
        ventana = continentes(self.usuario)

#compu
class intro(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Introducción")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Introducción", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="\n\nLa computación es la ciencia que se ocupa de los procesos que describen y transforman información.\n A través de su estudio se sientan las bases para el diseño, la programación y el uso de computadoras \ndigitales. Desde hace varios años, son muchos los ámbitos que aprovechan elementos de este campo de \nconocimiento e incorporan computadoras. Solo por citar algunos, se puede mencionar la agricultura (que \nutiliza la computación para realizar análisis de suelos, plagas y hacer un control automático de maquinaria,\n entre otras cosas), la arquitectura (para diseñar, planificar y hacer seguimientos de obras y procesos \narquitectónicos) y la medicina (en la realización de diagnósticos, intervenciones quirúrgicas, etc.). ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class hs(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Hardware y Software")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Hardware y Software", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Label(text="Hardware:\nEl hardware hace referencia a todos los componentes materiales y físicos de un dispositivo,\n es decir, aquellos que se pueden ver y tocar. El monitor, el ratón, la CPU, el teclado o la memoria\n RAM son algunos ejemplos de aquellas partes que, en su conjunto, forman el hardware.\n Este término tiene su origen etimológico en el inglés, donde “hard” significa “duro” \ny “ware”, “cosas”, por lo que se podría definir incluso como “las partes duras\n de una computadora”. Se distinguen dos tipos: interno y perifericos.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        Label(text="Software:\nEl software es la parte digital del ordenador, es decir, el conjunto de instrucciones,\n programas y reglas informáticas que el equipo requiere para funcionar. No tiene, por consiguiente, \nuna existencia física, sino que es intangible e inmaterial, como los programas para \nel procesamiento de textos o el sistema operativo. Este término fue acuñado por el matemático \nJohn Wilder Tukey en 1958 para referirse a los programas que hacían trabajar\n a las calculadoras electrónicas. El software se clasifica en: de sistema,\n aplicacion y de programación.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=260)
        
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class almacenamiento(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Almacenamiento de información")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Almacenamiento de información", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=120,y=20)
        Label(text="\nLos ordenadores actuales se basan en una tecnologia electronica digital, en\ncomparacion a otros dispositivos que utilizan senal analogica.\nPodemos identificar la idea de digital con discreto: en un sistema digital\nas variables de entrada y salida son magnitudes (en general senales\nelectricas) discretas o que se toman como tales, y se procesan como\nvalores discretos. Es decir, solo un numero entero y concreto de valores son\nposibles.\nPor el contrario, podemos identificar la idea de analogico con 'continuo': en\nun sistema analogico sus variables de entrada y salida son magnitudes (en\ngeneral, senales electricas) continuas y se procesan como valores\ncontinuos, es decir, pueden alcanzar cualquier valor dentro de un espectro\ndeterminado.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class sistema(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.geometry("900x500")
        self.usuario = usuario
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Sistema binario")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Sistema binario", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="\nEl sistema binario es un lenguaje que utiliza 2 dígitos binarios, el 0 y el 1, \ndonde cada símbolo constituye un bit, denominado en inglés como binary bit o bit binario.\n 8 bits constituyen un byte y cada byte contiene un caracter, letra o número.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=80,y=90)
        Label(text="\nCódigo binario:  El código binario es el sistema numérico usado para la representación de \ntextos, o procesadores de instrucciones de computadora, utilizando el sistema binario \n(sistema numérico de dos dígitos, o bit: el «0» /cerrado/ y el «1» /abierto/).\n En informática y telecomunicaciones, el código binario se utiliza con variados \nmétodos de codificación de datos, tales como cadenas de caracteres, o cadenas de bits. \nEstos métodos pueden ser de ancho fijo o ancho variable. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=55,y=190)
        
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class computacion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Computación")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Computación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Introducción",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Hardware y Software",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Almacenamiento de información",command=lambda:self.c()).place(x=400,y=280)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Sistema binario",command=lambda:self.d()).place(x=120,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = intro(self.usuario)

    def b(self):
        self.destroy()
        ventana = hs(self.usuario)

    def c(self):
        self.destroy()
        ventana = almacenamiento(self.usuario)

    def d(self):
        self.destroy()
        ventana = sistema(self.usuario)

#ingles
class salu2(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x600")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Saludos y expresiones")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Saludos y expresiones", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=270,y=20)
        Label(text="\nLa mayoría de las expresiones que vamos a ver a continuación constituyen frases \nidiomáticas o modismos. Los modismos son formas del idioma que no obedecen \nalgunas reglas gramaticales y muchas de ellas no tienen traducción literal.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=90)
        Label(text="Buenos Días = Good Morning\n Buenas Tardes = Good Afternoon\n Buenas Noches  = (Al Llegar A Un Lugar) Good Evening\n Buenas Noches = (Para Despedirnos) Good Night\n Por Favor = Please\n Disculpe = Excuse Me\n ¿Cómo está usted? = How Are You?\n Gracias = Thanks\n Gracias (A Usted) = Thank You\n Muchísimas Gracias = Thank You Very Much\n Por Nada, No Hay De Que = You Are Welcome\n Adiós = Good Bye\n Muy Bien = Very Well\n Correcto, Muy Bien = All Right\n Bien = Fine\n Un Poco = A Little\n Un Poquito = A Little Bit ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=190,y=190)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class preguntas(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Preguntas 'Wh'")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Preguntas 'Wh'", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=270,y=20)
        Label(text="\nEn lecciones anteriores ya hemos aprendido a realizar preguntas. Vamos a profundizar un \npoco más para aprender a hacer preguntas más complejas.\nLa estructura de una pregunta básica es:\nQuestion word + auxiliary verb + sujetos + verb+ complement + interrogative form", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=90)
        Label(text="\nWhat = Qué - What is this? ¿Qué es esto?  \nWhere = Dónde - Where is my pen? ¿Dónde está mi lapicero?\nWho = Quién - Quiénes Who are you? ¿Quién eres tú?\nHow = Cómo - How is your father?¿Cómo está tu padre?\nWhich = Cuál - Which is your English classroom, number 11 or 15??\n  ¿Cuál es tu salón de inglés, el salón 11 o el 15??\nWhy= Por qué - Why are you sad? ¿Por qué estas triste?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=170,y=240)
        
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class ingles(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Computación")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Inglés", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Saludos y expresiones",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Preguntas 'Wh'",command=lambda:self.b()).place(x=400,y=110)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = salu2(self.usuario)

    def b(self):
        self.destroy()
        ventana = preguntas(self.usuario)

#biologia
class introduccion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Introducción")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Introducción", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="\nEs la ciencia natural que estudia todo lo relacionado con la vida y lo orgánico,\n incluyendo los procesos, sistemas, funciones, mecanismos u otros caracteres biológicos\n subyacentes a los seres vivos en diversos campos especializados que abarcan su morfología,\n fisiología, filogénesis, desarrollo, evolución, distribución e interacciones en los niveles \nmacroscópico y microscópico.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class org(Tk):
    def __init__(self, usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Organismos vivos")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Organismos vivos", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=280,y=20)
        Label(text="\nUn organismo vivo es el resultado de los procesos bioquímicos que se dan gracias\n a la organización compleja de la materia con la siguiente jerarquía:\n\nCélula: Unidad mínima estructural y funcional de los organismos vivos.\nTejido: Conjunto de células de la misma naturaleza que desempeñan una función en común.\nÓrgano: Grupo de diversos tejidos que forman una unidad funcional.\nAparatos: Sistema de órganos que desempeñan una función particular.\nOrganismo: Resultado de la organización y funcionamiento de los niveles anteriores.\nEspecie: Grupo de seres semejantes entre sí.​\nPoblación: Conjunto de una especie en una área determinada.\nComunidad: Población que interactúa en una área determinada.\nEcosistema: Comunidad que se desarrolla con los medios físicos de un ambiente.\nBiosfera: Conjunto de los recursos donde se desarrolla la vida.\n", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class foto(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Fotosíntesis")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Fotosíntesis", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Label(text="\nProceso químico que se produce en las plantas, las algas y algunos tipos de bacterias \ncuando se exponen a la luz del sol. Durante la fotosíntesis, el agua y el dióxido de carbono \nse combinan para formar carbohidratos (azúcares) y se desprende oxígeno. La fotosíntesis es necesaria \npara la vida de los animales y las plantas.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class evolucion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Evolución")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Evolución", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Label(text="\nLa evolución, en relación con la genómica, se refiere al proceso por el cual los organismos \nvivos cambian con el tiempo a través de cambios en el genoma. Esos cambios evolutivos \nocurren por mutaciones que producen variación genómica, lo que da lugar a la aparición\n de individuos cuyas funciones biológicas o rasgos físicos están alterados. Esos individuos\n que están mejor adaptados a su entorno producen más descendencia que los individuos\n menos adaptados. Por lo tanto, con sucesivas generaciones (que en algunos casos abarcan\n millones de años), una especie puede evolucionar para asumir funciones o características \nfísicas divergentes o, incluso, puede evolucionar en una especie diferente.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=90)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class biologia(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Biología")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Biología", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Introducción",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Organismos vivos",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Fotosíntesis",command=lambda:self.c()).place(x=400,y=280)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Evolución",command=lambda:self.d()).place(x=120,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = introduccion(self.usuario)

    def b(self):
        self.destroy()
        ventana = org(self.usuario)

    def c(self):
        self.destroy()
        ventana = foto(self.usuario)

    def d(self):
        self.destroy()
        ventana = evolucion(self.usuario)

#quimica
class introdu(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Introducción")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Introducción", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nCiencia que estudia la composición y propiedades de las sustancias y las \nreacciones por las que unas sustancias se transforman en otras..", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class atomos(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Átomos")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Átomos", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nParte más pequeña de una sustancia que no se puede descomponer químicamente. Cada átomo\n tiene un núcleo (centro) compuesto de protones (partículas positivas) y neutrones (partículas sin carga).\n Los electrones (partículas negativas) se mueven alrededor del núcleo. Los átomos \nde diferentes elementos contienen diferentes números de protones, neutrones y electrones.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class mol(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("El mol")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="El mol", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="El mol es una de las magnitudes estipuladas por el Sistema Internacional de Unidades (SI).\n Su símbolo es “mol”.\nEl mol es definido como la cantidad de materia que contiene determinado número \nde entidades elementales (átomos, moléculas, etc) equivalente a la cantidad de átomos que hay en \n12 gramos del isótopo carbono-12 (12C).La masa de un mol de sustancia\n (llamada masa molar) es equivalente a la masa atómica o molecular (según se haya considerado \nun mol de átomos o de moléculas) expresada en gramos.El número de Avogadro \n(NA) es la cantidad de partículas ( moléculas, átomos, electrones) \nque contiene un mol de una sustancia cualquiera. Es una constante \nque corresponde al valor de 6,022×10^23 mol-1. Por tanto, 1 mol de cualquier sustancia \ncontiene 6,022×10^23 entidades elementales de esa sustancia.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class quimica(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Química")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Química", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Introducción",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Átomos",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="El mol",command=lambda:self.c()).place(x=260,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = introdu(self.usuario)

    def b(self):
        self.destroy()
        ventana = atomos(self.usuario)

    def c(self):
        self.destroy()
        ventana = mol(self.usuario)

#fisica

class des(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Descripción del movimiento \nen un sistema no inercial")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Descripción del movimiento \nen un sistema no inercial", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=220,y=20)
        #Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nEn mecánica newtoniana se dice que un sistema de referencia es no inercial cuando \nen él no se cumplen las leyes del movimiento de Newton. Dado un sistema de referencia inercial,\n un segundo sistema de referencia será no inercial cuando describa un movimiento acelerado\n con respecto al primero. Fuerzas inerciales como Centrífuga, Coriolis, etc. ", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class ele(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Introducción a la electrostática")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Introducción a la electrostática", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=220,y=20)
        Label(text="\nLa electrostática es la rama de la física que analiza los efectos mutuos que \nse producen entre los cuerpos como consecuencia de sus cargas eléctricas, es decir, \nel estudio de las cargas eléctricas en equilibrio. Leyes de Coulomb y de Gauss. Ecuaciones\n de Laplace y Poisson. Método de imágenes. Funciones de Green. Resolución de problemas \nde contorno en coordenadas cartesianas, esféricas y \ncilíndricas. Multipolos.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class fisica(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Física")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Física", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Descripción del movimiento \nen un sistema no inercial",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Introducción a la electrostática",command=lambda:self.b()).place(x=400,y=110)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = des(self.usuario)

    def b(self):
        self.destroy()
        ventana = ele(self.usuario)

#calculo
class lim(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Límite funcional")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Límite funcional", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=230,y=20)
        Label(text="\nEl límite de una función es un concepto fundamental del análisis matemático \naplicado a las funciones.1​ En particular, el concepto se refiere en análisis real al estudio\n de límites, continuidad y derivabilidad de las funciones reales.\nIntuitivamente, el hecho de que una función f alcance un límite L en un punto c\n significa que, tomando puntos suficientemente próximos a c, el valor de f puede \nser tan cercano a L como se desee. La cercanía de los valores de f y L no \ndepende del valor que adquiere f en dicho punto c.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class fun(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Funciones trigonométricas")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Funciones trigonométricas", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=230,y=20)
        Label(text="\nLas funciones trigonométricas son las funciones de un ángulo. \nEstas usualmente incluyen términos que describen la medición de ángulos y triángulos,\n tal como seno, coseno, tangente, cotangente, secante y cosecante. Los ángulos en las funciones\n trigonométricas se expresan como radianes.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class calculo(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Cálculo")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Cálculo", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Límite funcional",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Funciones trigonométricas",command=lambda:self.b()).place(x=400,y=110)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = lim(self.usuario)

    def b(self):
        self.destroy()
        ventana = fun(self.usuario)

#seminario

class vida(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Proyecto de vida")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Proyecto de vida", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nUn proyecto de vida se refiere a la definición de un plan de lo que se\n desea hacer en la vida. Es una idea que toda persona diseña, con el fin de conseguir \nuno o varios propósitos para su existencia, en otras palabras, se asocia al \nconcepto de realización personal, donde lleva a las personas a definir conscientemente las \nopciones que puede tener para conducir su vida y alcanzar el destino que se propone.\n Un proyecto de vida le da un por qué y un para qué a la existencia humana.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class nacion(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Proyecto nación")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Proyecto nación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nEl proyecto de nación es un ejercicio ciudadano mediante el cual, losmiembros de cada \ncomunidad de investigación del curso de seminario,tienen la oportunidad de plantear por\n escrito sus expectativas y sueñoscon respecto a su país, sabiéndose parte protagonista en los \ncambios ydesarrollo del mismo.Es un plan que refleja una visión de futuro comprometida\n con la mejorade una colectividad. Dentro del programa: Es un ejercicio cívico o actividad \npara iniciar nuestra participación ciudadana. Es un ejercicio deesperanza. No tiene que tener\n un título específico, más que: Proyecto de nación", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class casos(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Estudio de casos")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Estudio de casos", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nEstudio de caso es una herramienta de investigación y una técnica de aprendizaje\n que puede ser aplicado en cualquier área de conocimiento.\nEl objetivo fundamental de los estudios de caso es conocer y comprender \nla particularidad de una situación para distinguir cómo funcionan \nlas partes y las relaciones con el todo.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class seminario(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Seminario")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Seminario", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Proyecto de vida",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Proyecto nación",command=lambda:self.b()).place(x=400,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Estudio de casos",command=lambda:self.c()).place(x=260,y=280)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = vida(self.usuario)

    def b(self):
        self.destroy()
        ventana = nacion(self.usuario)

    def c(self):
        self.destroy()
        ventana = casos(self.usuario)

#programacion
class py(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Python")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Python", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nPython es un lenguaje de alto nivel de programación interpretado cuya filosofía \nhace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones\n de todo tipo, ejemplos: Instagram, Netflix, Panda 3D, entre otros. \n Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente\n la orientación a objetos, programación imperativa y, en menor medida, \nprogramación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

class java(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Java")
        Button(text="Regresar", bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Java", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=320,y=20)
        Label(text="¿Qué es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
        Label(text="\nJava es una plataforma informática de lenguaje de programación creada por\n Sun Microsystems en 1995. Ha evolucionado desde sus humildes comienzos hasta impulsar \nuna gran parte del mundo digital actual, ya que es una plataforma fiable \nen la que se crean muchos servicios y aplicaciones. Los nuevos e innovadores\n productos y servicios digitales diseñados para el futuro también siguen\n basándose en Java.", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=40,y=120)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


class progra(Tk):
    def __init__(self,usuario):
        Tk.__init__(self)
        self.usuario = usuario
        self.geometry("900x500")
        self.configure(bg="blueviolet")
        self.resizable(width=0, height=0)
        self.title("Programación")
        Button(text="Regresar",  bg="#5a189a", fg="White", command=lambda:self.regres()).place(x=835,y=5)
        #Pantalla 
        Label(text="Programación", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=300,y=20)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text=" Python",command=lambda:self.a()).place(x=120,y=110)
        Button(height=10, width=35 , bg="#deaaff", fg="#240046" ,text="Java",command=lambda:self.b()).place(x=400,y=110)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def a(self):
        self.destroy()
        ventana = py(self.usuario)

    def b(self):
        self.destroy()
        ventana = java(self.usuario)

programa = v1()
