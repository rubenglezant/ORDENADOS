import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta

df = pd.read_csv('/home/ruben/FINAL2/Mercado_Continuo/AjsutarFichero/valores.csv', sep=';',parse_dates = [4],dtype={'Valor':np.float})

df_EDR = df[df['Ind']=='EDR'].set_index('FechaLectura')

fecha_1 = datetime(2016, 10, 4,8,30,0)
fecha_2 = datetime(2016, 10, 5,17,50,0)

df_EDR = df_EDR.loc[fecha_1:fecha_2]

df_EDR['Valor'].plot()
plt.show()
