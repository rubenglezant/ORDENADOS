
#!/bin/bash
echo `date` - getXML - Recoge el XML del Servidor
wget -O tiempos.json http://localhost/piu-server/rutas.php?parada=23

echo `date` - traduceXML - Traduce el XML a Fichero con Tabla de Llegadas
python transformJSON.py > tablaBus.txt

echo `date` - Comienza a procesar la imagen
python buildImg.py

echo `date` - Backup de la informacion
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
cp out.bmp ./imgs/out-$NOW.bmp
cp tiempos.json ./logs/tiempos-$NOW.json
cp tablaBus.txt ./logs/tablaBus-$NOW.txt





