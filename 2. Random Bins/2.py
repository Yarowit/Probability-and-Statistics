# Zad 2 - Jarosław Socha

# Do losowania używam metody random() zamiast randint() ze względu na zwiększoną szybkość losowania.
# random() przestaje być dobrym generatorem dopiero przy bardzo dużych liczbach ze względu na precyzje,
# ale na cele tego programu i zakresu do 100 000 nie będzie żadnych problemów.
# Źródło: eli.thegreenplace.net/2018/slow-and-fast-methods-for-generating-random-integers-in-python/

from random import *

f = open("results.txt","w")

for n in range(1000, 101000, 1000):
    print(n)
    
    for k in range(50):
        Bn = -1
        Un = -1
        Ln = -1
        Cn = -1
        Dn = -1
        atLeastOne = 0 #liczba urn o conajmniej jedej kuli
        atLeastTwo = 0 #liczba urn o conajmniej dwóch kulach
        urns = [0]*n # tablica urn
        throw = 0 # numer rzutu

        # Pętla aż do n rzutów
        while throw < n:
            throw = throw + 1
            
            index = (int)(n * random())

            if urns[index] == 0:
                atLeastOne = atLeastOne + 1
                
            elif urns[index] == 1:
                if Bn < 0:
                    Bn = throw
                atLeastTwo = atLeastTwo + 1

            urns[index] = urns[index] + 1

        #Wrzucono n kul
        for balls in urns:
            if balls == 0:
                Un = Un + 1
            if balls > Ln:
                Ln = balls

        if Bn < 0:
            Bn = n + 1

        if atLeastOne == n:
            Cn = throw

        # Pętla do końca
        while atLeastTwo < n:
            throw = throw + 1
            
            index = (int)(n * random())
            
            if urns[index] == 0:
                atLeastOne = atLeastOne + 1

                if Cn < 0 and atLeastOne == n:
                    Cn = throw

            elif urns[index] == 1:
                atLeastTwo = atLeastTwo + 1

            urns[index] = urns[index] + 1

        Dn = throw

        f.write(str(Bn) +"\n"+ str(Un) +"\n"+ str(Ln) +"\n"+ str(Cn) +"\n"+ str(Dn)+"\n"+str(Dn-Cn)+"\n")
        
f.close()