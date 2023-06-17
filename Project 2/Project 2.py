import numpy as np

def waitTimeFunc(val):
    x = 1000
    a = 24693
    c = 3517
    K = 131072

    for i in range(0,val):
        LCG = ((a * x) + c) % K
        x = LCG
        inv = -12*np.log(1-(LCG/K))
        if (i == 51 or i == 52 or i == 53):
            print(i)
            print(" LCG: ", LCG)
            print(" u: ", LCG/K)
            #print(" x: ", inv)

print(waitTimeFunc(54))