#nacitanie kniznic
import random
import math

#mutacia
def mutacia(generacia,M):
    iA = 0
    iB = 0
    while iA == iB:
        iA = random.randint(0,M-1)
        iB = random.randint(0,M-1)
    pomoc = generacia[iA]
    generacia[iA] = generacia[iB]
    generacia[iB] = pomoc

#vzdialenost
def vzd(M, mesta, generacia):
    i = 0
    d = 0
    while i < M-1:
        d += math.sqrt(
            (mesta[int(generacia[i])][0]-mesta[int(generacia[i+1])][0])**2+
            (mesta[int(generacia[i])][1]-mesta[int(generacia[i+1])][1])**2
        )
        i += 1
    d += math.sqrt(
        (mesta[generacia[M-1]][0] - mesta[0][0])** 2 +
        (mesta[generacia[M-1]][1] - mesta[0][1])** 2
    )
    return d
