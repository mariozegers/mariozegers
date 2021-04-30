import math
import matplotlib.pyplot as plt
import numpy as np

loops = 3
z = 0
T = 283
P = 101300
R = 287
p = P/(R * T)
e = 611 * math.exp((17.27*(T-273))/(237.3 + (T-273)))
q = 0.622 * (e/P)
g = 9.8
a = 0.28 #####

for i in range(loops):
    print("En", str(i) + ":")
    print("z"+str(i)+":", z)
    print("T"+str(i)+":", T)
    print("P"+str(i)+":", P)
    print("p"+str(i)+":", p)
    print("e"+str(i)+":", e)
    print("q"+str(i)+":", q, "\n") 
    zn = z + 6000
    Tn = (T - 273) - a*(zn - z) ####
    z = zn
    P = P*(((Tn)/(T))**(g/(a*R))) ###
    T = Tn
    p = P/(R*T)
    e = 611 * math.exp((17.27*(T-273))/(237.3 + (T-273))) ###
    q = (e/P)

