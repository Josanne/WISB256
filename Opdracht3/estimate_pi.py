import random
import math
import sys

if len(sys.argv) < 3:
    print("Use: estimate_pi.py N L")
    exit()
if len(sys.argv) > 3:
    random.seed(int(sys.argv[3]))
    

def drop_needle(L):
    x0 = random.random()
    a = random.vonmisesvariate(0,0)
    x1 = x0 + L*math.cos(a)
    if x1 > 1 or x1 < 0:
        return True
    else:
        return False


L = float(sys.argv[2])
#assert L <= 1, "L should be smaller than 1"

count = 0
N = int(sys.argv[1]) 
for i in range(N+1):
    if drop_needle(L) == True:
        count += 1

if L<=1:
    pi = float((2 * L * N) / count)
else:
    pi = (2 * L - 2 * (math.sqrt(L**2-1)+math.asin(1/L))) / (count/N - 1)
    
print(count , "hits in" , N , "tries")
print("Pi =", pi)