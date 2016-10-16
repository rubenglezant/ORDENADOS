from haversine import haversine
import redis
import sys
from random import randint

IMEI_ANT = ""
r_server = redis.Redis("localhost")
fd = file('salida.txt', 'w')

def consultar(BT1, bt2_gps):
    a = randint(1, 125000)
    # b = r_server.get("BT"+str(a).zfill(12))
    b = r_server.get(BT1)
    b_str = str(b).split("|")
    bt1_gps = (float(b_str[0]), float(b_str[1]))
    return (haversine(bt1_gps, bt2_gps),bt1_gps)

BTs_ANT = "BT000000000539"
TEMPO_ANT = 0
POS_BTs_ANT = (0.0,0.0)
with open("./dataSorted.dat", "r") as f:
    for line in f:
        partes = line.split("|")
        IMEI = (partes[0])
        #if (IMEI == IMEI_ANT):
        (dist,pos_gps) = consultar(partes[1], POS_BTs_ANT)
        # print ("Consultar - IMEI " + IMEI + " - " + (partes[1]) + " - " + BTs_ANT + " - con diferencia de tiempo en minutos: " + str(int(partes[2]) - TEMPO_ANT) + " Dist: "+str(dist))
        fd.write(IMEI + "|" + (partes[1]) + "|" + BTs_ANT + "|" + str(int(partes[2]) - TEMPO_ANT) + "|"+str(dist))
        IMEI_ANT = IMEI
        BTs_ANT = (partes[1])
        TEMPO_ANT = int(partes[2])
        POS_BTs_ANT = pos_gps

fd.close()
