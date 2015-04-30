import time
import sys
from math import ceil

T1 = time.perf_counter()

N=int(sys.argv[1])

a = list(range(N+1))
a[1] = 0

for i in range(2, N+1):
    if a[i] != 0:
        for j in range(2 , ceil(N/2)+1):
            if j*i<N+1:
                a[j*i] = 0

T2 = time.perf_counter()

outfile = sys.argv[2]
data = open(outfile,'w')

count = 0
for i in a:
    if i != 0:
        count+=1
        data.write(str(i) + "\n")

data.close()

print('Found ', count, ' Prime numbers smaller than ', N, ' in ', T2-T1, 'sec.')