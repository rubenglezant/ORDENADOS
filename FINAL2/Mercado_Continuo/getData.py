import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 9, 30)

with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        f = web.DataReader(indice, 'yahoo', start, end)
        f.to_csv('./data/'+indice+'.csv')
        print ("*** " + line)
