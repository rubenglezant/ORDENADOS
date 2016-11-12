import pandas as pd

def printAnalsis(indice, df):
    vM = df.describe()['Volume']['mean']

    df['diff'] = df['Low']-df['High']

    df['por_diff_l'] = (df['Low']-df['High'])/df['Low']
    df['por_diff_h'] = (df['Low']-df['High'])/df['High']

    porLow = df['por_diff_l'].mean()
    porHigh= df['por_diff_h'].mean()

    fI = df['Date'].min()
    fF = df['Date'].max()

    separator = '\t'

    print (indice + separator + str(fI) + separator + str(fF) + separator + str(porLow) + separator + str(porHigh) + separator + str(vM))

    return

# Realizamos el calculo para todos los indices
print ("----> Todo el rango de fechas")
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        df = pd.read_csv('./data/'+indice + '.csv')
        printAnalsis(indice, df)

print ("----> Los ultimos 20")
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        df = pd.read_csv('./data/'+indice + '.csv')
        df = df[-20:]
        printAnalsis(indice, df)

print ("----> Los ultimos 5")
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        df = pd.read_csv('./data/'+indice + '.csv')
        df = df[-5:]
        printAnalsis(indice, df)
