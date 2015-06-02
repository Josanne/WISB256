import math

class Vector():
    V = []
    def __init__(self,n,vector=0):
        if type(vector) == list:
            self.vector = vector
        else:
            self.vector = [vector]*n

    def __str__(self):
        string = ""
        
        for x in self.vector:
            string += str(x) + '\n'
        return string
        
    def lincomb(self,other,alpha,beta):
        w = []
        #alpha*self+beta*other
        for i in range(len(other.vector)):
            x = alpha*self.vector[i]+beta*other.vector[i]
            w.append(x)
        return Vector(len(w), w)
        
    def scalar(self,alpha):
        return self.lincomb(self, alpha ,0)
        
    def inner(self,other):
        y = 0
        for i in range(len(self.vector)):
            x = self.vector[i] * other.vector[i]
            y += x
        return y
    
    def norm(self):
        return math.sqrt(self.inner(self))
        
    def proj(self,other):
        x = self.inner(other)
        y = self.inner(self)
        z = float(x/y)
        w = self.scalar(z)
        return w

def GrammSchmidt(V):
    W = [V[0].scalar(1/V[0].norm())]
    for i in range(1,len(V)):
        x = Vector(len(V[0].vector))
        for j in range(i):
            # x = som van alle proj.
            y = W[j-1].proj(V[i])
            x = x.lincomb(y,1,1)
        w = V[i].lincomb(x,1,-1)
        W.append(w)
    for i in range(len(V)):
        c = float(1/W[i].norm())
        W[i] = W[i].scalar(c)
    return W


