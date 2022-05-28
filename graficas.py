import pandas as pd
import matplotlib.pyplot as plt

def estadisticasMate(columna):
    dtf = pd.read_csv('matematica.csv',skipinitialspace=True)
    grf = dtf[['usuario','operaciones_basicas']]
    grf = grf.groupby('usuario').mean()
    grf.plot(kind='bar')
    plt.show()