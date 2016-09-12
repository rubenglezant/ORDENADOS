#!/usr/bin/python
# Obtiene los datos de la Web

import urllib2
import base64
import json


def GetAtributoEspecial(idOportunidad, nombreAtributo):
    # Obtenemos los atributos especiales
    username = '2d486e42771eee18125b8aef3afe216d'
    password = '4c2TNRdi'
    req = urllib2.Request('https://infeci.capsulecrm.com/api/opportunity/'+idOportunidad+'/customfields')
    base64string = base64.b64encode('%s:%s' % (username, password))
    req.add_header("Authorization", "Basic %s" % base64string)
    req.add_header("Accept", "application/json")
    response = urllib2.urlopen(req)
    data = json.load(response)
    try:
        for value in data['customFields']['customField']:
            if (value['label']==nombreAtributo):
                s = value['number']
                break
            else:
                s = ""
    except:
        s = ""
    return s


# Construimos el Array de Clientes
username = '2d486e42771eee18125b8aef3afe216d'
password = '4c2TNRdi'

req = urllib2.Request('https://infeci.capsulecrm.com/api/party')
base64string = base64.b64encode('%s:%s' % (username, password))
req.add_header("Authorization", "Basic %s" % base64string)
req.add_header("Accept", "application/json")
response = urllib2.urlopen(req)
data = json.load(response)

clientes = {}
for op in data['parties']['organisation']:
    clientes[op['id']] = op['name']

# Recogemos el conjunto de oportunidades
username = '2d486e42771eee18125b8aef3afe216d'
password = '4c2TNRdi'

req = urllib2.Request('https://infeci.capsulecrm.com/api/opportunity')
base64string = base64.b64encode('%s:%s' % (username, password))
req.add_header("Authorization", "Basic %s" % base64string)
req.add_header("Accept", "application/json")
response = urllib2.urlopen(req)
data = json.load(response)


# Creamos el CSV con las oportunidades
atributos = ['name','probability','expectedCloseDate','createdOn','updatedOn','value','currency','partyId','milestoneId','milestone','owner','id','durationBasis']

s = ""
s = s + "Cliente" + ","
for atr in atributos:
    s = s + atr + ","
s = s + "Margen" + ","
s = s + "Grafo" + ","
s = s + "\n"

for op in data['opportunities']['opportunity']:
    s = s + clientes[str(op['partyId'])] + ","
    for atr in atributos:
        try:
            s = s + op[atr] + ","
        except:
            s = s + "" + ","
    s = s + (GetAtributoEspecial(op['id'],'Margen')) + ","
    s = s + (GetAtributoEspecial(op['id'],'Grafo')) + ","
    s = s + "\n"


# Ajustamos para crear el CSV
s = s.replace(",","|")
s = s.replace(".",",")

print (s.encode("utf8"))

text_file = open("oportunidades.csv", "w")
text_file.write(s.encode("utf8"))
text_file.close()




