from datetime import datetime,timedelta

fecha = datetime(2016, 10, 03, 9, 05)
minuto = timedelta(minutes=1)
indicadores = 0

with open('/home/ruben/tmp/MercadoContinuo/valores_ajustar_2.csv') as f:
    for line in f:

        line = line.replace("\n","")
        line = line.replace("\r","")

        print(line+str(fecha))

        if (indicadores>=10):
            fecha = fecha + minuto
            indicadores = 0
        else:
            indicadores = indicadores + 1

