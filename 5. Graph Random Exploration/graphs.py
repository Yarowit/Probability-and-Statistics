import random as r
import matplotlib.pyplot as plt
import numpy as np
import time
import sympy as s

def plot(name):
    file = open("results/"+name+".txt","r")
    lines = file.readlines()
    average = []

    for i in range(len(lines)):
        n = 100+ i*50

        dataStr = lines[i].split(" ")
        dataStr.pop()
        data = []
        for d in dataStr:
            data.append(int(d))
            

        plt.scatter([n] * len(data), data, color = 'blue')

        average.append(np.average(data))
        
    plt.scatter(range(100, len(lines)*50+100, 50), average, color = 'red')
    
    plt.title(name)
    
    limits(len(lines), average,name)
    plt.show()

def limits(n, averages,name):
    xax = range(100, n*50+100, 50)
    functions = [
        [ averages[i]/(i) for i in range(len(averages)) ],
        [ averages[i]/(i*np.log(n)) for i in range(len(averages)) ],
        [ averages[i]/(i**2) for i in range(len(averages)) ],
        [ averages[i]/(i**3) for i in range(len(averages)) ]
    ]
    labels = [
        "f(n) / n",
        "f(n) / n ln(n)",
        "f(n) / n^2",
        "f(n) / n^3"
    ]
    plt.figure()
    for i in range(len(functions)):
        plt.plot(xax, functions[i], label = labels[i])
    
    plt.title(name)
    plt.legend()


def main():
    plot("klika")
    plot("sciezkaBok")
    plot("sciezkaSrodek")
    plot("drzewo")
    plot("lizak")
    print("done")

main()