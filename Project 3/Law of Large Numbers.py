#Matthew Beck
#Spencer Hernandez
import random

import numpy as np
import matplotlib.pyplot as plt
import statistics

# randVals = []
# randVals.append(1000)

x = 1000

def montecarlo(n):
    outerResults = []
    for i in range(1,110):
        innerResults = []
        for j in range(1, n):
            dist = distFunc(j+((i-1)*n))
            innerResults.append(dist)
        avg = sum(innerResults)/len(innerResults)
        outerResults.append(avg)
    return outerResults




def distFunc(val):
    a = 24693
    c = 3967
    K = 262144
    inv = 0
    global x
    LCG = ((a * x) + c) % K

    x = LCG
    inv = 57*np.sqrt(-2*np.log(1-(LCG/K)))
        #-12*np.log(1-(LCG/K))
        #print(i)
        #print(" LCG: ", LCG)
        #print(" u: ", LCG/K)
        #print(" X: ", inv)

    return inv

X = []
y = []

for i in range(1,110):
    X.append(10)
for i in range(1,110):
    X.append(30)
for i in range(1,110):
    X.append(50)
for i in range(1,110):
    X.append(100)
for i in range(1,110):
    X.append(250)
for i in range(1,110):
    X.append(500)
for i in range(1,110):
    X.append(1000)


y.append(montecarlo(10))
y.append(montecarlo(30))
y.append(montecarlo(50))
y.append(montecarlo(100))
y.append(montecarlo(250))
y.append(montecarlo(500))
y.append(montecarlo(1000))

expected = 57*np.sqrt(np.pi/2)

plt.scatter(X, y)
plt.semilogx()
plt.axhline(y=expected, color='r', label="\u03BC\u2093")
plt.legend()
plt.xticks([10,30,50,100,250,500,1000],[10,30,50,100,250,500,1000])
plt.xlabel('$\it{n}$')
plt.ylabel('$\it{m\u2099}$')
plt.title("The Law of Large Numbers")
plt.show()
