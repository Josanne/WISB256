import random
import math


def drop_needle(L):
    x = random.random()
    a = random.vonmisesvariate(0,0) 
    if x<= L/2*math.sin(a):
        print(True)
    else:
        print(False)

drop_needle(1)