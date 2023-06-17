import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

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
for i in range(1, 110):
    X.append(2500)
for i in range(1,110):
    X.append(5000)
for i in range(1,110):
    X.append(10000)

y.append(montecarlo(10))
y.append(montecarlo(30))
y.append(montecarlo(50))
y.append(montecarlo(100))
y.append(montecarlo(250))
y.append(montecarlo(500))
y.append(montecarlo(1000))
y.append(montecarlo(2500))
y.append(montecarlo(5000))
y.append(montecarlo(10000))

#m0 = 0
# for i in montecarlo(10):
#     m0 += i/110
# print("n = 10: m\u2099 =",m0)
#
# m0 = 0
# for i in montecarlo(100):
#     m0 += i/110
# print("n = 100: m\u2099 =",m0)
#
# m0 = 0
# for i in montecarlo(1000):
#     m0 += i/110
# print("n = 1000: m\u2099 =",m0)
#
# m0 = 0
# for i in montecarlo(10000):
#     m0 += i/110
# print("n = 10000: m\u2099 =",m0)

expected = 57*np.sqrt(np.pi/2)
A = 1/57
var = (4-np.pi)/(2 * A * A)
#print(var)

# plt.scatter(X, y)
# plt.semilogx()
# plt.axhline(y=expected, color='r', label="\u03BC\u2093")
# plt.legend()
# plt.xticks([10,30,50,100,250,500,1000,2500,5000,10000],[10,30,50,100,250,500,1000,2500,5000,10000])
# plt.xlabel('$\it{n}$')
# plt.ylabel('$\it{m\u2099}$')
# plt.title("The Law of Large Numbers")
# plt.show()

N = []
D = []
AVGDIFF = 0

for i in range(10,101):
    M = 0
    N.append(i)
    for j in montecarlo(i):
        M += j/110
    #print("n = ",i)
    #print("   m\u2099 =",M)
    diff = M - expected
    if diff < 0:
        diff *= -1
    AVGDIFF += diff/110
    #print("   m\u2099 - \u03BC\u2093=", diff)
    D.append(diff)

P = []

for n in N:
    V = var / n
    P.append( 1 - ( V / (n * 100) ) )

TICK = []
for i in range(10, 101):
    if (i % 5 == 0):
        TICK.append(i)

plt.scatter(N, P)
plt.grid()
plt.xticks(TICK)
plt.xlabel('$\it{n}$')
plt.ylabel('$\it{p}$')
plt.title('$\it{P[|M\u2099^* - \u03BC\u2093| < c] \u2248 p}$ vs n')
plt.show()


# plt.scatter(N,D)
# plt.axhline(y=AVGDIFF, color='r', label="Average of m\u2099 - \u03BC\u2093")
# plt.legend()
# plt.xticks(TICK)
# plt.grid()
# plt.xlabel('$\it{n}$')
# plt.ylabel('$\it{m\u2099 - \u03BC\u2093}$')
# plt.title("Difference of means vs n")
# plt.show()
