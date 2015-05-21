import math
def findRoot(f,a,b,epsilon):
    m = float((a+b)/2)
    if abs(b-a) < epsilon:
        return m
    else:
        if f(a)*f(m)<=0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)
            
root = findRoot(lambda x:math.cos(x),0,3,.1)
print(root)

def findAllRoots(f,a,b,epsilon):
    m = float((a+b)/2)
    roots = []
    if abs(b-a) < epsilon:
        roots.append(m)
        return roots
    else: 
        if f(a)*f(m)<=0:
            roots.extend(findAllRoots(f,a,m,epsilon))
        if f(b)*f(m)<=0:
            roots.extend(findAllRoots(f,m,b,epsilon))
        
        return roots
x = findAllRoots(lambda x:math.sin(x),1,9,.1)
print(x)