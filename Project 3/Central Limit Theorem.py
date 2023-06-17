#Matthew Beck
#Spencer Hernandez

import random

import numpy as np
import matplotlib.pyplot as plt
import statistics

from scipy.stats import norm

zj = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]
x = 1000

def montecarlo(n):
    outerResults = []
    z = []
    global x
    x = 1000
    for i in range(0,550):
        innerResults = []
        for j in range(0, n):
            dist = distFunc()
            innerResults.append(dist)
        avg = sum(innerResults)/len(innerResults)
        outerResults.append(avg)
#Mean---------------------------------------------------------------
    mean = sum(outerResults)/550
    print("Mean(", n ,") = ", mean)
#Variance---------------------------------------------------------------
    var = 0
    for k in range(0,550):
        estmeansq = outerResults[k] * outerResults[k]
        meansq = mean*mean
        var = var + (estmeansq - meansq)
    var = var/550
    print("Variance(",n,") = ", np.sqrt(var))
#Z Values---------------------------------------------------------------
    for l in range(0, 550):
        temp = (outerResults[l] - mean)/np.sqrt(var)
        z.append(temp)
#Fn(Zj)---------------------------------------------------------------
    MAD = 0
    MADj = 0
    MADy = 0
    for p in range(0,7):
        above = 0
        for o in range(0, len(z)):
            if z[o] <= zj[p]:
                above = above + 1
        print("(",n,", ", zj[p],")   P[Zn <= zj] = ", above/len(z))
#MAD---------------------------------------------------------------
        CDF = norm.cdf(zj[p])
        tempMad = np.abs(((above/len(z)) - CDF))
        print("MAD(", p, " ",n, ") = ", tempMad)
        if tempMad > MAD:
            MADj = zj[p]
            MADy = above/len(z)
            MAD = tempMad
        print(MAD)
#Graph---------------------------------------------------------------
        label = "j = " + str(p)
        plt.plot(zj[p], (above/len(z)), '-ro')
        plt.text(zj[p], (above/len(z))+.025, label)
    continuousX = np.linspace(-2.5, 2.5)
    continuousY = norm.cdf(continuousX)
    plt.plot(continuousX, continuousY)
    plt.plot(MADj, MAD, '-go')
    plt.text(MADj, MAD+0.025, "MAD")
    plt.title("Graph when n = " + str(n))
    plt.show()


def distFunc():
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

montecarlo(3)
montecarlo(9)
montecarlo(27)
montecarlo(81)