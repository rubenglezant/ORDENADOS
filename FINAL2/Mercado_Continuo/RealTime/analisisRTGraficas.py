import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta

# wkhtmltopdf --page-size A3 web-CDR.html bolsa.pdf

#lista = ['TEF', 'ITX', 'CDR', 'EDR', 'DGI', 'ENC', 'PHM', 'RLIA', 'TUB', 'NTH']
lista = ['DGI', 'RLIA', 'A3M', 'BIO', 'CDR', 'OLE', 'EBRO', 'EDR', 'ENO',
       'ENC', 'TRG', 'TUB', 'OHL', 'ZEL', 'NHH', 'FAE', 'ZOT', 'ECR',
       'SNC', 'LBK']
#lista = ['TEF', 'ITX', 'CDR']
# lista = ['EDR']

def pintaUno():
    lista = ['TEF','ITX','CDR','EDR','DGI','ENC','PHM','RLIA','TUB','NTH']

    for indice in lista:

        for i in range(4,16):
            df = pd.read_csv('/home/ruben/temp/temp/valores.csv', sep=';',parse_dates = [4])


            df_EDR = df[df['Ind']==indice].set_index('FechaLectura')

            fecha_1 = datetime(2016, 10, i,8,30,0)
            fecha_2 = datetime(2016, 10, i,17,50,0)

            df_EDR = df_EDR.loc[fecha_1:fecha_2]

            plt.figure()
            df_EDR['Valor'].plot()
            plt.title(indice + " - "+str(i)+"/10/16\nPEPE\nPEPE")
            plt.savefig("./imgs/"+indice+"-"+str(i)+".png")

def pintaDos(diaInicio, diaFin):
    # lista = ['TEF','ITX','CDR','EDR','DGI','ENC','PHM','RLIA','TUB','NTH']

    df = pd.read_csv('valores.csv', sep=';', parse_dates=[4])

    for indice in lista:

        print (indice + " .......")

        min_y = df[df['Ind'] == indice].Valor.min() * 0.98
        max_y = df[df['Ind'] == indice].Valor.max() * 1.02

        for i in range(diaInicio,diaFin):

            #df_EDR = df[df['Ind']==indice].set_index('FechaLectura')
            df_EDR = df[df['Ind'] == indice]

            fecha_1 = datetime(2016, 11, i,8,30,0)
            fecha_2 = datetime(2016, 11, i,17,50,0)

            aux = df_EDR[df_EDR['FechaLectura']>fecha_1]
            aux = aux[aux['FechaLectura']<fecha_2]
            #aux = aux.reset_index()
            aux.set_index('FechaLectura')
            df_EDR = aux
            df_EDR['Valora6'] = df_EDR['Valor']

            #print (df_EDR.describe())

            plt.figure()
            ax1 = aux.plot()
            ax1.set_ylim(min_y, max_y)
            plt.title(indice + " - "+str(i)+"/10/16")
            plt.savefig("./imgs/"+indice+"-"+str(i)+".png")

            # Creamos los datos de interes
            f = open("./imgs/"+indice+"-"+str(i)+".txt","w")
            s = "Max: " + str(df_EDR["Valora6"].max())
            s = s + "\t" +  "Min: " + str(df_EDR["Valora6"].min())
            s = s + "\n" +  "Porcentaje: " + str((df_EDR["Valora6"].max()-df_EDR["Valora6"].min())/df_EDR["Valora6"].max())
            f.write (s + "\n")
            f.close()


def getTextFile(fichero):
    out = ""
    with open(fichero) as f:
        for line in f:
            line = line.split("\n")[0]
            out = out + line + "<br />"
    return out

def creaWeb(diaInicio, diaFin):
    for indice in lista:
        f = open('./webs/web-'+indice+'.html','w')
        f.write('<html><table border="1">' + '\n')

        f.write('<tr>' + '\n')
        for i in range(diaInicio, diaFin):
            f.write('<td><img src="../imgs/'+indice+'-'+str(i)+'.png" width="400px;"/></td>'+'\n')
        f.write('</tr>' + '\n')

        f.write('<tr>' + '\n')
        for i in range(diaInicio, diaFin):
            f.write('<td>'+getTextFile("./imgs/"+indice+"-"+str(i)+".txt")+'</td>'+'\n')
        f.write('</tr>' + '\n')

        f.write('</table></html>' + '\n')
        f.close()

def creaWebDos(diaInicio, diaFin):
    f = open('./webs/web.html', 'w')
    f.write('<html>' + '\n')
    for indice in lista:

        f.write('<h1>' + indice + '</h1>' + '\n')

        f.write('<table border="1">' + '\n')
        f.write('<tr>' + '\n')
        for i in range(diaInicio, diaFin):
            f.write('<td><img src="../imgs/'+indice+'-'+str(i)+'.png" width="400px;"/></td>'+'\n')
        f.write('</tr>' + '\n')

        f.write('<tr>' + '\n')
        for i in range(diaInicio, diaFin):
            f.write('<td>'+getTextFile("./imgs/"+indice+"-"+str(i)+".txt")+'</td>'+'\n')
        f.write('</tr>' + '\n')
        f.write('</table>' + '\n')

    f.write('</html>' + '\n')
    f.close()

pintaDos(7,7+5)
creaWebDos(7,7+5)