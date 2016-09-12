__author__ = 'ruben'


# -*- coding: utf-8 -*-
import urllib2, unicodedata
import time
from bs4 import BeautifulSoup

def analisisDescarga(conexion, text_file):
    html = conexion.read()
    soup = BeautifulSoup(html)
    sOut = "";
    # obtenemos una lista de String con la condicin de atributos class con valores details y price
    links = soup.find_all(True, {'class': ['nombre']})
    # la lista alterna valores de nombre de producto y precio
    #   creamos una bandera para diferenciar si es valor o producto
    precio = False
    for tag in links:
        for linea in tag:
            linea = linea.strip().replace('(DVDRip)','');
            sOut += linea + "|"
            href = str(tag['href'])
            # adaptamos unicode a utf-8
            normalizado = unicodedata.normalize('NFKD', linea).encode('ascii', 'ignore')
            # Obtenemos la URL de Descarga
            hrefS = href.split('/')
            urlDest = 'http://www.elitetorrent.net/get-torrent/' + hrefS[2]
            sOut += urlDest + "\n"
            # print (sOut);
            # text_file.write(sOut)
            # sOut = "";
    text_file.write(sOut.encode('utf-8').strip())

# este metodo se conectara con la web y establece un timeout que obliga a reintentar el fallo
# una vez descargada realiza el analisis
def preparar(web, x, text_file):
	#try:
    #    conector = urllib2.urlopen(web, timeout=60)  # timeout de 10 segundos
    #    analisisDescarga(conector, text_file)
    #except:
    #    print("Tiempo de espera agotado, volviendo a intentar")
    #    preparar(web, x, text_file)
    conector = urllib2.urlopen(web, timeout=60)  # timeout de 10 segundos
    analisisDescarga(conector, text_file)


# El CSV separa las columnas por medio de tabuladores
# http://www.elitetorrent.net/categoria/2/peliculas/pag:
# http://www.elitetorrent.net/categoria/13/peliculas-hdrip/pag:
# http://www.elitetorrent.net/categoria/17/peliculas-microhd/pag:
# http://www.elitetorrent.net/categoria/4/series/pag:
#for x in range(1, 2):
    # Ruta de la pagina web
#    url = 'http://www.elitetorrent.net/categoria/1/estrenos/pag:' + str(x)
#    preparar(url, x)
text_file = open("pelis.txt", "a")

for x in (1,10):
    url = 'http://www.elitetorrent.net/categoria/1/estrenos/pag:' + str(x)
    preparar(url, x, text_file)
    time.sleep(60)
    url = 'http://www.elitetorrent.net/categoria/2/peliculas/pag:' + str(x)
    preparar(url, x, text_file)
    time.sleep(60)
    url = 'http://www.elitetorrent.net/categoria/4/series/pag:' + str(x)
    preparar(url, x, text_file)
    time.sleep(60)

text_file.close()
