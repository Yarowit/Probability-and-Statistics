import math
import numpy as np
import matplotlib.pyplot as plt

# Roboczo przybliża supremum funkcji na przedziale
def sup(a, b, f, level = 2):
    if level <= 0 :
        return f( (a + b) / 2.0 )

    max = f(a)
    step = (b - a) / 1000.0
    maxi = a

    for i in np.arange(a, b, step):
        new = f(i)

        if new > max:
            max = new
            maxi = i
    
    return sup(maxi - step, maxi + step, f, level - 1)

# Liczy całkę metodą losowych punktów
def MCIntegral(a, b, f, n):
    M = sup(a, b, f, 3) * 1.2
    X = np.random.uniform(a, b, n)
    Y = np.random.uniform(0, M, n)
    C = 0

    for i in range(0, n):
        if Y[i] <= f(X[i]):
            C = C + 1

    return M * (b - a) * C / n

# Tworzy szukany w zadaniu wykres dla podanego przedziałui funkcji f
def experiment(a, b, f, realIntegral):
    maxStep = 5000
    average = []

    print(99 * "_")

    for n in range(50, maxStep, 50):
        data = []

        for k in range(50):
            data.append(MCIntegral(a, b, f, n))

        plt.scatter([n] * 50, data, color = 'blue')

        average.append(np.average(data))
        
        print(">", end='', flush=True)

    plt.plot([50, maxStep], [realIntegral] * 2, color = 'green')
    
    plt.scatter(range(50, maxStep, 50), average, color = 'red')

    plt.show()


# eksperymenty

val = input("Podpunkt: ")

if val == "1":
    experiment(0, 8, lambda x: x**(1/3.0), 12)
elif val == "2":
    experiment(0, math.pi, lambda x: math.sin(x), 2)
elif val == "3":
    experiment(0, 1, lambda x: 4*x*(1-x)**3, 0.2)
else:
    experiment(-1, 1, lambda x: (1-x**2)**0.5, math.pi/2.0)