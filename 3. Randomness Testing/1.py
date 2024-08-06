import random as r
import secrets as s

fr = open("bitsR.txt","w")
fs = open("bitsS.txt","w")

# for i in range(500):
# fr.write( str(r.randbytes(20)))
# fs.write(str(s.token_bytes(20)))

for i in range(1000000):
    fr.write(str(r.randint(0,1)))
    fs.write(str(s.randbelow(2)))


fr.close()
fs.close()