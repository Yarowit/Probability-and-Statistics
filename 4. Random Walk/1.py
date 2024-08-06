import numpy as np
import matplotlib.pyplot as plt
import random as r

def wander(N):
    print(N)
    Parr = []
    for k in range(5000):
        #Jedno błądzenie
        if(k % 1000 == 0):
            print(" - "+str(k))
        S = 0
        L = 0
        for i in range(N):
            step = r.randint(0,1) * 2 - 1

            if S > 0 or (S == 0 and step == 1):
                L = L + 1

            S = S + step
        P = L/N
        Parr.append(P)
    return Parr
    
for N in {100,1000,10000}:
    Parr = wander(N)

    count, bins = np.histogram(Parr,20)
    pdf = count / sum(count)
    
    plt.figure()
    plt.hist(bins[:-1], bins, weights=pdf)
    plt.show()