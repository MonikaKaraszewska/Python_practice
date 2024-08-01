import math
from math import  sqrt

number = 10
suma = 0
for i in range(4):
    jeden = math.factorial(4*i)
    dwa = jeden*(1103+26390 *i)
    trzy = (math.factorial(i))**4
    cztery = 396 ** (4*i)
    pod_kr = trzy * cztery
    nad_kreska = jeden * dwa
    result = nad_kreska / pod_kr
    suma += result

przed_suma = 2*(sqrt(2))
dziel = przed_suma / 9801

efekt = dziel * suma
pi = 1 / efekt
print (pi)