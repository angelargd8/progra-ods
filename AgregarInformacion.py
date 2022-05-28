import pandas as pd

#columna
#promedio
#usuario - operaciones_basicas
#Mandar columna y usuario
def Agregar(usuario,columna,valor):
    dtf = pd.read_csv('matematica.csv')
    mColumns = list(dtf.columns)
    datos = []
    for x in mColumns:
        if x == 'usuario':
            datos.append(usuario)
        elif x == columna:
            datos.append(valor)
        else:
            datos.append(None)
    newdf = pd.DataFrame([datos],columns=mColumns)
    dtf = pd.concat([dtf,newdf])
    dtf.to_csv('matematica.csv',index=False)

