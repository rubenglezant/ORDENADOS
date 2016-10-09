import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta

lista = ['TEF','ITX','CDR','EDR','DGI','ENC','PHM','RLIA','TUB','NTH']

for indice in lista:

    for i in range(4,7):
        df = pd.read_csv('/home/ruben/FINAL2/Mercado_Continuo/AjsutarFichero/valores.csv', sep=';',parse_dates = [4])


        df_EDR = df[df['Ind']==indice].set_index('FechaLectura')

        fecha_1 = datetime(2016, 10, i,8,30,0)
        fecha_2 = datetime(2016, 10, i,17,50,0)

        df_EDR = df_EDR.loc[fecha_1:fecha_2]

        plt.figure()
        df_EDR['Valor'].plot()
        plt.title(indice + " - "+str(i)+"/10/16\nPEPE\nPEPE")
        plt.savefig("./imgs/"+indice+"-"+str(i)+".png")