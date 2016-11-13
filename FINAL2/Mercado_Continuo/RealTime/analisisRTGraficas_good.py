import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta

df = pd.read_csv('valores.csv', sep=';',parse_dates = [4])


fecha_1 = datetime(2016, 10, 23,8,30,0)
fecha_2 = datetime(2016, 10, 30,17,50,0)

aux = df[df['FechaLectura']>fecha_1]
aux = df[df['FechaLectura']<fecha_2]

df_EDR = aux[aux['Ind']=='EDR'].set_index('FechaLectura')

plt.figure()
df_EDR['Valor'].plot()
plt.title("EDR - 04/10/16\nPEPE\nPEPE")
plt.savefig("test2.png")
