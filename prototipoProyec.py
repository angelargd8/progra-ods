""" Autores: Gabriel Gerardo Pineda Riveiro  #22880
             Sergio Alejandro Orellana Colindres #221122
             Angela Rosana Garcia Donis #22869
             Alisson Anette López Barrientos #221011
    Fase #04
    Recursos: python 3.10
    Catedratico: Ludwing Cano
    Auxiliares: Daniela Villamar y José Perez
    ultima fecha de modificacion: 13/05/2022

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
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Comunicación", command=lambda:self.comu()).place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Ciencias naturales", command=lambda:self.cs()).place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Sociales", command=lambda:self.ss()).place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Computación").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Inglés").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)
        
    def comu(self):
        self.destroy()
        ventana = comunicacion(self.usuario)

    def cs(self):
        self.destroy()
        ventana = ciencias(self.usuario)

    def ss(self):
        self.destroy()
        ventana = sociales(self.usuario)
        
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
        Button(height=2, width=50 , bg="#deaaff", fg="#240046", text="Matemáticas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Comunicación", command=lambda:self.comu()).place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Quimica").place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Seminario").place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046",text="Computación").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)
    def comu(self):
        self.destroy()
        ventana = comunicacion(self.usuario)

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
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Matematicas",command=lambda:self.ventana3()).place(x=280,y=110)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Química").place(x=280,y=170)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Biología").place(x=280,y=230)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Física").place(x=280,y=290)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=350)
        Button(height=2, width=50 , bg="#deaaff", fg="#240046" ,text="Programación").place(x=280,y=410)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)


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
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Derivadas").place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Integrales").place(x=520,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Geometría").place(x=40,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Cálculo").place(x=280,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones líneales").place(x=520,y=200)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ecuaciones cuadraticas").place(x=40,y=290)
        if self.usuario == 'gerax5' or self.usuario == 'angela':
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Estadisticas matematicas").place(x=350,y=400)
        self.mainloop()

    def regres(self):
        self.destroy()
        ventana = v2(self.usuario)

    def operaciones(self):
        self.destroy()
        ventana = opera(self.usuario)

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
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Derivadas").place(x=280,y=110)
        Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Integrales").place(x=520,y=110)
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
        ventana = pantallaOperacionBasica(self.usuario,accion)


class pantallaOperacionBasica(Tk):
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
            Label(text="Operación aritmética que consiste en calcular el resultado (producto)\n de sumar un mismo número (multiplicando) tantas veces como\n indica otro número (multiplicador)\n se representa con los signos · o ×.", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="5 * 5 = 25", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="7 * 30 = 210", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('multiplicacion')).place(x=370,y=390)
        if accion == 'division':
            self.title("division")
            Label(text="Divison", fg="White", bg="blueviolet", font=("Times New Roman",30)).place(x=390,y=20)
            Label(text="¿Que es?", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=80)
            Label(text="Operacion aritmetica que consiste en la separación o partición\n de un todo en partes. Usual mente se representa por '/'", font=("Times New Roman",15)).place(x=260,y=120)
            Label(text="Ejemplos:", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=50,y=220)
            Label(text="5 / 5 = 1", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=300)
            Label(text="80 / 8 = 10", fg="White", bg="blueviolet", font=("Times New Roman",15)).place(x=90,y=350)
            Button(height=2, width=30 , bg="#deaaff", fg="#240046" ,text="Ejercicio",command=lambda:self.ejercic('division')).place(x=370,y=390)
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
            r1 = int(self.c1.get())
            r2 = int(self.c2.get())
            r3 = int(self.c3.get())
            r4 = int(self.c4.get())
            r5 = int(self.c5.get())
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
            ag.Agregar(self.usuario,'operaciones_basicas',puntos)
        except:
            messagebox.showerror("Error", "Debe de ingresar números válidos")
        if puntos == 5:
            messagebox.showinfo("Informacion","Obtuviste todo correcto")
        else:
            messagebox.showinfo("Informacion","Obtuviste "+str(puntos)+" buenas en este ejercicio")

        self.regresar()

    def regresar(self):
        self.destroy()
        ventana = opera(self.usuario)


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

programa = v1()
