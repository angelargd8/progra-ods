import pandas as pd
from tkinter import messagebox
def ingrearRegistro(usuario, contra):
    db = pd.read_csv('usuarios.csv')
    flag = True
    for i in range(db.shape[0]):
        tempUsuario = db.at[i,'usuario']
        if tempUsuario.lower() == usuario.lower() :
            flag = False
    if flag:
        index = db.shape[0]
        newdf = pd.DataFrame([[index,usuario.lower(),contra]],columns=db.columns)
        db = pd.concat([db,newdf])
        columnas = list(db.columns)
        db.to_csv('usuarios.csv',index=False)
        messagebox.showinfo('Informacion','Se creo el usuario Correctamente')
    else:
        messagebox.showerror('Error','El usuario ya existe')
    
    return flag

