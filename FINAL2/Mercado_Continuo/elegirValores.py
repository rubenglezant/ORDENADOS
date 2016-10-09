import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

def printAnalsis(indice, df, porcentaje):
    vM = df.describe()['Volume']['mean']

    df['diff'] = df['Low']-df['High']

    df['por_diff_l'] = (df['Low']-df['High'])/df['Low']
    df['por_diff_h'] = (df['Low']-df['High'])/df['High']

    porLow = df['por_diff_l'].mean()
    porHigh= df['por_diff_h'].mean()

    fI = df['Date'].min()
    fF = df['Date'].max()

    df['value'] = (df['Open']+df['Close'])/2
    valor = df['value'].mean()

    separator = '\t'

    if (porcentaje<abs(porLow)):
        print (indice + separator + str(fI) + separator + str(fF) + separator + str(porLow) + separator + str(porHigh) + separator + str(vM) + separator + str(valor))

    return

diasEleccion = -10
porcentajeEleccion = 0.030
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        df = pd.read_csv('./data/'+indice + '.csv')
        df = df[diasEleccion:]
        printAnalsis(indice, df, porcentajeEleccion)
