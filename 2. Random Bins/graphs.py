
# Grafy - Jarosław Socha

import numpy as np
import matplotlib.pyplot as plt

points = 100

f = open("results.txt","r")

Bn = []
Un = []
Ln = []
Cn = []
Dn = []
DCn = []

for n in range(points):
    dataArr = [[],[],[],[],[],[]]
    
    for i in range (50):
        for j in range(6):
            dataArr[j].append( (int) (f.readline()) )
    Bn.append(dataArr[0])
    Un.append(dataArr[1])
    Ln.append(dataArr[2])
    Cn.append(dataArr[3])
    Dn.append(dataArr[4])
    DCn.append(dataArr[5])

data = [Bn,Un,Ln,Cn,Dn,DCn]
averages = [[],[],[],[],[],[]]
labels = ["Bn","Un","Ln","Cn","Dn","Dn - Cn"]
for i in range(6):
    plt.figure()

    for j in range(points):
        plt.scatter([(j+1)*1000] * 50, data[i][j], color = 'blue')
        averages[i].append(np.average(data[i][j]))

    plt.scatter(range(1000, (points+1)*1000, 1000), averages[i], color = 'red')
    plt.ylabel(labels[i])
    plt.xlabel("Urny")
    plt.gcf().set_size_inches(16, 9)
    plt.savefig(str(i)+"fig.svg")

def plots():
    xax = range(1000, (points+1)*1000, 1000)
    labels = [
        "b(n) / n",
        "b(n) / √n",
        "u(n) / n",
        "l(n) / ln(n)",
        "l(n) / ( ln(n) / ln(ln(n)) )",
        "l(n) / ln(ln(n))",
        "c(n) / n",
        "c(n) / ( n ln(n) )",
        "c(n) / n^2",
        "d(n) / n",
        "d(n) / ( n ln(n) )",
        "d(n) / n^2",
        "d(n) - c(n) / n",
        "d(n) - c(n) / ( n ln(n) )",
        "d(n) - c(n) / ( n ln(ln(n)) )"
    ]

    functions = [
        [ averages[0][n]/(n) for n in range(points) ],
        [ averages[0][n]/(n**0.5) for n in range(points) ],

        [ averages[1][n]/(n) for n in range(points) ],

        [ averages[2][n]/(np.log(n)) for n in range(points) ],
        [ averages[2][n]/(np.log(n)/np.log(np.log(n))) for n in range(points) ],
        [ averages[2][n]/(np.log(np.log(n))) for n in range(points) ],

        [ averages[3][n]/(n) for n in range(points) ],
        [ averages[3][n]/(n*np.log(n)) for n in range(points) ],
        [ averages[3][n]/(n*n) for n in range(points) ],

        [ averages[4][n]/(n) for n in range(points) ],
        [ averages[4][n]/(n*np.log(n)) for n in range(points) ],
        [ averages[4][n]/(n*n) for n in range(points) ],
        
        [ averages[5][n]/(n) for n in range(points) ],
        [ averages[5][n]/(n*np.log(n)) for n in range(points) ],
        [ averages[5][n]/(n*np.log(np.log(n))) for n in range(points) ]
    ]

    for i in range(15):
    
        plt.figure()
        plt.scatter(xax, functions[i-12])
        plt.ylabel(labels[i])
        plt.xlabel("Urny")
        # plt.xscale('log') - ta linijka pozwala czasami na zmianę osi x na logarytm
    
        plt.gcf().set_size_inches(16, 9)
        plt.savefig("logs/"+str(i)+"fig2.svg")

plots()
print("Gotowe")