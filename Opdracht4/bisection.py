def findRoot(f,a,b,epsilon):
    m = float((a+b)/2)
    if abs(b-a) < epsilon:
        return m
    else:
        if f(a)*f(m)<=0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)
            
root = findRoot(lambda x:x-1,0,3,.1)
print(root)