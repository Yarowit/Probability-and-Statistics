import random as r
import matplotlib.pyplot as plt
import numpy as np
import time

class Node:
    def __init__(self):
        
        self.neighbours = []
        self.checked = False

    def goNext(self):
        return(r.choice(self.neighbours))

    
class Struktura:
    def __init__(self, n):
        self.n = n
        self.nodes = []
        self.visited = 0
        self.time = 0

        for i in range(n):
            self.nodes.append(Node())


    
    def walk(self):
        path = []
        curr = self.start()
        self.nodes[curr].checked = True
        next = curr
        time = 0
        visited = 1

        while visited < self.n:

            next = self.goNext(curr)
            # while next == curr:
            #     next = r.randint(0, self.n - 1)

            curr = next
            path.append(next)

            if self.nodes[next].checked == False:
                self.nodes[next].checked = True
                visited = visited + 1
                
            time = time + 1
        
        # print(path)
        for n in self.nodes:
            n.checked = False

        return time
        
    
    def goNext(self, curr):
        pass
    def start(self):
        pass

class Klika(Struktura):
    def start(self):
        return 0
    def goNext(self, curr):
        next = curr
        while next == curr:
            next = r.randint(0, self.n - 1)
        return next
            
class Ścieżka(Struktura):
    def goNext(self, curr):
        if curr == 0:
            return 1
        
        if curr == self.n-1:
            return self.n-2

        return curr + ( r.randint(0,1) * 2 - 1 )

class Ścieżka1(Ścieżka):
    def start(self):
        return self.n//2

class Ścieżka2(Ścieżka):
    def start(self):
        return 0

class Drzewo(Struktura):
    def __init__(self, n):
        super().__init__(n)
        
        for i in range(n):
            neigh = self.nodes[i].neighbours
            if i != 0:
                neigh.append((i-1)//2)
                    
            if i*2+1 < self.n:
                neigh.append(i*2+1)
            if i*2+2 < self.n:
                neigh.append(i*2+2)

    def start(self):
        return 0
    
    # WYPEŁNIĆ NODY NAJPIERW LICZBOWYMI SĄSIADAMI, POTEM Z NICH LOSOWAĆ
    def goNext(self, curr):
        return r.choice(self.nodes[curr].neighbours)

class Lizak(Struktura):
    def __init__(self, n):
        super().__init__(n)
        self.border = (2*self.n)//3
    def start(self):
        return 0
    
    def goNext(self,curr):
        if curr == self.border - 1:   #łącznik
            next = curr
            while next == curr:
                next = r.randint(0, self.border)
            return next
        if curr < self.border : #klika
            next = curr
            while next == curr:
                next = r.randint(0, self.border - 1)
            return next
        else:                   #ścieżka
            if curr == self.n-1:
                return self.n-2
            return curr + ( r.randint(0,1) * 2 - 1 )


def plot(struktura, maxK):
    
    average = []
    maxN = 1000

    print(99 * "_")

    for n in range(100,maxN,50):
        print("n:",n)
        data = []
        
        graf = struktura(n)
        
        for k in range(maxK):
            data.append(graf.walk())

        plt.scatter([n] * maxK, data, color = 'blue')

        average.append(np.average(data))
        
        print(">", end='', flush=True)
    
    plt.scatter(range(100, maxN, 50), average, color = 'red')

    plt.show()


def main():
    struktury = [Ścieżka2]
    k = 1
    for struktura in struktury:
        plot(struktura, k)


def perf():
    for n in range(100,1000,50):
        print("n:",n)
        
        graf = Drzewo(n)
        
        for k in range(5):
            graf.walk()
# main()

start_time = time.time()
perf()
print(time.time() - start_time)