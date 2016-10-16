# 7,359262, -77,150505
# -1,321474, -70,273064

import random
import redis
import sys
from random import randint

# ----- Populate
r_server = redis.Redis("localhost")

for i in range (0,125000):
    a = random.uniform(-1.321474, 7.359262)
    b = random.uniform(-77.150505, -70.273064)
    a_str = "{:.6f}".format(a)
    b_str = "{:.6f}".format(b)
    r_server.set("BT"+str(i).zfill(12), a_str+"|"+b_str)
