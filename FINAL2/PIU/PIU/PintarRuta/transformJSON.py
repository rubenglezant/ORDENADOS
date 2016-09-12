import json
from pprint import pprint

# Lectura del JSON
with open('tiempos.json') as data_file:    
    data = json.load(data_file)

# Obtencion de los datos para una parada
for i in data:
	print '' + str(i[0]) + '           ' + str(i[1]) + '                           '












